"""app/routes/api.py"""

from flask import Blueprint, jsonify, request
from app.models.country import Country
from app.models.state_province import StateProvince
from app.models.city import City
from app.extensions import db

api_bp = Blueprint("api", __name__)

# Fetch all countries
@api_bp.route("/api/countries", methods=["GET"])
def get_countries():
    countries = Country.query.order_by(Country.name).all()
    return jsonify([{"id": c.id, "name": c.name} for c in countries])

# Fetch states based on selected country
@api_bp.route("/api/states", methods=["GET"])
def get_states():
    country_id = request.args.get("country_id")
    states = StateProvince.query.filter_by(country_id=country_id).order_by(StateProvince.name).all()
    return jsonify([{"id": s.id, "name": s.name} for s in states])

# Fetch cities based on selected state/province
@api_bp.route("/api/cities", methods=["GET"])
def get_cities():
    state_id = request.args.get("state_id")
    cities = City.query.filter_by(state_province_id=state_id).order_by(City.name).all()
    return jsonify([{"id": c.id, "name": c.name} for c in cities])
