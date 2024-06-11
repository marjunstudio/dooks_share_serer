"""create_books_table

Revision ID: 8a6d7552f632
Revises: 
Create Date: 2024-06-10 18:21:26.472224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import func


# revision identifiers, used by Alembic.
revision: str = '8a6d7552f632'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "books",
        sa.Column("id", sa.String(length=12), nullable=False),
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("subtitle", sa.String(length=100), nullable=True),
        sa.Column("published_date", sa.DateTime(), nullable=True),
        sa.Column("page_count", sa.Integer(), nullable=True),
        sa.Column("thumbnail", sa.String(length=200), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=func.now()),
        sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=func.now()),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("books")
