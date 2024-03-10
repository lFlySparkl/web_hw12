"""initial

Revision ID: 12ff8dd67c80
Revises: 
Create Date: 2024-03-10 06:28:31.995344

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12ff8dd67c80'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = ('main',)
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
