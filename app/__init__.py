"""app/__init__.py"""

import os
from flask import Flask
from app.config.settings import Config
from app.extensions import db, migrate
from app.routes.main import main_bp  # Import the new route
from app.routes.compare import compare_bp
from app.routes.api import api_bp

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath("app/templates"))
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(compare_bp, url_prefix="/compare") 
    app.register_blueprint(api_bp)

    return app


