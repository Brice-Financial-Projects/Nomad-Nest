# Project Structure - Cost of Living Calculator

/backend
│── /app                    # Main application package
│   ├── __init__.py         # Initializes Flask app, SQLAlchemy, and other extensions
│   ├── /config             # Configurations
│   │   ├── __init__.py     # Initialize models
│   │   ├── config.py       # App configuration settings
│   ├── extensions.py       # Centralized extensions (DB, Redis, etc.)
│   ├── /models             # Database models
│   │   ├── __init__.py     # Initialize models
│   │   ├── city.py         # COL database model
│   │   ├── user.py         # User model (for future login enhancement)
│   ├── /routes             # Blueprint routes
│   │   ├── __init__.py     # Registers all blueprints
│   │   ├── main.py         # Landing page routes
│   │   ├── compare.py      # COL comparison routes
│   │   ├── api.py          # API endpoints
│   ├── /templates          # HTML templates folder
│   │   ├── /main           # Templates for main blueprint
│   │   │   ├── index.html  # Landing page template
│   │   ├── /compare        # Templates for comparison blueprint
│   │   │   ├── form.html    # Input form template
│   │   │   ├── result.html  # Comparison results
│   ├── /static             # CSS, JS, Images
│   │   ├── css             # Stylesheets
│   │   ├── js              # JavaScript files
│   │   ├── images          # Static images
│── /data                   # Raw datasets or backups
│── /migrations             # Database migrations folder (Flask-Migrate)
│── .env                    # Environment variables
│── requirements.txt        # Dependencies
│── wsgi.py                 # Entry point for production deployment
│── gunicorn_config.py      # WSGI server config
│── Dockerfile              # Docker setup
