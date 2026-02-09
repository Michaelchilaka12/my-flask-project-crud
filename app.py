from flask import Flask
from extensions import db, jwt
from routes.auth_routes import auth_routes
from routes.user_routes import user_routes

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"

db.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth_routes, url_prefix="/api/auth")
app.register_blueprint(user_routes, url_prefix="/api")

@app.route("/")
def home():
    return "Flask MVC + JWT + SQLite Running 🚀"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
