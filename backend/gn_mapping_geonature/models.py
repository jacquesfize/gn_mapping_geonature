from flask import current_app
from sqlalchemy import ForeignKey

# import utiles pour déclarer les classes SQLAlchemy
from sqlalchemy.sql import select, func, and_
from sqlalchemy.dialects.postgresql import UUID

from geoalchemy2 import Geometry

# méthode de sérialisation
from utils_flask_sqla.serializers import serializable
from utils_flask_sqla_geo.serializers import geoserializable

# instance de la BDD
from geonature.utils.env import DB


class BibTypeOrganism(DB.Model):
    __tablename__ = "bib_type_organism"
    __table_args__ = {"schema": "gn_mapping_geonature"}
    id_type = DB.Column(DB.Integer, primary_key=True)
    nom_type = DB.Column(DB.String, nullable=False)


@serializable
@geoserializable
class Organism(DB.Model):
    __tablename__ = "t_organism"
    __table_args__ = {"schema": "gn_mapping_geonature"}
    id_organism = (DB.Column(sa.Integer, primary_key=True),)
    nom = (db.Column(sa.String, nullable=False),)
    adresse = (db.Column(sa.String, nullable=False),)
    id_type = (
        DB.Column(
            sa.Integer,
            sa.ForeignKey("gn_mapping_geonature.bib_type_organism.id_type"),
            nullable=False,
        ),
    )
    description = db.Column(sa.String, nullable=False)
    url = db.Column(sa.String, nullable=False)
    geometry = db.Column(Geometry, nullable=False)
