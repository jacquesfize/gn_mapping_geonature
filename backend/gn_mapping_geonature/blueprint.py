from flask import Blueprint, request
from werkzeug.exceptions import BadRequest
from utils_flask_sqla.response import json_resp
from geonature.utils.env import DB, db
import sqlalchemy as sa

# import des fonctions utiles depuis le sous-module d'authentification
from geonature.core.gn_permissions import decorators as permissions
from geonature.core.gn_permissions.tools import _get_user_permissions
from .models import BibTypeOrganism, Organism
from gn_mapping_geonature.schema import OrganismSchema
from marshmallow.exceptions import ValidationError

blueprint = Blueprint(
    "mapping_geonature", __name__
)  # blueprint prefix should be different from existing ones in GeoNature !


# Exemple d'une route simple


@blueprint.route("/organisms/<int:id_organism>", methods=["GET"])
def get_organism(id_organism):
    organism = db.session.get(Organism, id_organism)
    if not organism:
        raise BadRequest(f"Organism with id {id_organism} not found !")

    return OrganismSchema(as_geojson=True).dumps(organism)


@blueprint.route("/organisms", methods=["GET"])
def get_organisms():
    organisms = DB.session.scalars(sa.select(Organism)).all()
    return OrganismSchema(many=True, as_geojson=True).dumps(organisms)


@blueprint.route("/type_organism/<int:id_type>", methods=["GET"])
def get_type_organism(id_type):
    type_organism = db.session.get(BibTypeOrganism, id_type)
    if not type_organism:
        raise BadRequest(f"Organism Type with id {id_type} not found !")
    return type_organism.as_dict()


@blueprint.route("/organisms", methods=["POST"])
def create_organism():
    data = request.get_json()
    try:
        new_organism = OrganismSchema().load(**data)
    except ValidationError as e:
        raise BadRequest(str(e))
    DB.session.add(new_organism)
    DB.session.commit()
    return "OK"


@blueprint.route("/organisms/<int:id_organism>", methods=["PUT"])
def update_organism(id_organism):
    data = request.get_json()
    organism = DB.session.get(Organism, id_organism)
    organism.update(data)
    DB.session.commit()
    return "OK"


@blueprint.route("/organisms/<int:id_organism>", methods=["DELETE"])
def delete_organism(id_organism):
    q = sa.delete(Organism).where(Organism.id_organism == id_organism)
    db.session.execute(q)
    DB.session.commit()
    return "OK"
