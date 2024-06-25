from flask_admin.contrib.geoa import ModelView
from geonature.core.admin.admin import admin as flask_admin
from .models import Organism
from geonature.utils.env import db
from flask import current_app as app

app.config["MAPBOX_MAP_ID"] = "example.abc123"
app.config["DEFAULT_CENTER_LAT"] = 0.2
app.config["DEFAULT_CENTER_LONG"] = 0.2


class OrganismView(ModelView):
    tile_layer_url = "a.tile.openstreetmap.org/{z}/{x}/{y}.png"
    tile_layer_attribution = "some string or html goes here"


flask_admin.add_view(
    OrganismView(Organism, db.session, name="Organisms", category="Mapping GeoNature")
)
