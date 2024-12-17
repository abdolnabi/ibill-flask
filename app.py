from flask import Flask
from database import db
from config import Config
from routes.items import item_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Register routes
app.register_blueprint(item_bp)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
