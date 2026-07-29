from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.infra.db.models.user import User
    from src.infra.db.uow import UnitOfWork

from src.core.exceptions import UserAlreadyExistsError, UserNotFoundError


class UserService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_by_id(self, user_id: int) -> User:
        user = await self.uow.users.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError(f"User with ID {user_id} not found.")
        return user

    async def get_by_tg_id(self, telegram_id: int) -> User:
        user = await self.uow.users.get_by_tg_id(telegram_id)
        if user is None:
            raise UserNotFoundError(f"User with Telegram ID {telegram_id} not found.")
        return user

    async def create(self, user_tg_id: int, username: str) -> None:
        existing_user = await self.uow.users.get_by_tg_id(user_tg_id)
        if existing_user is not None:
            raise UserAlreadyExistsError(
                f"User with Telegram ID {user_tg_id} already exists."
            )
        await self.uow.users.create(user_tg_id, username)

    async def update_username(self, user_tg_id: int, new_username: str) -> None:
        user = await self.get_by_tg_id(user_tg_id)
        await self.uow.users.update_username(user, new_username)

    async def delete(self, user_id: int) -> None:
        user = await self.get_by_id(user_id)
        await self.uow.users.delete(user)
