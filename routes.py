from flask import Blueprint, request, jsonify
from models import db, User

routes = Blueprint('routes', __name__)

@routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nom = data.get('nom')
    prenom = data.get('prenom')
    age = data.get('age')
    etablissement = data.get('etablissement')
    email = data.get('email')  # ✅ Ajout de l'email
    password = data.get('password')

    if not nom or not prenom or not age or not etablissement or not email or not password:
        return jsonify({'message': 'Tous les champs sont requis'}), 400

    # Vérifier si l'email existe déjà
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email déjà utilisé'}), 400

    new_user = User(nom=nom, prenom=prenom, age=age, etablissement=etablissement, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Inscription réussie'}), 201

@routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')  # ✅ Vérification par email
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email et mot de passe requis'}), 400  # ❌ Erreur 400 si vide

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        return jsonify({'message': 'Connexion réussie'}), 200
    else:
        return jsonify({'message': 'Email ou mot de passe incorrect'}), 401
