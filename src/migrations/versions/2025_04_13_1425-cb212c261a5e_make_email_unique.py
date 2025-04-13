"""make email unique

Revision ID: cb212c261a5e
Revises: 780451c9d428
Create Date: 2025-04-13 14:25:14.104511

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "cb212c261a5e"
down_revision: Union[str, None] = "780451c9d428"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(None, "users", ["email"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, "users", type_="unique")

