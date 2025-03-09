from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150), nullable=False)
    prenom = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    etablissement = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)  # ✅ Assurez-vous que cette ligne est présente !
    password_hash = db.Column(db.String(256), nullable=False)

    def __init__(self, nom, prenom, age, etablissement, email, password):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.etablissement = etablissement
        self.email = email 
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
