"""create_book_reviews_table

Revision ID: 46e00f59d098
Revises: 1d3381a47ab0
Create Date: 2024-06-11 08:33:58.018000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import func

# revision identifiers, used by Alembic.
revision: str = '46e00f59d098'
down_revision: Union[str, None] = '1d3381a47ab0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'book_reviews',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('content', sa.String(100), nullable=False),
        sa.Column('book_id', sa.String(12), sa.ForeignKey('books.id'), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=func.now()),
    )


def downgrade() -> None:
    op.drop_table('book_reviews')
