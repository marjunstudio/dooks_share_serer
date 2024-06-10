"""change_published_date_to_date

Revision ID: 318b410b6e9f
Revises: 8a6d7552f632
Create Date: 2024-06-10 19:40:39.179382

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '318b410b6e9f'
down_revision: Union[str, None] = '8a6d7552f632'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('books', 'published_date',
        existing_type=sa.DateTime(),
        type_=sa.Date(),
        existing_nullable=True)


def downgrade() -> None:
    op.alter_column('books', 'published_date',
        existing_type=sa.Date(),
        type_=sa.DateTime(),
        existing_nullable=True)
