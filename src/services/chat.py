from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infra.db.models.chat import Chat
    from src.infra.db.uow import UnitOfWork

from src.core.exceptions import ChatAlreadyExistsError, ChatNotFoundError


class ChatService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_by_id(self, chat_id: int) -> Chat:
        chat = await self.uow.chats.get_by_id(chat_id)
        if not chat:
            raise ChatNotFoundError("Chat not found")
        return chat

    async def get_by_user_id(self, user_id: int) -> list[Chat]:
        chats = await self.uow.chats.get_by_user_id(user_id)
        if not chats:
            raise ChatNotFoundError("No chats found for the user")
        return chats

    async def get_all(self) -> list[Chat]:
        chats = await self.uow.chats.get_all()
        if not chats:
            raise ChatNotFoundError("No chats found")
        return chats

    async def create(self, chat: Chat) -> Chat:
        existing_chats = await self.uow.chats.get_by_user_id(chat.user_id)
        if existing_chats:
            raise ChatAlreadyExistsError("Chat already exists for the user")
        return await self.uow.chats.create(chat)

    async def delete(self, chat: Chat) -> None:
        await self.uow.chats.delete(chat)
