"""empty message

Revision ID: 6149f7e8ce03
Revises: e6e619658266
Create Date: 2024-06-14 22:17:06.299485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6149f7e8ce03'
down_revision = 'e6e619658266'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('session', schema=None) as batch_op:
        batch_op.add_column(sa.Column('session_type', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('score', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('paperwork_completed', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('paperwork_details', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('session_data_file', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('computed_values', sa.Text(), nullable=True))
        batch_op.alter_column('start_time',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('session', schema=None) as batch_op:
        batch_op.alter_column('start_time',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.drop_column('computed_values')
        batch_op.drop_column('session_data_file')
        batch_op.drop_column('paperwork_details')
        batch_op.drop_column('paperwork_completed')
        batch_op.drop_column('score')
        batch_op.drop_column('session_type')

    # ### end Alembic commands ###
