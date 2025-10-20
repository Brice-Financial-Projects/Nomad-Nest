"""backend/run.py"""

from app import create_app

# Create the nomad_nest instance using the factory function
app = create_app()

if __name__ == '__main__':
    # Run the nomad_nest
    app.run(port=5000)