"""backend/app/config/settings.py"""

import os
from dotenv import load_dotenv

# Load environment variables from the .env file(s)
load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL'
    )
    DEBUG = os.getenv('FLASK_DEBUG', '0') == '1'  # 1 = Development, 0 = Production
    SESSION_TYPE = os.getenv("SESSION_TYPE", "filesystem")  # Default to filesystem
    SESSION_PERMANENT = False

class DevelopmentConfig(Config):
    """Development-specific configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DEV_DATABASE_URL',
    )
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG_TB_PANELS = [
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
    ]


class TestingConfig(Config):
    """Testing-specific configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'TEST_DATABASE_URL',
    )
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing

class ProductionConfig(Config):
    """Production-specific configuration."""
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
    )
    SESSION_TYPE = "redis"  # Use Redis in production
    SESSION_REDIS = os.getenv("REDIS_URL", "redis://localhost:6379/0")
