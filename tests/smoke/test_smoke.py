"""
Basic Smoke Test
----------------
Verifies that the Flask application factory loads successfully
and the app context initializes without error.
"""

from src.nomad_nest.__init__ import create_app


def test_app_factory_loads():
    """Ensure the Flask app can be created successfully."""
    app = create_app()
    assert app is not None, "App factory returned None"

    # Verify we can push an application context without errors
    with app.app_context():
        assert isinstance(app.name, str)
        assert len(app.name) > 0
