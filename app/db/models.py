from sqlalchemy import String, CheckConstraint, func, Text, DATETIME
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from datetime import datetime
import uuid


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = (
        CheckConstraint(
            "status IN ('pending', 'processing', 'completed', 'failed')",
            name="chk_status"
        ),
        {"schema": "main"}
    )
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid()
    )

    url: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default='pending'
    )

    created_at: Mapped[datetime] = mapped_column(
        DATETIME(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DATETIME(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    error_message: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    result_payload: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True
    )

    def __repr__(self):
        return f"<Task(id={self.id}, status={self.status})>"

