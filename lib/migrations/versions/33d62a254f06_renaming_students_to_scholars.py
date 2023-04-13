"""Renaming students to scholars

Revision ID: 33d62a254f06
Revises: 791279dd0760
Create Date: 2023-04-13 12:15:21.995150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33d62a254f06'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    # op.rename_table('scholars', 'students')
    pass
