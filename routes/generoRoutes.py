from flask import request, jsonify, render_template
from app import app
from models.genero import Genero
from mongoengine import get_connection

@app.route('/generos', methods=['GET'])
def get_generos():
    try:
        generos = Genero.objects()        
        return jsonify(generos), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
    
@app.route('/generos/', methods=['POST'])
def agregarGenero():
    try:
        data = request.get_json(force=True)
        genero = Genero(**data)
        genero.save()
        print(genero)
        return jsonify("✅ Documento guardado:",genero), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route('/generos/<id>', methods=['PUT'])
def actualizarGenero(id):
    try:
        data = request.get_json(force=True)
        genero = Genero.objects(id=id).first()
        if genero is None:
            return jsonify({"message": "Genero no encontrado"}), 404
        else:
            generoNuevo = genero.update(**data)
            return jsonify(genero), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route('/generos/<id>', methods=['DELETE'])
def eliminarGenero(id):
    try:
        genero = Genero.objects(id=id).first()
        if genero is None:
            return jsonify({"message": "Genero no encontrado"}), 404
        else:
            genero.delete()
            return jsonify({"message": "Genero eliminado"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
#vistas

@app.route('/generosVista', methods=['GET'])
def get_generos_vista():
    try:
        generos = Genero.objects()
        print("genero encontrad" , generos)
        return render_template('listarGeneros.html', generos=generos), 200
    except Exception as e:
        return render_template('error.html', error=str(e)), 500