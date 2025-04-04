from flask import request, jsonify, render_template, session
from app import app
from models.usuario import Usuario
import yagmail
import threading
from app import recaptcha
import requests

email = yagmail.SMTP('santo2828@gmail.com','yoqdygtmnxvptnjn',encoding='utf-8')

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        usuarios = Usuario.objects()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500  
       
def enviarCorreo(destinatario, asunto, mensaje):
    email.send(to=destinatario, subject=asunto, contents=mensaje)

#metodos para inicio de secion y registro de usuario
@app.route('/usuarios/login', methods=['POST'])
def login():
    try:
        data = request.get_json(force=True)

        token = data.get("g-recaptcha-response")
        if not token:
            return jsonify({"message": "Captcha no verificado"}), 400

        # Validar el token con Google
        secret = app.config['GOOGLE_RECAPTCHA_SECRET_KEY']
        payload = {'secret': secret, 'response': token}
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
        result = r.json()

        if not result.get("success"):
            return jsonify({"message": "Captcha no verificado"}), 400

        # Login
        userId = data.get("userId")
        passwordIn = data.get("password")

        if not userId or not passwordIn:
            return jsonify({"message": "Faltan datos"}), 400

        usuario = Usuario.objects(userId=userId).first()
        if usuario is None:
            return jsonify({"message": "Usuario no encontrado"}), 404

        if passwordIn != usuario.password:
            return jsonify({"message": "Contraseña incorrecta"}), 401

        # Sesión y correo
        session["userId"] = usuario.userId
        session["correo"] = usuario.correo
        session["autenticado"] = True

        mensaje = f'Hola, has iniciado sesión en la aplicación. {usuario.userId}'
        destinatario = [usuario.correo, "andresan0328@gmail.com"]
        hilo = threading.Thread(target=enviarCorreo, args=(destinatario, 'Inicio de sesión', mensaje))
        hilo.start()

        return jsonify({"message": "Inicio de sesión exitoso"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route('/usuarios/logout', methods=['POST'])
def logout():
    try:
        session.clear()
        return jsonify({"message": "Sesión cerrada"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

@app.route('/loginVista', methods=['GET'])
def loginVista():
    try:
        return render_template('login.html'), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/dash')
def dash():
    return render_template('content.html')