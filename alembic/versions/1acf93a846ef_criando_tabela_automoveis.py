"""criando tabela automoveis

Revision ID: 1acf93a846ef
Revises: 3c3b4bb9c7a2
Create Date: 2024-01-26 00:31:32.082045

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1acf93a846ef'
down_revision: Union[str, None] = '3c3b4bb9c7a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
