"""add users

Revision ID: 780451c9d428
Revises: 4aaa31639e79
Create Date: 2025-04-11 18:20:45.672808

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "780451c9d428"
down_revision: Union[str, None] = "4aaa31639e79"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("hashed_password", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

def downgrade() -> None:
    op.drop_table("users")
