"""empty message

Revision ID: 513c5211b7e
Revises: None
Create Date: 2015-12-03 19:54:45.811499

"""

# revision identifiers, used by Alembic.
revision = '513c5211b7e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('favorite_colors', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'favorite_colors')
    ### end Alembic commands ###
