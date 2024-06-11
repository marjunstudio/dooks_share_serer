"""change_column_subtitle_to_description

Revision ID: 67876b13ad02
Revises: 318b410b6e9f
Create Date: 2024-06-10 23:19:14.695493

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '67876b13ad02'
down_revision: Union[str, None] = '318b410b6e9f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('books', sa.Column('description', sa.String(length=500), nullable=True))
    op.drop_column('books', 'subtitle')


def downgrade() -> None:
    op.add_column('books', sa.Column('subtitle', sa.String(length=100), nullable=True))
    op.drop_column('books', 'description')
