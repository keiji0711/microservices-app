import requests
from flask import request
from flask_restful import Resource

USER_SERVICE_URL = "http://user_service:5000/user"

class CreateOrder(Resource):
    def post(self):
        from models import db, Order  # Lazy import
        data = request.get_json()
        user_id = data['user_id']
        response = requests.get(f"{USER_SERVICE_URL}/{user_id}")

        if response.status_code != 200:
            return {"message": "User not found"}, 404

        new_order = Order(user_id=user_id, product_name=data['product_name'], quantity=data['quantity'])
        db.session.add(new_order)
        db.session.commit()
        return {"message": "Order created successfully"}, 201

class GetOrders(Resource):
    def get(self):
        from models import db, Order  # Lazy import
        orders = Order.query.all()
        return [{"id": o.id, "user_id": o.user_id, "product": o.product_name, "quantity": o.quantity} for o in orders], 200
