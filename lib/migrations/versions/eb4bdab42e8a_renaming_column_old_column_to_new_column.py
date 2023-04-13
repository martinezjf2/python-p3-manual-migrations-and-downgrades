"""renaming column old_column to new_column

Revision ID: eb4bdab42e8a
Revises: 33d62a254f06
Create Date: 2023-04-13 12:27:10.637166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb4bdab42e8a'
down_revision = '33d62a254f06'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars','grade', new_column_name='age')
    pass


def downgrade() -> None:
    pass
