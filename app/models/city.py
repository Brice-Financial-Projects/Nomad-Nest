"""backend/app/models/city.py"""

from app.extensions import db

class City(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    housing = db.Column(db.Float, nullable=False)
    groceries = db.Column(db.Float, nullable=False)
    transport = db.Column(db.Float, nullable=False)
    healthcare = db.Column(db.Float, nullable=False)
    utilities = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<City {self.name}>"
