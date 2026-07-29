from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infra.db.models.message import Message
    from src.infra.db.uow import UnitOfWork

from src.core.exceptions import MessageNotFoundError


class MessageService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_by_id(self, message_id: int) -> Message:
        message = await self.uow.messages.get_by_id(message_id)
        if not message:
            raise MessageNotFoundError("Message not found")
        return message

    async def get_by_chat_id(self, chat_id: int) -> list[Message]:
        messages = await self.uow.messages.get_by_chat_id(chat_id)
        if not messages:
            raise MessageNotFoundError("No messages found for the chat")
        return messages

    async def get_all(self) -> list[Message]:
        messages = await self.uow.messages.get_all()
        if not messages:
            raise MessageNotFoundError("No messages found")
        return messages

    async def create(self, message: Message) -> Message:
        return await self.uow.messages.create(message)

    async def delete(self, message: Message) -> None:
        await self.uow.messages.delete(message)
