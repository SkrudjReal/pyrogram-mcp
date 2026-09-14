from __future__ import annotations

import re
from html import escape


_CODE_SPAN = re.compile(r"`([^`\n]+)`")
_LINK = re.compile(r"\[([^\]\n]+)\]\(((?:https?|tg|mailto)://[^\s)]+)\)")
_TAG = re.compile(
    r"</?(?:b|strong|i|em|u|s|strike|del|pre|blockquote)\s*>"
    r'|</?code(?:\s+class="language-[A-Za-z0-9_-]+")?\s*>'
    r'|<a\s+href=(?:"[^"]*"|\'[^\']*\')\s*>|</a>',
    re.IGNORECASE,
)
_ENTITY = re.compile(r"&(?:amp|lt|gt|quot|#\d+|#x[0-9a-f]+);")
_FENCE = re.compile(r"^\s*```(?:\S+)?\s*$")
_HEADING = re.compile(r"^\s{0,3}\\?#{1,6}\s+(.+?)\s*#*\s*$")
_QUOTE = re.compile(r"^\s*\\?>\s?(.*)$")
_UNORDERED = re.compile(r"^\s*\\?([-+*])\s+(.+)$")
_ORDERED = re.compile(r"^\s*(\d+[.)])\s+(.+)$")
_HORIZONTAL_RULE = re.compile(r"^\s*(?:[-*_]\s*){3,}$")
_HTML_TOKEN = re.compile(r"<[^>]+>|&(?:amp|lt|gt|quot|#\d+|#x[0-9a-f]+);")
_OPEN_TAG = re.compile(r"^<(b|strong|i|em|u|s|strike|del|pre|blockquote|code|a)(?:\s[^>]*)?>$", re.I)
_CLOSE_TAG = re.compile(r"^</(b|strong|i|em|u|s|strike|del|pre|blockquote|code|a)>$", re.I)


def _inline_to_html(value: str) -> str:
    replacements: list[str] = []

    def protect(fragment: str) -> str:
        token = f"\x00{len(replacements)}\x00"
        replacements.append(fragment)
        return token

    value = _TAG.sub(lambda match: protect(match.group(0)), value)
    value = _ENTITY.sub(lambda match: protect(match.group(0)), value)
    value = _CODE_SPAN.sub(
        lambda match: protect(f"<code>{escape(match.group(1))}</code>"),
        value,
    )
    value = re.sub(r"\\([\\`*_[\]{}()#+.!<>|~\-])", r"\1", value)
    value = _LINK.sub(
        lambda match: protect(
            f'<a href="{escape(match.group(2), quote=True)}">'
            f"{_inline_to_html(match.group(1))}</a>"
        ),
        value,
    )
    value = escape(value, quote=False)
    value = re.sub(r"\*\*(\S(?:.*?\S)?)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"__(\S(?:.*?\S)?)__", r"<b>\1</b>", value)
    value = re.sub(r"~~(\S(?:.*?\S)?)~~", r"<s>\1</s>", value)
    value = re.sub(r"(?<![\w*])\*(\S(?:.*?\S)?)\*(?![\w*])", r"<i>\1</i>", value)
    value = re.sub(r"(?<!\w)_(\S(?:.*?\S)?)_(?!\w)", r"<i>\1</i>", value)
    for index, replacement in enumerate(replacements):
        value = value.replace(f"\x00{index}\x00", replacement)
    return value


def markdown_to_telegram_html(markdown: str) -> str:
    lines = markdown.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    rendered: list[str] = []
    code_lines: list[str] = []
    in_fence = False
    index = 0
    while index < len(lines):
        line = lines[index]
        if in_fence:
            if _FENCE.fullmatch(line):
                rendered.append(f"<pre><code>{escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                in_fence = False
            else:
                code_lines.append(line)
            index += 1
            continue
        if _FENCE.fullmatch(line):
            in_fence = True
            index += 1
            continue

        quote = _QUOTE.match(line)
        if quote:
            quote_lines = [quote.group(1)]
            index += 1
            while index < len(lines):
                next_quote = _QUOTE.match(lines[index])
                if not next_quote:
                    break
                quote_lines.append(next_quote.group(1))
                index += 1
            rendered.append(f"<blockquote>{chr(10).join(_inline_to_html(item) for item in quote_lines)}</blockquote>")
            continue

        heading = _HEADING.match(line)
        if heading:
            rendered.append(f"<b>{_inline_to_html(heading.group(1))}</b>")
        elif _HORIZONTAL_RULE.fullmatch(line):
            rendered.append("")
        elif unordered := _UNORDERED.match(line):
            rendered.append(f"• {_inline_to_html(unordered.group(2))}")
        elif ordered := _ORDERED.match(line):
            rendered.append(f"{ordered.group(1)} {_inline_to_html(ordered.group(2))}")
        else:
            rendered.append(_inline_to_html(line))
        index += 1

    if in_fence:
        rendered.append(f"<pre><code>{escape(chr(10).join(code_lines))}</code></pre>")
    return "\n".join(rendered).strip()


def telegram_html_chunks(text: str, limit: int = 3900) -> list[str]:
    if not text:
        return []

    chunks: list[str] = []
    current: list[str] = []
    active: list[tuple[str, str]] = []

    def closing_tags() -> str:
        return "".join(f"</{name}>" for name, _ in reversed(active))

    def flush() -> None:
        nonlocal current
        if not current:
            return
        current.append(closing_tags())
        chunks.append("".join(current))
        current = [opening for _, opening in active]

    def append_text(value: str) -> None:
        nonlocal current
        while value:
            available = limit - len("".join(current)) - len(closing_tags())
            if available <= 0:
                flush()
                continue
            if len(value) <= available:
                current.append(value)
                return
            cut = max(value.rfind("\n", 0, available + 1), value.rfind(" ", 0, available + 1))
            if cut <= 0:
                cut = available
            current.append(value[:cut])
            value = value[cut:]
            flush()

    def append_token(token: str) -> None:
        nonlocal current
        if len("".join(current)) + len(token) + len(closing_tags()) > limit:
            flush()
        current.append(token)
        if entity := _OPEN_TAG.fullmatch(token):
            active.append((entity.group(1).lower(), token))
        elif entity := _CLOSE_TAG.fullmatch(token):
            name = entity.group(1).lower()
            for position in range(len(active) - 1, -1, -1):
                if active[position][0] == name:
                    del active[position]
                    break

    position = 0
    for match in _HTML_TOKEN.finditer(text):
        append_text(text[position : match.start()])
        append_token(match.group(0))
        position = match.end()
    append_text(text[position:])
    if current:
        chunks.append("".join(current))
    return [chunk for chunk in chunks if chunk]
