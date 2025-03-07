"""app/models/country.py"""

from app.extensions import db

class Country(db.Model):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    
    states_provinces = db.relationship("StateProvince", backref="country", cascade="all, delete-orphan")
