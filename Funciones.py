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
                print(f"Nombre: {personaje['nombre']}, "
                      f"Nacimiento: {personaje['Nacimiento']}, "
                      f"Jinchūriki: {personaje['Jinchūriki']}, "
                      f"Clan: {personaje['Clan']}, "
                      f"Aldea: {personaje['Aldea']}")
                print("-"*40)
        except requests.exceptions.RequestException as e:
            print(f"Ocurrió un error al obtener los personajes: {e}")

if __name__ == "__main__":
    api_url = "https://proyecto-python.onrender.com/api/personajes"
    api = PersonajesAPI(api_url)
    api.listar_personajes()
