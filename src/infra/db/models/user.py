from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.db.base import Base
from src.infra.db.models.mixins import (
    CreatedAtMixin,
    IdMixin,
    UpdatedAtMixin,
)

if TYPE_CHECKING:
    from src.infra.db.models.chat import Chat


class User(Base, IdMixin, CreatedAtMixin, UpdatedAtMixin):
    telegram_id: Mapped[int] = mapped_column(
        unique=True,
        nullable=False,
        index=True,
    )

    username: Mapped[str | None] = mapped_column(
        nullable=True,
    )

    active: Mapped[bool] = mapped_column(
        nullable=False,
        default=True,
    )

    chats: Mapped[list[Chat]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )
