"""add few columns tomposts table

Revision ID: 3e971abb6a52
Revises: 2d26769b46ed
Create Date: 2025-02-27 12:47:22.811581

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e971abb6a52'
down_revision: Union[str, None] = '2d26769b46ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published', sa.Boolean(),nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at',sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts', 'created_at')

    pass
