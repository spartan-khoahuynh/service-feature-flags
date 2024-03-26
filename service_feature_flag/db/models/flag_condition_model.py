from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import expression

from service_feature_flag.db.base import Base


class FlagConditionModel(Base):
    """Model for demo purpose."""

    __tablename__ = "flag_condition_model"

    cond_key: Mapped[str] = mapped_column(
        String(),
        nullable=False,
    )
    cond_value: Mapped[str] = mapped_column(
        String(),
        nullable=False,
    )
    is_evaluated: Mapped[bool] = mapped_column(
        Boolean,
        server_default=expression.false(),
    )
