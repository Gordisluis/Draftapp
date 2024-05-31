from django.shortcuts import render

# Create your views here.
def buscar_equipo_insensible(jugador, jugadores_futbol):
    """
    Busca el equipo en el que juega un jugador de fútbol sin distinguir entre mayúsculas y minúsculas.

    Args:
    jugador (str): El nombre del jugador.
    jugadores_futbol (dict): Diccionario que mapea jugadores a sus equipos.

    Returns:
    str or None: El nombre del equipo si se encuentra el jugador, None si no se encuentra.
    """
    jugador = jugador.lower()  # Convertir el nombre del jugador a minúsculas
    for nombre, equipo in jugadores_futbol.items():
        if nombre.lower() == jugador:  # Convertir el nombre del diccionario a minúsculas para comparar
            return equipo
    return None

# Diccionario ficticio de jugadores de fútbol y sus equipos
jugadores_futbol = {
    'Messi': 'Paris Saint-Germain',
    'Ronaldo': 'Manchester United',
    'Neymar': 'Paris Saint-Germain',
    'Suarez': 'Atletico Madrid',
    'Mbappé': 'Real Madrid',
    'Lewandowski': 'Bayern Munich',
    # Añade más jugadores y equipos según desees
}

def buscar_equipo_insensible(jugador, jugadores_futbol):
    """
    Busca el equipo en el que juega un jugador de fútbol sin distinguir entre mayúsculas y minúsculas.

    Args:
    jugador (str): El nombre del jugador.
    jugadores_futbol (dict): Diccionario que mapea jugadores a sus equipos.

    Returns:
    str or None: El nombre del equipo si se encuentra el jugador, None si no se encuentra.
    """
    jugador = jugador.lower()  # Convertir el nombre del jugador a minúsculas
    for nombre, equipo in jugadores_futbol.items():
        if nombre.lower() == jugador:  # Convertir el nombre del diccionario a minúsculas para comparar
            return equipo
    return None

# Diccionario ficticio de jugadores de fútbol y sus equipos
jugadores_futbol = {
    'Messi': 'Paris Saint-Germain',
    'Ronaldo': 'Manchester United',
    'Neymar': 'Paris Saint-Germain',
    'Suarez': 'Atletico Madrid',
    'Mbappé': 'Real Madrid',
    'Lewandowski': 'Bayern Munich',
    # Añade más jugadores y equipos según desees
}

while True:
    jugador = input("Ingresa el nombre del jugador de fútbol (o 'salir' para terminar): ")
    if jugador.lower() == 'salir':
        print("Saliendo del programa...")
        break
    equipo = buscar_equipo_insensible(jugador, jugadores_futbol)
    if equipo:
        print(f"{jugador.capitalize()} juega en {equipo}.")
    else:
        print(f"No se encontró información sobre {jugador.capitalize()}.")

