"""empty message

Revision ID: 5df23ec29228
Revises: d7cf3b75e0c3
Create Date: 2023-04-18 09:22:35.903256

"""
from alembic import op
import sqlalchemy as sa
from app import db, Position, Role, Courses


# revision identifiers, used by Alembic.
revision = '5df23ec29228'
down_revision = 'd7cf3b75e0c3'
branch_labels = None
depends_on = None


def upgrade():
    admin = Role('admin')
    user = Role ('user')
    a1 = Position('Начальник')
    a2 = Position('Зам. начальника')
    a3 = Position('Преподаватель')
    a4 = Position('Инж. по охр. труда')
    a5 = Position('Начальник Детского Технопарка')
    a6 = Position('Начальник Дворца Творчества')
    a7 = Position('Гл. инженер')
    a8 = Position('Сотрудник тех. блока')
    a9 = Position('Методист')
    a10 = Position('Начальник отдела кадров')
    a11 = Position('Библиотекарь')
    c1= Courses('Пожарная безопасность')
    c2 =Courses('Электротехника')
    c3 =Courses('Охрана труда')
    db.session.add_all([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,c1,c2,c3,admin,user])
    db.session.commit()
    


def downgrade():
    Position.query.delete()
    Role.query.delete()

    db.session.commit()
