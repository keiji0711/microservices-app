from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models import db
from routes import RegisterUser, LoginUser, GetUser  # Import your resources

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:password@db/microservices_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # Change this to a secure value

db.init_app(app)
api = Api(app)
jwt = JWTManager(app)

# Register the resources
api.add_resource(RegisterUser, "/register")  # POST
api.add_resource(LoginUser, "/login")  # POST
api.add_resource(GetUser, "/user/<int:user_id>")  # GET

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(host='0.0.0.0', port=5000, debug=True)
