from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infra.db.models.chat import Chat
    from src.infra.db.repositories.chat import ChatRepository

from src.core.exceptions import ChatAlreadyExistsError, ChatNotFoundError


class ChatService:
    def __init__(self, chat_repository: ChatRepository):
        self.chat_repo = chat_repository

    async def get_by_id(self, chat_id: int) -> Chat:
        chat = await self.chat_repo.get_by_id(chat_id)
        if not chat:
            raise ChatNotFoundError("Chat not found")
        return chat

    async def get_by_user_id(self, user_id: int) -> list[Chat]:
        chats = await self.chat_repo.get_by_user_id(user_id)
        if not chats:
            raise ChatNotFoundError("No chats found for the user")
        return chats
