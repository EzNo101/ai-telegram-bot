from collections.abc import AsyncGenerator

from openai import AsyncOpenAI

from src.config import settings


class ChatService:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )

    async def generate_response(self, prompt: str) -> AsyncGenerator[str]:
        response = await self.client.chat.completions.create(
            model=settings.MODEL,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )
        async for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                yield content
