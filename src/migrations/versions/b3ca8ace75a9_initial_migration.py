"""initial migration

Revision ID: b3ca8ace75a9
Revises: 13f6dd1d5810
Create Date: 2025-04-02 14:21:07.641199

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = 'b3ca8ace75a9'
down_revision: Union[str, None] = '13f6dd1d5810'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('rooms')

