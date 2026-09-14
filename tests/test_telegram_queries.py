import unittest
from unittest.mock import AsyncMock
from types import SimpleNamespace

from core.service import telegram


class Queries(unittest.IsolatedAsyncioTestCase):
    async def test_reply_parameters(self):
        client = SimpleNamespace(send_message=AsyncMock())
        await telegram.send_message(client, -100123, 'reply', reply_to_message_id=42)
        params = client.send_message.call_args.kwargs
        self.assertNotIn('reply_to_message_id', params)
        self.assertEqual(params['reply_parameters'].message_id, 42)
        await telegram.send_message(client, -100123, 'ordinary')
        self.assertIsNone(client.send_message.call_args.kwargs['reply_parameters'])

    async def test_history_cursor_and_end(self):
        calls = []

        async def history(target, **kwargs):
            calls.append(kwargs)
            yield SimpleNamespace(id=kwargs['max_id'])

        client = SimpleNamespace(get_chat_history=history)
        messages = await telegram.get_messages(client, -100123, offset_id=50)
        self.assertEqual(messages[0].id, 49)
        self.assertNotIn('offset_id', calls[0])
        self.assertEqual(await telegram.get_messages(client, -100123, offset_id=1), [])
        self.assertEqual(len(calls), 1)

    async def test_author_filter_is_server_side(self):
        calls = []

        async def search(target, **kwargs):
            calls.append(kwargs)
            yield SimpleNamespace(id=40)

        await telegram.search_messages(
            SimpleNamespace(search_messages=search), -100123, '',
            from_user='me', max_id=50, limit=100,
        )
        self.assertEqual(calls[0]['from_user'], 'me')
        self.assertEqual(calls[0]['max_id'], 50)
        self.assertEqual(calls[0]['limit'], 100)
