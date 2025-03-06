"""backend/data/seed.py"""

from app import create_app, db
from app.models.city import City

app = create_app()

with app.app_context():
    db.create_all()
    
    cities = [
        City(name="Jacksonville", housing=1200, groceries=500, transport=300, healthcare=400, utilities=150),
        City(name="Mactan Island", housing=400, groceries=250, transport=150, healthcare=200, utilities=100),
        City(name="Cebu", housing=500, groceries=300, transport=170, healthcare=220, utilities=110),
    ]
    
    db.session.bulk_save_objects(cities)
    db.session.commit()

print("Database seeded successfully!")
