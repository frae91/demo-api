"""Create Customer model

Revision ID: 5622e17a4cfc
Revises: 
Create Date: 2024-09-23 15:34:55.667982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5622e17a4cfc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email_address', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('loyalty_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customers')
    # ### end Alembic commands ###
