import requests
from PIL import Image
import json

pokemon = input("Ingresa el nombre de un pokemon: ")

def filtrar_datos(datos, caracteristica):
    datos_filtrados = []
    for dato in datos:
    	datos_filtrados.append(dato[caracteristica]["name"])
    return datos_filtrados


respuesta_del_servidor = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
if not respuesta_del_servidor:
    print("No existe el pokemon indicado")
    exit()

datos = respuesta_del_servidor.json()

tamano = datos["height"]
peso = datos["weight"]
movimientos = datos["moves"]
habilidades = datos["abilities"]
tipos = datos["types"]
imagen = datos["sprites"]

tipos_filtrados = filtrar_datos(tipos, "type")
habilidades_filtradas = filtrar_datos(habilidades, "ability")
movimientos_filtrados = filtrar_datos(movimientos, "move")

imagen_frontal_url = imagen["front_default"]
imagen = requests.get(imagen_frontal_url, stream=True)
imagen_bytes = imagen.raw

imagen = Image.open(imagen_bytes)
imagen.show()

datos_a_guardar = {
    "tamano": tamano,
    "peso": peso,
    "movimientos": movimientos_filtrados,
    "habilidades": habilidades_filtradas,
    "tipos": tipos_filtrados,
    "imagen": imagen_frontal_url
}

f = open(rf"C:\Users\Gaby\Desktop\Curso Pyhton Rox\MODULO 4\{pokemon}.json", "w")
json.dump(datos_a_guardar, f, indent=6)
f.close()

print(f"""
tamano = {tamano}
peso = {peso}
movimientos = {movimientos_filtrados}
habilidades = {habilidades_filtradas}
tipos = {tipos_filtrados}
""")
