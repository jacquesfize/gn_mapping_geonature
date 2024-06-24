from flask import Blueprint, request

from utils_flask_sqla.response import json_resp
from geonature.utils.env import DB

# import des fonctions utiles depuis le sous-module d'authentification
from geonature.core.gn_permissions import decorators as permissions
from geonature.core.gn_permissions.tools import _get_user_permissions
from .models import BibTypeOrganism, Organism

blueprint = Blueprint(
    "mapping_geonature", __name__
)  # blueprint prefix should be different from existing ones in GeoNature !


# Exemple d'une route simple


@blueprint.route("/organisms/<int:id_organism>", methods=["GET"])
def get_organism():
    q = DB.session.query(Organism).filter_by(id_organism=id_organism)
    data = q.first()
    return data.as_dict()


@blueprint.route("/organisms", methods=["GET"])
def get_organisms():
    q = DB.session.query(Organism)
    data = q.all()
    return [d.as_dict() for d in data]


@blueprint.route("/type_organism", methods=["GET"])
def get_type_organism():
    q = DB.session.query(BibTypeOrganism)
    data = q.all()
    return [d.as_dict() for d in data]


@blueprint.route("/organism", methods=["POST"])
def create_organism():
    data = request.get_json()
    new_organism = Organism(**data)
    DB.session.add(new_organism)
    DB.session.commit()
    return new_organism


@blueprint.route("/organism/<int:id_organism>", methods=["PUT"])
def update_organism(id_organism):
    data = request.get_json()
    q = DB.session.query(Organism).filter_by(id_organism=id_organism)
    q.update(data)
    DB.session.commit()
    return "OK"


@blueprint.route("/organism/<int:id_organism>", methods=["DELETE"])
def delete_organism(id_organism):
    q = DB.session.query(Organism).filter_by(id_organism=id_organism)
    q.delete()
    DB.session.commit()
    return "OK"
