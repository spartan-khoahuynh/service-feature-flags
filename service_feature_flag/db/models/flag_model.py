import uuid as uuid_pkg
from datetime import datetime

from sqlalchemy import UUID, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from service_feature_flag.db.base import Base


class FlagModel(Base):
    """Model for demo purpose."""

    __tablename__ = "flag_model"

    name: Mapped[str] = mapped_column(
        String(),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        String(),
        nullable=True,
    )
    default_on_variation_id: Mapped[uuid_pkg.UUID] = mapped_column(
        UUID(as_uuid=True),
        server_default=func.gen_random_uuid(),
        nullable=False,
    )
    default_off_variation_type: Mapped[str] = mapped_column(
        String(),
        nullable=True,
    )
    update_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    create_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
