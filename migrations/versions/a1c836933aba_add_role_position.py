"""add Role, Position

Revision ID: a1c836933aba
Revises: e6cff8ce3570
Create Date: 2023-04-16 13:19:39.236631

"""
from alembic import op
import sqlalchemy as sa
from app import db, Role, Position, Courses


# revision identifiers, used by Alembic.
revision = 'a1c836933aba'
down_revision = 'e6cff8ce3570'
branch_labels = None
depends_on = None


def upgrade():
    admin = Role('admin')
    user = Role('user')
    seo = Position('Начальник')
    work_security = Position('Инженер по охране труда')
    course1 = Courses('Электробезопасность')
    course2= Courses('Пожарная безопасность')
    db.session.add_all([admin, user, seo, work_security, course1, course2])
    db.session.commit()



def downgrade():
    Role.query.delete()
    Position.query.delete()
    Courses.query.delete()
    db.session.commit()
