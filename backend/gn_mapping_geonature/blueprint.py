from flask import Blueprint, request, current_app
from werkzeug.exceptions import BadRequest
from utils_flask_sqla.response import json_resp
from geonature.utils.env import DB, db
import sqlalchemy as sa
from sqlalchemy.orm import joinedload

# import des fonctions utiles depuis le sous-module d'authentification
from geonature.core.gn_permissions import decorators as permissions
from geonature.core.gn_permissions.tools import _get_user_permissions
from .models import BibTypeOrganism, Organism
from gn_mapping_geonature.schema import OrganismSchema
from marshmallow.exceptions import ValidationError
import geojson
from shapely.geometry import shape
from .admin import *
import json


blueprint = Blueprint(
    "mapping_geonature", __name__
)  # blueprint prefix should be different from existing ones in GeoNature !


# Exemple d'une route simple


@blueprint.route("/organisms/<int:id_organism>", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="MAPPING_GEONATURE", get_scope=False)
def get_organism(id_organism):
    organism = db.session.get(Organism, id_organism)
    if not organism:
        raise BadRequest(f"Organism with id {id_organism} not found !")

    return OrganismSchema(as_geojson=True, only=["+cruved"]).dumps(organism)


@blueprint.route("/organisms", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="MAPPING_GEONATURE", get_scope=False)
def get_organisms():
    organisms = DB.session.scalars(
        sa.select(Organism).options(joinedload(Organism.type_))
    ).all()
    return OrganismSchema(many=True, as_geojson=True, only=["+cruved", "type_"]).dumps(
        organisms
    )


@blueprint.route("/type_organism/<int:id_type>", methods=["GET"])
@permissions.check_cruved_scope("R", module_code="MAPPING_GEONATURE", get_scope=False)
def get_type_organism(id_type):
    type_organism = db.session.get(BibTypeOrganism, id_type)
    if not type_organism:
        raise BadRequest(f"Organism Type with id {id_type} not found !")
    return type_organism.as_dict()


@blueprint.route("/organisms", methods=["POST"])
@permissions.check_cruved_scope("C", module_code="MAPPING_GEONATURE", get_scope=False)
def create_organism():
    data = request.json
    print(data["geometry"])
    geom = geojson.loads(json.dumps(data["geometry"]))
    data["geometry"] = shape(geom).wkt
    try:
        new_organism = Organism(**data)
    except ValidationError as e:
        raise BadRequest(str(e))
    DB.session.add(new_organism)
    DB.session.commit()
    return {}


@blueprint.route("/organisms/<int:id_organism>", methods=["PUT"])
@permissions.check_cruved_scope("U", module_code="MAPPING_GEONATURE", get_scope=False)
def update_organism(id_organism):
    data = request.get_json()
    organism = DB.session.get(Organism, id_organism)
    organism = OrganismSchema().load(request.json, instance=organism)
    db.session.add(organism)
    db.session.commit()
    return OrganismSchema().dumps(organism)


@blueprint.route("/organisms/<int:id_organism>", methods=["DELETE"])
@permissions.check_cruved_scope("D", module_code="MAPPING_GEONATURE", get_scope=False)
def delete_organism(id_organism):
    q = sa.delete(Organism).where(Organism.id_organism == id_organism)
    db.session.execute(q)
    DB.session.commit()
    return {}
