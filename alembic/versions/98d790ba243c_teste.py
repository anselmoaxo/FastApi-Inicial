"""teste

Revision ID: 98d790ba243c
Revises: 63bb913a6bf2
Create Date: 2024-01-26 00:50:48.104953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98d790ba243c'
down_revision: Union[str, None] = '63bb913a6bf2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_automoveis_id', table_name='automoveis')
    op.drop_table('automoveis')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('automoveis',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('marca', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('modelo', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cor', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('preco', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='automoveis_pkey')
    )
    op.create_index('ix_automoveis_id', 'automoveis', ['id'], unique=False)
    # ### end Alembic commands ###