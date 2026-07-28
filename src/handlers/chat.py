import asyncio

from aiogram import Bot, Router
from aiogram.exceptions import TelegramRetryAfter
from aiogram.types import Message

from src.services.chat import ChatService

router = Router()

chat_service = ChatService()


@router.message()
async def chat_handler(message: Message, bot: Bot):
    if not message.text:
        await message.answer("Please send a text message.")
        return
    user_id = message.from_user.id  # type: ignore
    username = message.from_user.username  # type: ignore
    chat_id = message.chat.id  # type: ignore
    print(
        f"Received message from user {username} (ID: {user_id}, chat ID: {chat_id}): {message.text}"
    )

    try:
        await bot.send_message_draft(
            chat_id=message.chat.id,
            draft_id=message.message_id,
            text="",
        )
    except TelegramRetryAfter as e:
        print(f"Rate limit exceeded. Retry after {e.retry_after} seconds.")
        await asyncio.sleep(e.retry_after)
    except Exception as e:  # noqa: BLE001
        print(f"Error occurred while sending message draft: {e}")
    full_text = ""
    async for chunk in chat_service.generate_response(message.text):
        full_text += chunk
        await bot.send_message_draft(
            chat_id=message.chat.id,
            draft_id=message.message_id,
            text=full_text,
        )
        await asyncio.sleep(0.5)

    await message.answer(full_text)
