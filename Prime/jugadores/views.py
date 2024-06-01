from django.shortcuts import render

# Definimos una lista de jugadores con su nombre, nacionalidad y equipo
jugadores = [
    {"nombre": "Lionel Messi", "nacionalidad": "Argentina", "equipo": "Paris Saint-Germain"},
    {"nombre": "Cristiano Ronaldo", "nacionalidad": "Portugal", "equipo": "Manchester United"},
    {"nombre": "Neymar Jr", "nacionalidad": "Brasil", "equipo": "Paris Saint-Germain"},
    {"nombre": "Kylian Mbappé", "nacionalidad": "Francia", "equipo": "Paris Saint-Germain"}
]

# Función para buscar un jugador por nombre
def buscar_jugador(nombre):
    nombre = nombre.lower()  # Convertimos el nombre ingresado a minúsculas
    for jugador in jugadores:
        if nombre in jugador["nombre"].lower():  # Comprobamos si el nombre está contenido en el nombre del jugador
            return jugador
    return None

# Función para validar la entrada del usuario
def validar_entrada(texto):
    entrada = input(texto)
    while not entrada:
        print("Por favor, ingresa un valor.")
        entrada = input(texto)
    return entrada

# Función principal
def main():
    nombre_jugador = validar_entrada("Ingresa el nombre del jugador de fútbol que deseas buscar: ")

    jugador_encontrado = buscar_jugador(nombre_jugador)

    if jugador_encontrado:
        print("Nombre:", jugador_encontrado["nombre"])
        print("Nacionalidad:", jugador_encontrado["nacionalidad"])
        print("Equipo:", jugador_encontrado["equipo"])
    else:
        print("El jugador no fue encontrado en la lista.")

if __name__ == "__main__":
    main()
