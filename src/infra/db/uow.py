from types import TracebackType

from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.db.repositories.chat import ChatRepository
from src.infra.db.repositories.message import MessageRepository
from src.infra.db.repositories.user import UserRepository
from src.infra.db.session import AsyncSessionLocal


class UnitOfWork:
    def __init__(self) -> None:
        self._session: AsyncSession | None = None
        self.users: UserRepository  # initialized in __aenter__
        self.chats: ChatRepository  # initialized in __aenter__
        self.messages: MessageRepository  # initialized in __aenter__

    async def __aenter__(self):
        self._session = AsyncSessionLocal()
        self.users = UserRepository(self._session)
        self.chats = ChatRepository(self._session)
        self.messages = MessageRepository(self._session)
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if exc_type is not None:
            await self.rollback()
        assert self._session is not None
        await self._session.close()

    async def commit(self) -> None:
        assert self._session is not None
        await self._session.commit()

    async def rollback(self) -> None:
        assert self._session is not None
        await self._session.rollback()
