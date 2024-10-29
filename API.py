"""
Autor: Mario Criado Guerrero
Clase: Diseño de interfaces
"""
from flask import Flask, jsonify

ninjapi = Flask(__name__)

#Lista
@ninjapi.route('/api/personajes', methods=['GET'])
def obtener_personajes():
    lista_datos = [
        {"nombre": "Naruto", "Nacimiento": "10 Octubre", "Jinchūriki": "Si", "Clan": "Uzumaki", "Aldea": "Konoha"},
        {"nombre": "Sasuke", "Nacimiento": "23 Julio", "Jinchūriki": "No", "Clan": "Uchiha", "Aldea": "Konoha"},
        {"nombre": "Kakashi", "Nacimiento": "15 Septiembre", "Jinchūriki": "No", "Clan": "Hatake", "Aldea": "Konoha"},
        {"nombre": "A", "Nacimiento": "1 Junio", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Kumogakure"},
        {"nombre": "Darui", "Nacimiento": "6 Enero", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Kumogakure"},
        {"nombre": "Rin", "Nacimiento": "15 Noviembre", "Jinchūriki": "Si", "Clan": "Nohara", "Aldea": "Konoha"},
        {"nombre": "Nagato", "Nacimiento": "19 Septiembre", "Jinchūriki": "No", "Clan": "Uzumaki", "Aldea": "Amegakure"},
        {"nombre": "Gaara", "Nacimiento": "19 Enero", "Jinchūriki": "Si", "Clan": "Kazekage", "Aldea": "Sunagakure"},
        {"nombre": "Chiyo", "Nacimiento": "15 Octubre", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Sunagakure"},
        {"nombre": "Sakura", "Nacimiento": "28 Marzo", "Jinchūriki": "No", "Clan": "Haruno", "Aldea": "Konoha"}]
    return jsonify(lista_datos)

if __name__ == '__main__':
    ninjapi.run(debug=False)
