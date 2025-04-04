from flask import Flask, render_template, session, jsonify, flash
from flask_mongoengine import MongoEngine
from functools import wraps
from dotenv import load_dotenv
from google_recaptcha_flask import ReCaptcha
import os

app = Flask(__name__)
key = os.environ.get("SECRET_KEY")
app.secret_key = f"{key}"
# uri1= "mongodb://localhost:27017/GestionPeliculas"
user = os.environ.get("USER_BD")

uri = f"mongodb+srv://{user}:TCe9nPLdWbYxs3OS@cluster-arias.xeprl.mongodb.net/GestionPeliculas?retryWrites=true&w=majority&appName=Cluster-arias"

app.config['SESSION_TYPE'] = 'filesystem' 
app.config["UPLOAD_FOLDER"] = "./static/images"

app.config['MONGODB_SETTINGS'] = [{
    "db": "GestionPeliculas",
    "host": uri,
    #"port": 27017
}]

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['GOOGLE_RECAPTCHA_ENABLED'] =  True
app.config['GOOGLE_RECAPTCHA_SITE_KEY'] = os.environ.get("RECAPTCHA_SITE_KEY")
app.config['GOOGLE_RECAPTCHA_SECRET_KEY'] = os.environ.get("RECAPTCHA_SECRET_KEY")

recaptcha = ReCaptcha(app=app)

db = MongoEngine(app)

from mongoengine.connection import get_db

db_actual = get_db()
print("📌 Conectado a la base de datos:", db_actual.name)

def login_requerido(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        if "autenticado" not in session or not session["autenticado"]:
            flash("Debes iniciar sesión para acceder a esta página.", "danger")
            return render_template('login.html'), 401
        return f(*args, **kwargs)
    return decorador


from routes.peliculasRouter import *
from routes.generoRoutes import *
from routes.usuarioRouter import *
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True) 
    