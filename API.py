"""
Autor: Mario Criado Guerrero
Clase: Diseño de interfaces
"""
from flask import Flask, jsonify
import os

ninjapi = Flask(__name__)

# Lista
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
        {"nombre": "Sakura", "Nacimiento": "28 Marzo", "Jinchūriki": "No", "Clan": "Haruno", "Aldea": "Konoha"},
        {"nombre": "Itachi", "Nacimiento": "9 Junio", "Jinchūriki": "No", "Clan": "Uchiha", "Aldea": "Konoha"},
        {"nombre": "Shikamaru", "Nacimiento": "22 Septiembre", "Jinchūriki": "No", "Clan": "Nara", "Aldea": "Konoha"},
        {"nombre": "Tsunade", "Nacimiento": "2 Agosto", "Jinchūriki": "No", "Clan": "Senju", "Aldea": "Konoha"},
        {"nombre": "Jiraiya", "Nacimiento": "11 Noviembre", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Konoha"},
        {"nombre": "Killer Bee", "Nacimiento": "15 Mayo", "Jinchūriki": "Si", "Clan": "Desconocido", "Aldea": "Kumogakure"},
        {"nombre": "Orochimaru", "Nacimiento": "27 Octubre", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Konoha"},
        {"nombre": "Madara", "Nacimiento": "24 Diciembre", "Jinchūriki": "Si", "Clan": "Uchiha", "Aldea": "Konoha"},
        {"nombre": "Hinata", "Nacimiento": "27 Diciembre", "Jinchūriki": "No", "Clan": "Hyūga", "Aldea": "Konoha"},
        {"nombre": "Neji", "Nacimiento": "3 Julio", "Jinchūriki": "No", "Clan": "Hyūga", "Aldea": "Konoha"},
        {"nombre": "Obito", "Nacimiento": "10 Febrero", "Jinchūriki": "Si", "Clan": "Uchiha", "Aldea": "Konoha"},
        {"nombre": "Ōnoki", "Nacimiento": "8 Octubre", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Iwagakure"},
        {"nombre": "Mei Terumī", "Nacimiento": "21 Mayo", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Kirigakure"},
        {"nombre": "Pain", "Nacimiento": "23 Septiembre", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Amegakure"},
        {"nombre": "Konan", "Nacimiento": "20 Febrero", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Amegakure"},
        {"nombre": "Kisame Hoshigaki", "Nacimiento": "18 Marzo", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Kirigakure"},
        {"nombre": "Deidara", "Nacimiento": "5 Mayo", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Iwagakure"},
        {"nombre": "Sasori", "Nacimiento": "8 Noviembre", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Sunagakure"},
        {"nombre": "Hidan", "Nacimiento": "2 Abril", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Yugakure"},
        {"nombre": "Kakuzu", "Nacimiento": "15 Agosto", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Takigakure"},
        {"nombre": "Zetsu", "Nacimiento": "Desconocido", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Desconocido"},
        {"nombre": "Tobi", "Nacimiento": "10 Febrero", "Jinchūriki": "Si", "Clan": "Uchiha", "Aldea": "Konoha"},
        {"nombre": "Hashirama", "Nacimiento": "23 Octubre", "Jinchūriki": "No", "Clan": "Senju", "Aldea": "Konoha"},
        {"nombre": "Tobirama", "Nacimiento": "19 Febrero", "Jinchūriki": "No", "Clan": "Senju", "Aldea": "Konoha"},
        {"nombre": "Minato", "Nacimiento": "25 Enero", "Jinchūriki": "Si", "Clan": "Namikaze", "Aldea": "Konoha"},
        {"nombre": "Kaguya Ōtsutsuki", "Nacimiento": "Desconocido", "Jinchūriki": "Si", "Clan": "Ōtsutsuki", "Aldea": "Desconocido"},
        {"nombre": "Kimimaro", "Nacimiento": "15 Junio", "Jinchūriki": "No", "Clan": "Kaguya", "Aldea": "Otogakure"},
        {"nombre": "Temari", "Nacimiento": "23 Agosto", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Sunagakure"},
        {"nombre": "Kankurō", "Nacimiento": "15 Mayo", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Sunagakure"},
        {"nombre": "Yugito Nii", "Nacimiento": "24 Julio", "Jinchūriki": "Si", "Clan": "Desconocido", "Aldea": "Kumogakure"},
        {"nombre": "Han", "Nacimiento": "19 Abril", "Jinchūriki": "Si", "Clan": "Desconocido", "Aldea": "Iwagakure"},
        {"nombre": "Yagura", "Nacimiento": "3 Octubre", "Jinchūriki": "Si", "Clan": "Karatachi", "Aldea": "Kirigakure"},
        {"nombre": "Gengetsu Hōzuki", "Nacimiento": "5 Abril", "Jinchūriki": "No", "Clan": "Hōzuki", "Aldea": "Kirigakure"},
        {"nombre": "Choji Akimichi", "Nacimiento": "1 Mayo", "Jinchūriki": "No", "Clan": "Akimichi", "Aldea": "Konoha"},
        {"nombre": "Ino Yamanaka", "Nacimiento": "23 Septiembre", "Jinchūriki": "No", "Clan": "Yamanaka", "Aldea": "Konoha"},
        {"nombre": "Shino Aburame", "Nacimiento": "23 Enero", "Jinchūriki": "No", "Clan": "Aburame", "Aldea": "Konoha"},
        {"nombre": "Kurenai Yuhi", "Nacimiento": "11 Junio", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Konoha"},
        {"nombre": "Iruka Umino", "Nacimiento": "26 Mayo", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Konoha"},
        {"nombre": "Yamato", "Nacimiento": "10 Agosto", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Konoha"},
        {"nombre": "Might Guy", "Nacimiento": "1 Enero", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Konoha"},
        {"nombre": "Rock Lee", "Nacimiento": "27 Noviembre", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Konoha"},
        {"nombre": "TenTen", "Nacimiento": "9 Marzo", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Konoha"},
        {"nombre": "Kurama", "Nacimiento": "Desconocido", "Jinchūriki": "No", "Clan": "Desconocido", "Aldea": "Desconocido"}
    ]
    return jsonify(lista_datos)

# Ruta principal
@ninjapi.route("/")
def inicio():
    mensaje = "¡Bienvenido a la API de personajes de Naruto!"
    return mensaje

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    ninjapi.run(host="0.0.0.0", port=port)
