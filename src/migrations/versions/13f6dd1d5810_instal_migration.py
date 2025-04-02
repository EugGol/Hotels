"""instal migration

Revision ID: 13f6dd1d5810
Revises: 
Create Date: 2025-04-02 13:28:02.013705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '13f6dd1d5810'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('hotels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('hotels')
