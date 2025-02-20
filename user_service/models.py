from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Do not bind to app here

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Increased length
