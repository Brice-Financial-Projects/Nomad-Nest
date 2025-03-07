"""backend/app/models/city.py"""

from app.extensions import db

from app.extensions import db

class City(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state_province_id = db.Column(db.Integer, db.ForeignKey("states_provinces.id"), nullable=False)
    
    housing = db.Column(db.Float, nullable=False)
    groceries = db.Column(db.Float, nullable=False)
    transport = db.Column(db.Float, nullable=False)
    healthcare = db.Column(db.Float, nullable=False)
    utilities = db.Column(db.Float, nullable=False)


    __table_args__ = (db.UniqueConstraint("name", "state_province_id", name="uq_city"),)
