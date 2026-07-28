from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from pgvector.sqlalchemy import Vector
from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.db.base import Base
from src.infra.db.models.mixins import (
    CreatedAtMixin,
    IdMixin,
)

if TYPE_CHECKING:
    from src.infra.db.models.chat import Chat


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"


class Message(Base, IdMixin, CreatedAtMixin):
    chat_id: Mapped[int] = mapped_column(
        ForeignKey("chats.id"),
        nullable=False,
        index=True,
    )

    role: Mapped[MessageRole] = mapped_column(
        SAEnum(MessageRole),
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    embedding: Mapped[list[float]] = mapped_column(
        Vector(1536),
        nullable=False,
    )

    chat: Mapped[Chat] = relationship(
        back_populates="messages",
    )
