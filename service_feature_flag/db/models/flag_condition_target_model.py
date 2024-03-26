import uuid as uuid_pkg

from sqlalchemy import JSON, UUID, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column

from service_feature_flag.db.base import Base


class FlagConditionTargetModel(Base):
    """Model for demo purpose."""

    __tablename__ = "flag_condition_target_model"

    conditions: Mapped[JSON] = mapped_column(
        JSON,
        nullable=False,
    )
    status: Mapped[bool] = mapped_column(
        Boolean,
        nullable=True,
    )
    variation_id: Mapped[uuid_pkg.UUID] = mapped_column(
        UUID(as_uuid=True),
        server_default=func.gen_random_uuid(),
        nullable=False,
    )
