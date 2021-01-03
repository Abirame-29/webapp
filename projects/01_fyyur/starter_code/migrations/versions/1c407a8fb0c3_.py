"""empty message

Revision ID: 1c407a8fb0c3
Revises: d44c0aa7bbd4
Create Date: 2021-01-03 17:43:04.528519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c407a8fb0c3'
down_revision = 'd44c0aa7bbd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'available_timings')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('available_timings', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
