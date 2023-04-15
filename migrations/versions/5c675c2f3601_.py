"""empty message

Revision ID: 5c675c2f3601
Revises: ff5fa360baca
Create Date: 2023-04-15 10:56:16.595485

"""
from alembic import op
import sqlalchemy as sa
from flask import Flask
from app import db, Role, Position

# revision identifiers, used by Alembic.
revision = '5c675c2f3601'
down_revision = 'ff5fa360baca'
branch_labels = None
depends_on = None


def upgrade():
    admin = Role('admin')
    user = Role('user')
    seo = Position('Начальник')
    work_security = Position('Инженер по охране труда')
    db.session.add_all([admin, user, seo, work_security])
    db.session.commit()



def downgrade():
    Role.query.delete()
    Position.query.delete()
    db.session.commit()
