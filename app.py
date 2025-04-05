from flask import Flask, render_template, session, jsonify, flash
from flask_mongoengine import MongoEngine
from functools import wraps
from dotenv import load_dotenv
from google_recaptcha_flask import ReCaptcha
import os

app = Flask(__name__)

# Configuración de la clave secreta (mejor usa una variable de entorno)
app.secret_key = os.environ.get("SECRET_KEY", "una-clave-secreta-por-defecto")  # ⚠️ Cambia esto en producción

# Conexión a tu MongoDB Atlas (¡usa variables de entorno para el usuario y contraseña!)
uri = "mongodb://gerardo47:12345@cluster0-shard-00-00.rrbne.mongodb.net:27017,cluster0-shard-00-01.rrbne.mongodb.net:27017,cluster0-shard-00-02.rrbne.mongodb.net:27017/?replicaSet=atlas-u4x1au-shard-0&ssl=true&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

app.config['MONGODB_SETTINGS'] = {
    "db": "GestionPeliculas",
    "host": uri,
}

# Configuraciones adicionales
app.config['SESSION_TYPE'] = 'filesystem' 
app.config["UPLOAD_FOLDER"] = "./static/images"
app.config['CORS_HEADERS'] = 'Content-Type'

# Configuración de reCAPTCHA (opcional)
app.config['GOOGLE_RECAPTCHA_ENABLED'] = True
app.config['GOOGLE_RECAPTCHA_SITE_KEY'] = os.environ.get("RECAPTCHA_SITE_KEY", "")
app.config['GOOGLE_RECAPTCHA_SECRET_KEY'] = os.environ.get("RECAPTCHA_SECRET_KEY", "")

recaptcha = ReCaptcha(app=app)
db = MongoEngine(app)

# Verificar conexión
from mongoengine.connection import get_db
db_actual = get_db()
print("📌 Conectado a la base de datos:", db_actual.name)

# Decorador de login (ejemplo)
def login_requerido(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        if "autenticado" not in session or not session["autenticado"]:
            flash("Debes iniciar sesión para acceder a esta página.", "danger")
            return render_template('login.html'), 401
        return f(*args, **kwargs)
    return decorador

# Importar rutas
from routes.peliculasRouter import *
from routes.generoRoutes import *
from routes.usuarioRouter import *

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
    