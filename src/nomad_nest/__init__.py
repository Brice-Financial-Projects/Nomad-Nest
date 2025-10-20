"""nomad_nest/__init__.py"""

import os
from flask import Flask
from nomad_nest.config.settings import Config
from nomad_nest.extensions import db, migrate
from nomad_nest.routes.main import main_bp  # Import the new route
from nomad_nest.routes.compare import compare_bp
from nomad_nest.routes.api import api_bp

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath("nomad_nest/templates"))
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(compare_bp, url_prefix="/compare") 
    app.register_blueprint(api_bp)

    return app


