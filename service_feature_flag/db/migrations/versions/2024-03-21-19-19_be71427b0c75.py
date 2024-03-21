"""empty message

Revision ID: be71427b0c75
Revises:
Create Date: 2024-03-21 19:19:55.216584

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "be71427b0c75"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "dummy_model",
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_dummy_model_id"), "dummy_model", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_dummy_model_id"), table_name="dummy_model")
    op.drop_table("dummy_model")
    # ### end Alembic commands ###