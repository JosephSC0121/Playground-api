"""Add some fields

Revision ID: 75d260778f00
Revises: 2feee45752f4
Create Date: 2024-03-19 16:34:18.416710

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '75d260778f00'
down_revision: Union[str, None] = '2feee45752f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nombres', sa.String(length=50), nullable=True))
    op.add_column('users', sa.Column('apellidos', sa.String(length=50), nullable=True))
    op.add_column('users', sa.Column('aboutme', sa.String(length=255), nullable=True))
    op.drop_column('users', 'email')
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', mysql.VARCHAR(length=70), nullable=True))
    op.add_column('users', sa.Column('email', mysql.VARCHAR(length=50), nullable=True))
    op.drop_column('users', 'aboutme')
    op.drop_column('users', 'apellidos')
    op.drop_column('users', 'nombres')
    # ### end Alembic commands ###
