from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.db.base import Base
from src.infra.db.models.mixins import (
    CreatedAtMixin,
    IdMixin,
    UpdatedAtMixin,
)

if TYPE_CHECKING:
    from src.infra.db.models.message import Message
    from src.infra.db.models.user import User


class Chat(Base, IdMixin, CreatedAtMixin, UpdatedAtMixin):
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    user: Mapped[User] = relationship(
        back_populates="chats",
    )

    messages: Mapped[list[Message]] = relationship(
        back_populates="chat",
        cascade="all, delete-orphan",
        order_by="Message.created_at",
    )
