"""src/nomad_nest/models/city.py"""

from nomad_nest.extensions import db


class City(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state_province_id = db.Column(
        db.Integer, db.ForeignKey("states_provinces.id"), nullable=False
    )
    is_cached = db.Column(
        db.Boolean, default=False
    )  # Track if the city is stored locally

    housing = db.Column(db.Float, nullable=True)
    groceries = db.Column(db.Float, nullable=True)
    transport = db.Column(db.Float, nullable=True)
    healthcare = db.Column(db.Float, nullable=True)
    utilities = db.Column(db.Float, nullable=True)

    __table_args__ = (db.UniqueConstraint("name", "state_province_id", name="uq_city"),)
