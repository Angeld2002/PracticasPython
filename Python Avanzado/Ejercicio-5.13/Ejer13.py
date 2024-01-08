import requests

def obtener_personajes_por_especie(especie):
    url = f'https://rickandmortyapi.com/api/character/?species={especie}'
    
    try:
        # Realizar la solicitud GET a la API
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtener el contenido en formato JSON
            data = response.json()

            # Mostrar información sobre los personajes de la especie
            print(f"Personajes de la especie '{especie}':")
            for character in data['results']:
                print(f"- {character['name']}")
        else:
            print(f"Error en la solicitud. Código de estado: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Pedir al usuario la especie deseada
    especie = input("Ingrese la especie para obtener los personajes: ")

    # Llamar a la función para obtener personajes por especie
    obtener_personajes_por_especie(especie)
