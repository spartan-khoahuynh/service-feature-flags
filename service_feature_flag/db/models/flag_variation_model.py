import uuid as uuid_pkg

from sqlalchemy import JSON, TIMESTAMP, UUID, String, func
from sqlalchemy.orm import Mapped, mapped_column

from service_feature_flag.db.base import Base


class FlagVariationModel(Base):
    """Model for demo purpose."""

    __tablename__ = "flag_variation_model"

    flag_id: Mapped[uuid_pkg.UUID] = mapped_column(
        UUID(as_uuid=True),
        server_default=func.gen_random_uuid(),
        nullable=False,
    )
    key: Mapped[str] = mapped_column(
        String(),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        String(),
        nullable=True,
    )
    value: Mapped[JSON] = mapped_column(
        JSON,
        nullable=False,
    )

    update_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
    )
    create_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
    )
