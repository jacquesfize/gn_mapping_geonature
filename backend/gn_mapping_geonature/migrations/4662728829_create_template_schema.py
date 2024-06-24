"""create_template_schema

Revision ID: 4662728829
Revises: 
Create Date: 2024-06-24

"""
import importlib

from alembic import op, context
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4662728829"  # CHANGE ME!
down_revision = None
branch_labels = ("mapping_geonature",)
depends_on = None


schema = "gn_mapping_geonature"


def upgrade():
    operations = importlib.resources.read_text(
        "gn_mapping_geonature.migrations.data", "schema.sql"
    )
    op.execute(operations)


def downgrade():
    op.execute(f"DROP TABLE {schema}.my_table")
    op.execute(f"DROP SCHEMA {schema}")
