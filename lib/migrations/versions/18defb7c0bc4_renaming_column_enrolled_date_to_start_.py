"""Renaming column enrolled_date to start_date

Revision ID: 18defb7c0bc4
Revises: 791279dd0760
Create Date: 2023-11-10 16:04:56.633949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "18defb7c0bc4"
down_revision = "791279dd0760"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("students", "enrolled_date", new_column_name="start_date")


def downgrade() -> None:
    op.alter_column("students", "start_date", new_column_name="enrolled_date")
