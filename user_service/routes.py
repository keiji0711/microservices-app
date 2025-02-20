from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

class RegisterUser(Resource):
    def post(self):
        from models import db, User  # Lazy import inside the function
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return {"message": "User already exists"}, 400

        new_user = User(username=data['username'], password=generate_password_hash(data['password']))
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User registered successfully"}, 201

class LoginUser(Resource):
    def post(self):
        from models import db, User  # Lazy import
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            token = create_access_token(identity=user.id)
            return {"access_token": token}, 200
        return {"message": "Invalid credentials"}, 401

class GetUser(Resource):
    def get(self, user_id):
        from models import db, User  # Lazy import
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return {"id": user.id, "username": user.username}, 200
