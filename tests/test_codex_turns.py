import asyncio
import unittest
from unittest.mock import AsyncMock, patch

from core.service import codex


class TurnTests(unittest.IsolatedAsyncioTestCase):
    async def test_old_completion_does_not_finish_new_turn(self):
        events = asyncio.Queue()
        for method, fields in [
            ("turn/completed", {"turn": {"id": "old", "status": "interrupted"}}),
            ("item/completed", {"turnId": "new", "item": {
                "type": "agentMessage", "id": "answer", "phase": "final_answer", "text": "Done"
            }}),
            ("turn/completed", {"turn": {"id": "new", "status": "completed"}}),
        ]:
            events.put_nowait({"method": method, "params": {"threadId": "thread", **fields}})
        with patch.object(codex._state, "events", events), patch.object(codex._state, "timeout", 0):
            self.assertEqual(await codex._wait_for_turn("thread", "new"), "Done")

    async def test_explicit_timeout_interrupts(self):
        with (
            patch.object(codex._state, "events", asyncio.Queue()),
            patch.object(codex._state, "timeout", 0.01),
            patch.object(codex, "_is_ready", return_value=True),
            patch.object(codex, "_interrupt", new_callable=AsyncMock) as interrupt,
        ):
            with self.assertRaisesRegex(codex.CodexError, "вовремя"):
                await codex._wait_for_turn("thread", "new")
            interrupt.assert_awaited_once_with("thread", "new")

    async def test_unlimited_wait_detects_disconnect(self):
        with (
            patch.object(codex._state, "events", asyncio.Queue()),
            patch.object(codex._state, "timeout", 0),
            patch.object(codex, "_is_ready", return_value=False),
        ):
            with self.assertRaisesRegex(codex.CodexError, "закрыто"):
                await asyncio.wait_for(codex._wait_for_turn("thread", "new"), 2)
