import uuid as uuid_pkg
from datetime import datetime

from sqlalchemy import UUID, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from service_feature_flag.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta

    id: Mapped[uuid_pkg.UUID] = mapped_column(
        UUID(as_uuid=True),
        server_default=func.gen_random_uuid(),
        primary_key=True,
        index=True,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
        nullable=True,
    )
    deleted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
