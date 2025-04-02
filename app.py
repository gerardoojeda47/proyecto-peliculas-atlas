from flask import Flask, render_template
from flask_mongoengine import MongoEngine

app = Flask(__name__)

uri = "mongodb+srv://andresan0328:TCe9nPLdWbYxs3OS@cluster-arias.xeprl.mongodb.net/GestionPeliculas?retryWrites=true&w=majority&appName=Cluster-arias"
app.config["UPLOAD_FOLDER"] = "./static/images"

app.config['MONGODB_SETTINGS'] = [{
    "db": "GestionPeliculas",
    "host": uri,
    #"port": 27017
}]

db = MongoEngine(app)

from mongoengine.connection import get_db

db_actual = get_db()
print("📌 Conectado a la base de datos:", db_actual.name)

@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/dash')
def dash():
    return render_template('content.html')
    
if __name__ == '__main__':
    from routes.peliculasRouter import *
    from routes.generoRoutes import *
    from routes.usuarioRouter import *
    app.run(port=5000, host='0.0.0.0', debug=True) 
    