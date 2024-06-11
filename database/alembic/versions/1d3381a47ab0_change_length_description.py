"""change_length_description

Revision ID: 1d3381a47ab0
Revises: 67876b13ad02
Create Date: 2024-06-11 00:20:21.916765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '1d3381a47ab0'
down_revision: Union[str, None] = '67876b13ad02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('books', 'description',
                    existing_type=sa.String(length=500),
                    type_=sa.String(length=1000),
                    existing_nullable=True)


def downgrade() -> None:
    op.alter_column('books', 'description',
                    existing_type=sa.String(length=1000),
                    type_=sa.String(length=500),
                    existing_nullable=True)
