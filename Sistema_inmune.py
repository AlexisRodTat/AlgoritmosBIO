import random

# Parámetros del algoritmo
TAMANO_POBLACION = 10       # Tamaño de la población de anticuerpos
GENERACIONES = 20           # Número de generaciones
TAMANO_ANTICUERPO = 5       # Tamaño de cada anticuerpo (cromosoma)
PROB_MUTACION = 0.2         # Probabilidad de mutación
NUMERO_CLONES = 5           # Número de clones por anticuerpo

# Función de aptitud: suma de los valores del anticuerpo
def calcular_aptitud(anticuerpo):
    return sum(anticuerpo)

# Generación inicial de una población de anticuerpos
def crear_poblacion():
    return [[random.randint(0, 1) for _ in range(TAMANO_ANTICUERPO)] for _ in range(TAMANO_POBLACION)]

# Selección de anticuerpos por aptitud: se quedan los mejores
def seleccionar_mejores(poblacion):
    # Ordenamos la población en orden descendente de aptitud
    return sorted(poblacion, key=calcular_aptitud, reverse=True)[:TAMANO_POBLACION // 2]

# Clonación: Genera clones de los mejores anticuerpos
def clonar(anticuerpo):
    clones = [anticuerpo[:] for _ in range(NUMERO_CLONES)]
    return clones

# Mutación: Cambia aleatoriamente los bits de los clones
def mutar(clones):
    for clon in clones:
        for i in range(len(clon)):
            if random.random() < PROB_MUTACION:
                clon[i] = 1 - clon[i]  # Cambia 0 a 1 o 1 a 0
    return clones

# Algoritmo de sistema inmune artificial
def sistema_inmune_artificial():
    # Inicializamos la población
    poblacion = crear_poblacion()

    for generacion in range(GENERACIONES):
        # Evaluamos la aptitud de cada anticuerpo y seleccionamos los mejores
        mejores_anticuerpos = seleccionar_mejores(poblacion)

        # Clonamos y mutamos los mejores anticuerpos
        nuevos_clones = []
        for anticuerpo in mejores_anticuerpos:
            clones = clonar(anticuerpo)
            clones_mutados = mutar(clones)
            nuevos_clones.extend(clones_mutados)

        # Combinamos los nuevos clones con la población original y seleccionamos los mejores
