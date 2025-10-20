"""nomad_nest/models/state_province.py"""

from nomad_nest.extensions import db


class StateProvince(db.Model):
    __tablename__ = "states_provinces"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"), nullable=False)

    cities = db.relationship(
        "City", backref="state_province", cascade="all, delete-orphan"
    )

    __table_args__ = (
        db.UniqueConstraint("name", "country_id", name="uq_state_province"),
    )
