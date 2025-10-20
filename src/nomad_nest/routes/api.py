"""nomad_nest/routes/api.py"""

import requests
from flask import Blueprint, jsonify, request

from nomad_nest.extensions import db
from nomad_nest.models.city import City
from nomad_nest.models.state_province import StateProvince

api_bp = Blueprint("api", __name__)

# OpenStreetMap API URL
OSM_API_URL = "https://nominatim.openstreetmap.org/search"


# Fetch cities dynamically
@api_bp.route("/api/cities", methods=["GET"])
def get_cities():
    state_id = request.args.get("state_id")

    # Check if cities are already cached
    cached_cities = City.query.filter_by(
        state_province_id=state_id, is_cached=True
    ).all()
    if cached_cities:
        return jsonify([{"id": c.id, "name": c.name} for c in cached_cities])

    # If not cached, fetch from OpenStreetMap API
    state = StateProvince.query.get(state_id)
    if not state:
        return jsonify({"error": "Invalid state_id"}), 400

    params = {"state": state.name, "country": state.country.name, "format": "json"}
    headers = {"User-Agent": "COL-Calculator"}
    response = requests.get(OSM_API_URL, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        cities = []
        for item in data:
            city_name = item.get("display_name").split(",")[0]
            city = City(name=city_name, state_province_id=state.id, is_cached=True)
            db.session.add(city)
            db.session.commit()
            cities.append({"id": city.id, "name": city.name})

        return jsonify(cities)
    else:
        return jsonify({"error": "Failed to fetch cities"}), 500
