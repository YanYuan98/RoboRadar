import unittest
from unittest.mock import patch

from roboradar.llm import OpenAICompat


class OpenAICompatTests(unittest.TestCase):
    @patch("openai.OpenAI")
    def test_api_key_is_forwarded(self, openai_cls):
        OpenAICompat({
            "openai_base_url": "https://api.deepseek.com",
            "openai_api_key": "secret-key",
            "openai_model": "deepseek-chat",
            "timeout": 42,
        })

        openai_cls.assert_called_once_with(
            base_url="https://api.deepseek.com",
            api_key="secret-key",
            timeout=42,
        )

    @patch("openai.OpenAI")
    def test_unauthenticated_endpoint_can_leave_api_key_empty(self, openai_cls):
        OpenAICompat({
            "openai_base_url": "http://localhost:11434/v1",
            "openai_api_key": "",
            "openai_model": "local-model",
        })

        openai_cls.assert_called_once_with(
            base_url="http://localhost:11434/v1",
            api_key="not-needed",
            timeout=180,
        )


if __name__ == "__main__":
    unittest.main()
