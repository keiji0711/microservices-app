from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'

db = SQLAlchemy()  # Initialize db first
db.init_app(app)   # Bind db to app

api = Api(app)

# Import models after db is initialized
from models import Order
with app.app_context():
    db.create_all()

# Import routes after app is ready
from routes import CreateOrder, GetOrders

api.add_resource(CreateOrder, "/order")
api.add_resource(GetOrders, "/orders")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
