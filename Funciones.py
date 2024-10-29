# -*- coding: utf-8 -*-
"""
Autor: Mario Criado Guerrero
Clase: Diseño de interfaces
"""

import requests

class PersonajesAPI:
    def __init__(self, url):
        self.url = url

    def listar_personajes(self):
        try:
            respuesta = requests.get(self.url)
            respuesta.raise_for_status()
            personajes = respuesta.json()
            for personaje in personajes:
                print(f"Nombre: {personaje['nombre']}, Nacimiento: {personaje['Nacimiento']}, Jinchūriki: {personaje['Jinchūriki']}, Clan: {personaje['Clan']}, Aldea: {personaje['Aldea']}")
        except requests.exceptions.RequestException as e:
            print(f"Ocurrió un error al obtener los personajes: {e}")

if __name__ == "__main__":
    api_url = "http://127.0.0.1:5000/api/personajes"
    api = PersonajesAPI(api_url)
    api.listar_personajes()
