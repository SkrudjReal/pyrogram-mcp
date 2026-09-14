import asyncio
import unittest
from unittest.mock import patch

from core.service import codex


class StreamTests(unittest.IsolatedAsyncioTestCase):
    async def test_frame_larger_than_previous_limit(self):
        stream = asyncio.StreamReader(limit=65536)
        payload = b'x' * (9 * 1024 * 1024)
        stream.feed_data(payload + b'\n{}\nlast')
        stream.feed_eof()
        result = [line async for line in codex._stream_lines(stream)]
        self.assertEqual(result, [payload, b'{}', b'last'])

    async def test_fragmented_utf8_and_newlines(self):
        stream = asyncio.StreamReader(limit=4)
        async def feed():
            for byte in 'привет\n\nмир\n'.encode():
                stream.feed_data(bytes([byte]))
                await asyncio.sleep(0)
            stream.feed_eof()
        task = asyncio.create_task(feed())
        result = [line async for line in codex._stream_lines(stream)]
        await task
        self.assertEqual(result, ['привет'.encode(), b'', 'мир'.encode()])

    async def test_frame_size_guard(self):
        stream = asyncio.StreamReader()
        stream.feed_data(b'x' * 17)
        stream.feed_eof()
        with patch.object(codex, 'MAX_RPC_FRAME', 16):
            with self.assertRaises(codex.CodexError):
                _ = [line async for line in codex._stream_lines(stream)]
