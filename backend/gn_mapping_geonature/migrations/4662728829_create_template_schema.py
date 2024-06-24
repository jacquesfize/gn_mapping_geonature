"""create_template_schema

Revision ID: 4662728829
Revises: 
Create Date: 2024-06-24

"""

import importlib

from alembic import op, context
import sqlalchemy as sa
from geoalchemy2 import Geometry
from gn_mapping_geonature.models import BibTypeOrganism


# revision identifiers, used by Alembic.
revision = "4662728829"  # CHANGE ME!
down_revision = None
branch_labels = ("mapping_geonature",)
depends_on = None


schema = "gn_mapping_geonature"


def upgrade():

    op.execute(
        f"""
    CREATE SCHEMA IF NOT EXISTS {schema};
    """
    )
    op.create_table(
        "bib_type_organism",
        sa.Column("id_type", sa.Integer, primary_key=True),
        sa.Column("nom_type", sa.String, nullable=False),
        schema=schema,
    )
    op.execute(
        sa.insert(sa.table(BibTypeOrganism)),
        [
            {"id_type": 1, "nom_type": "Parc National"},
            {"id_type": 2, "nom_type": "Parc Régional"},
            {"id_type": 3, "nom_type": "Association"},
            {"id_type": 4, "nom_type": "Autre"},
            {"id_type": 5, "nom_type": "Entreprise privée"},
            {"id_type": 6, "nom_type": "Personne physique"},
            {"id_type": 7, "nom_type": "Journal"},
            {"id_type": 8, "nom_type": "Métropole"},
            {"id_type": 9, "nom_type": "Ferme"},
            {"id_type": 10, "nom_type": "Bureau d'études"},
            {"id_type": 11, "nom_type": "Conservatoire d'Espaces Naturels"},
            {"id_type": 12, "nom_type": "Agence Régional de Biodiversité"},
            {"id_type": 13, "nom_type": "Conservatoire Botanique National"},
            {"id_type": 14, "nom_type": "DREAL"},
            {"id_type": 15, "nom_type": "DRAC"},
            {"id_type": 16, "nom_type": "Syndicat Mixte"},
        ],
    )
    op.create_table(
        "t_organism",
        sa.Column("id_organism", sa.Integer, primary_key=True),
        sa.Column("nom", sa.String, nullable=False),
        sa.Column("adresse", sa.String, nullable=False),
        sa.Column(
            "id_type",
            sa.ForeignKey("gn_mapping_geonature.bib_type_organism.id_type"),
            nullable=False,
        ),
        sa.Column("description", sa.String, nullable=False),
        sa.Column("url", sa.String, nullable=False),
        sa.Column("geometry", Geometry, nullable=False),
        schema=schema,
    )
    op.execute(operations)


def downgrade():
    op.execute(f"DROP TABLE {schema}.bib_type_organism")
    op.execute(f"DROP TABLE {schema}.t_organism")
    op.execute(f"DROP SCHEMA {schema}")
