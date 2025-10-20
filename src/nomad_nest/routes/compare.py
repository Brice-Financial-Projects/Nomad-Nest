"""nomad_nest/routes/compare.py"""

from flask import Blueprint, render_template, request
from nomad_nest.models.city import City
from nomad_nest.extensions import db

compare_bp = Blueprint("compare", __name__)

@compare_bp.route("/compare", methods=["GET", "POST"])
def compare():
    if request.method == "POST":
        city1 = request.form["city1"]
        city2 = request.form["city2"]
        
        city1_data = City.query.filter_by(name=city1).first()
        city2_data = City.query.filter_by(name=city2).first()

        return render_template("compare/result.html", city1=city1_data, city2=city2_data)

    cities = City.query.all()
    return render_template("compare/form.html", cities=cities)
