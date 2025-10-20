# Project Structure - Nomad Nest (Cost of Living Calculator)

Nomad-Nest/
│
├── src/                                 # Source code (application lives here)
│   └── nomad_nest/                      # Main Flask application package
│       ├── __init__.py                  # App factory: creates and configures the Flask app
│       ├── extensions.py                # Centralized extensions (DB, Redis, JWT, etc.)
│       │
│       ├── config/                      # Configuration management
│       │   ├── __init__.py
│       │   ├── settings.py              # Environment-based config (Dev, Prod, Test)
│       │
│       ├── models/                      # SQLAlchemy ORM models
│       │   ├── __init__.py
│       │   ├── country.py               # Country model
│       │   ├── state.py                 # State/Province model
│       │   ├── city.py                  # City model
│       │   ├── user.py                  # User model (for authentication)
│       │
│       ├── routes/                      # Flask Blueprints for modular routes
│       │   ├── __init__.py
│       │   ├── main.py                  # Landing page routes
│       │   ├── compare.py               # COL comparison routes
│       │   ├── api.py                   # REST API endpoints
│       │   ├── auth.py                  # Authentication routes
│       │
│       ├── templates/                   # Jinja2 templates for rendering pages
│       │   ├── main/                    # Templates for main blueprint
│       │   │   ├── index.html
│       │   ├── compare/                 # Templates for COL comparison
│       │   │   ├── form.html
│       │   │   ├── result.html
│       │   ├── auth/                    # Templates for login/register
│       │       ├── login.html
│       │       ├── register.html
│       │
│       ├── static/                      # Static assets (CSS, JS, images)
│       │   ├── css/
│       │   ├── js/
│       │   ├── images/
│       │
│       ├── utils/                       # Helper modules and business logic
│       │   ├── __init__.py
│       │   ├── data_loader.py           # Load/parse COL datasets
│       │   ├── validators.py            # Input validation
│       │   ├── converters.py            # Currency and unit conversions
│       │
│       ├── tests/                       # Unit and integration tests
│       │   ├── __init__.py
│       │   ├── test_models.py
│       │   ├── test_routes.py
│       │   ├── test_api.py
│       │
│       └── __main__.py                  # Optional: run with `python -m app`
│
├── data/                                # Static datasets and CSVs for COL indices
│   ├── countryInfo.txt
│   ├── admin1CodesASCII.txt
│   ├── sample_city_costs.csv
│
├── migrations/                          # Alembic/Flask-Migrate database migrations
│
├── .env                                 # Environment variables (Flask, DB, Redis, etc.)
├── .gitignore                           # Git ignore rules
├── Dockerfile                           # Docker build instructions
├── gunicorn_config.py                   # Gunicorn WSGI configuration
├── pyproject.toml                       # Project build and dependency configuration
├── README.md                            # Project overview and setup instructions
├── structure.md                         # Documentation of folder layout
└── wsgi.py                              # Entry point for production deployment
