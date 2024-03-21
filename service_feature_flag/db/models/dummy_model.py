from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String

from service_feature_flag.db.base import Base


class DummyModel(Base):
    """Model for demo purpose."""

    __tablename__ = "dummy_model"

    name: Mapped[str] = mapped_column(String(length=200))  # noqa: WPS432
