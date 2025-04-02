from flask import request, jsonify, render_template, session
from app import app
from models.usuario import Usuario

app.secret_key = "clave_super_secreta"
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        usuarios = Usuario.objects()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
#metodos para inicio de secion y registro de usuario
@app.route('/usuarios/login', methods=['POST'])
def login():
    try:
        data = request.get_json(force=True)
        print(data)
        
        userId = data.get("userId")
        passwordIn = data.get("password")   
        if not userId or not passwordIn:
            return jsonify({"message": "Faltan datos"}), 400
          
        usuario = Usuario.objects(userId=userId).first()
        
        if usuario is None:
            return jsonify({"message": "Usuario no encontrado"}), 404
        
        print("Usuario encontrado en BD:", usuario.to_json())  # Depuración
        #obtener el password de la base de datos
        password = usuario.password
        print("Contraseña en BD:", password)
        if passwordIn != password:
            return jsonify({"message": "Contraseña incorrecta"}), 401
        
        session["userId"] = usuario.userId  
        session["correo"] = usuario.correo  
        session["password"] = usuario.password  
        session["autenticado"] = True  

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
    

