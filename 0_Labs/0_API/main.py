import requests
def trivia_fetch(num):
    url= f"http://pokeapi.co/api/v2/pokemon/{num}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data

def main():
    print("--- Bienvenidos al Pokedex de 'abilities' con API ---")
    print("Responderás 3 rondas.")
    puntuacion = 0
    for ronda in range(1, 4):
        print(f"Ronda {ronda}")
        numero_usuario = input("Ingresa número: ")
        trivia = trivia_fetch(numero_usuario)
        print("Dato curioso sobre tu número: ")
        print(trivia["abilities"])
#        print(trivia["moves"])
#        print(trivia["sprites"])
        print("-----------------------")

if __name__ == "__main__":
    main()