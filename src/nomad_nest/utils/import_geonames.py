"""nomad_nest/utils/import_geonames.py"""

import csv

from app import create_app
from app.extensions import db
from app.models.country import Country
from app.models.state_province import StateProvince

app = create_app()


def load_countries():
    with open("../data/countryInfo.txt", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="|")
        for row in reader:
            if row[0].startswith("#") or len(row) < 5:
                continue  # Skip comments and invalid rows
            country = Country(name=row[4])  # Column 5 = Country Name
            db.session.add(country)
    db.session.commit()
    print("✅ Countries imported successfully!")


def load_states():
    with open("../data/admin1CodesASCII.txt", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            country_code, state_name = row[0].split(".")  # "US.AL" -> "US", "AL"
            country = Country.query.filter_by(name=country_code).first()
            if country:
                state = StateProvince(name=row[1], country_id=country.id)
                db.session.add(state)
    db.session.commit()
    print("✅ States/Provinces imported successfully!")


with app.app_context():
    load_countries()
    load_states()
    print("✅ Database populated with countries & states!")
