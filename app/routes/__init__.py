"""app/routes/__init__.py"""

from flask import Blueprint

# Blueprints will be defined in their own files
main_bp = Blueprint("main", __name__)
compare_bp = Blueprint("compare", __name__)
