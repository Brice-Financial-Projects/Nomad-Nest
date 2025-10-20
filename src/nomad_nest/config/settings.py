"""src/nomad_nest/config/settings.py"""

import os

from dotenv import load_dotenv

# Load environment variables from .env (not .flaskenv)
load_dotenv()


class Config:
    """Base configuration shared across all environments."""

    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///:memory:")
    SESSION_TYPE = os.getenv("SESSION_TYPE", "filesystem")
    SESSION_PERMANENT = False

    # App environment context (used internally, not by Flask CLI)
    FLASK_CONFIG = os.getenv("FLASK_CONFIG", "development").lower()


class DevelopmentConfig(Config):
    """Development-specific configuration."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DEV_DATABASE_URL", Config.SQLALCHEMY_DATABASE_URI
    )
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG_TB_PANELS = [
        "flask_debugtoolbar.panels.headers.HeaderDebugPanel",
        "flask_debugtoolbar.panels.logger.LoggingPanel",
        "flask_debugtoolbar.panels.route_list.RouteListDebugPanel",
        "flask_debugtoolbar.panels.profiler.ProfilerDebugPanel",
    ]


class TestingConfig(Config):
    """Testing-specific configuration."""

    TESTING = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "sqlite:///:memory:")
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """Production-specific configuration."""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", Config.SQLALCHEMY_DATABASE_URI)
    SESSION_TYPE = "redis"
    SESSION_REDIS = os.getenv("REDIS_URL", "redis://localhost:6379/0")
