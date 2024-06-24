from marshmallow import fields, validates_schema, EXCLUDE
from utils_flask_sqla_geo.schema import GeoAlchemyAutoSchema, GeoModelConverter
from gn_mapping_geonature.models import Organism
from geonature.utils.env import db
from pypnnomenclature.utils import NomenclaturesConverter
from geonature.utils.schema import CruvedSchemaMixin
from utils_flask_sqla.schema import SmartRelationshipsMixin


class OrganismConverter(NomenclaturesConverter, GeoModelConverter):
    pass


class OrganismSchema(CruvedSchemaMixin, SmartRelationshipsMixin, GeoAlchemyAutoSchema):
    class Meta:
        model = Organism
        include_fk = True
        load_instance = True
        sqla_session = db.session
        feature_id = "id_organism"
        model_converter = OrganismConverter

    __module_code__ = "MAPPING_GEONATURE"
