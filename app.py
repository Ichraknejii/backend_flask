from flask import Flask
from flask_cors import CORS
from config import Config
from models import db, bcrypt
from routes import routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
CORS(app)  

app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
