"""nomad_nest/__init__.py"""

import os

from flask import Flask

from nomad_nest.config.settings import (
    DevelopmentConfig,
    ProductionConfig,
    TestingConfig,
)
from nomad_nest.extensions import db, migrate
from nomad_nest.routes.api import api_bp
from nomad_nest.routes.compare import compare_bp
from nomad_nest.routes.main import main_bp  # Import the new route


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    config_name = os.getenv("FLASK_CONFIG", "development").lower()
    config_mapping = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }

    app.config.from_object(config_mapping.get(config_name, DevelopmentConfig))

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(compare_bp, url_prefix="/compare")
    app.register_blueprint(api_bp)

    return app
