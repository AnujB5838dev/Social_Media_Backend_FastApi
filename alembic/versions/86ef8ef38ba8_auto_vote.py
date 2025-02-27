"""auto-vote

Revision ID: 86ef8ef38ba8
Revises: 3e971abb6a52
Create Date: 2025-02-27 13:00:56.554931

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86ef8ef38ba8'
down_revision: Union[str, None] = '3e971abb6a52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.create_unique_constraint(None, 'users', ['password'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_table('votes')
    # ### end Alembic commands ###
