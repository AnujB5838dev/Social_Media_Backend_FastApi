"""add content column to posts table

Revision ID: dd2feb32170d
Revises: 06ed8817a340
Create Date: 2025-02-27 11:39:22.340248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd2feb32170d'
down_revision: Union[str, None] = '06ed8817a340'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
