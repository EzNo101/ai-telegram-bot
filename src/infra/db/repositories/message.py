from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.db.models.message import Message


class MessageRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, message: Message) -> Message:
        self.session.add(message)
        await self.session.flush()
        await self.session.refresh(message)
        return message

    async def get_by_id(self, message_id: int) -> Message | None:
        result = await self.session.execute(
            select(Message).where(Message.id == message_id)
        )
        return result.scalar_one_or_none()

    async def get_by_chat_id(self, chat_id: int) -> list[Message]:
        result = await self.session.execute(
            select(Message).where(Message.chat_id == chat_id)
        )
        return list(result.scalars().all())

    async def get_all(self) -> list[Message]:
        result = await self.session.execute(select(Message))
        return list(result.scalars().all())

    async def delete(self, message: Message) -> None:
        await self.session.delete(message)
