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
                print(f"\nNombre: {personaje['nombre']}\n"
                      f"Nacimiento: {personaje['Nacimiento']}\n"
                      f"Jinchūriki: {personaje['Jinchūriki']}\n"
                      f"Clan: {personaje['Clan']}\n"
                      f"Aldea: {personaje['Aldea']}")
                print("-"*90)
        except requests.exceptions.RequestException as e:
            print(f"Ocurrió un error al obtener los personajes: {e}")

    def listar_personajes_por_aldea(self, aldea):
        try:
            respuesta = requests.get(self.url)
            respuesta.raise_for_status()
            personajes = respuesta.json()
            personajes_filtrados = [personaje for personaje in personajes if personaje['Aldea'] == aldea]
            
            if personajes_filtrados:
                for personaje in personajes_filtrados:
                    print(f"\nNombre: {personaje['nombre']}\n"
                          f"Nacimiento: {personaje['Nacimiento']}\n"
                          f"Jinchūriki: {personaje['Jinchūriki']}\n"
                          f"Clan: {personaje['Clan']}\n"
                          f"Aldea: {personaje['Aldea']}")
                    print("-"*90)
            else:
                print(f"No se encontraron personajes en la aldea: {aldea}")

        except requests.exceptions.RequestException as e:
            print(f"Ocurrió un error al obtener los personajes: {e}")

if __name__ == "__main__":
    api_url = "https://proyecto-python.onrender.com/api/personajes"
    api = PersonajesAPI(api_url)
    
    # Listar todos los personajes
    api.listar_personajes()

    # Listar personajes por aldea
    aldea = input("Introduce la aldea para filtrar personajes: ")
    api.listar_personajes_por_aldea(aldea)
