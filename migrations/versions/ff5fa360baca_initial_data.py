"""initial data

Revision ID: ff5fa360baca
Revises: 
Create Date: 2023-04-15 10:37:52.944275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff5fa360baca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('course_name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('course_id')
    )
    op.create_table('position',
    sa.Column('position_id', sa.Integer(), nullable=False),
    sa.Column('position_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('position_id')
    )
    op.create_table('role',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('role_id')
    )
    op.create_table('employee',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('middle_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('position_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['position_id'], ['position.position_id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.role_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('course_lisenters',
    sa.Column('lisenter_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('is_done', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.course_id'], ),
    sa.ForeignKeyConstraint(['lisenter_id'], ['employee.user_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('course_lisenters')
    op.drop_table('employee')
    op.drop_table('role')
    op.drop_table('position')
    op.drop_table('courses')
    # ### end Alembic commands ###
