# -*- coding: utf-8 -*-
"""
Autor: Mario Criado Guerrero
Clase: Diseño de interfaces
"""

from Funciones import PersonajesAPI

def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Listar todos los personajes")
    print("2. Listar personajes por aldea")
    print("3. Buscar personaje por nombre")
    print("4. Listar todos los Jinchūrikis")
    print("5. Salir")

def ejecutar_opcion(api):
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == '1':
            api.listar_personajes()
        elif opcion == '2':
            aldea = input("Introduce la aldea para filtrar personajes: ")
            api.listar_personajes_por_aldea(aldea)
        elif opcion == '3':
            nombre = input("Introduce el nombre del personaje para buscar: ")
            api.buscar_personaje_por_nombre(nombre)
        elif opcion == '4':
            print("\nListado de Jinchūrikis:")
            api.listar_jinchurikis()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    api_url = "https://proyecto-python.onrender.com/api/personajes"
    api = PersonajesAPI(api_url)
    ejecutar_opcion(api)
