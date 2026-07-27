from __future__ import annotations

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.db.base import Base
from src.infra.db.models.mixins import CreatedAtMixin, IdMixin, UpdatedAtMixin


class User(Base, IdMixin, CreatedAtMixin, UpdatedAtMixin):
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=True)
