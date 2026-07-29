from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.db.models.chat import Chat


class ChatRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_chat(self, chat: Chat) -> Chat:
        self.session.add(chat)
        await self.session.commit()
        await self.session.refresh(chat)
        return chat

    async def get_by_id(self, chat_id: int) -> Chat | None:
        result = await self.session.execute(select(Chat).where(Chat.id == chat_id))
        return result.scalar_one_or_none()

    async def get_by_user_id(self, user_id: int) -> list[Chat]:
        result = await self.session.execute(select(Chat).where(Chat.user_id == user_id))
        return list(result.scalars().all())

    async def get_all(self) -> list[Chat]:
        result = await self.session.execute(select(Chat))
        return list(result.scalars().all())

    async def delete(self, chat: Chat) -> None:
        await self.session.delete(chat)
        await self.session.commit()
