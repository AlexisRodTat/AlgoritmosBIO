import random

# Parámetros del algoritmo genético
TAMANO_POBLACION = 10       # Tamaño de la población
GENERACIONES = 20           # Número de generaciones
TAMANO_CROMOSOMA = 5        # Tamaño de cada cromosoma
PROB_MUTACION = 0.1         # Probabilidad de mutación

# Función de aptitud (fitness): la suma de valores en el cromosoma
def calcular_aptitud(cromosoma):
    return sum(cromosoma)

# Generación inicial de una población aleatoria
def crear_poblacion():
    return [[random.randint(0, 1) for _ in range(TAMANO_CROMOSOMA)] for _ in range(TAMANO_POBLACION)]

# Selección de individuos: selección por torneo
def seleccion(poblacion):
    padre1 = max(random.sample(poblacion, 2), key=calcular_aptitud)
    padre2 = max(random.sample(poblacion, 2), key=calcular_aptitud)
    return padre1, padre2

# Cruza o crossover: combinación de genes entre dos padres
def cruzar(padre1, padre2):
    punto_cruce = random.randint(1, TAMANO_CROMOSOMA - 1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

# Mutación: alteración aleatoria de un gen
def mutar(cromosoma):
    for i in range(TAMANO_CROMOSOMA):
        if random.random() < PROB_MUTACION:
            cromosoma[i] = 1 - cromosoma[i]  # Cambia 0 a 1 o 1 a 0
    return cromosoma

# Evolución de la población a través de generaciones
def algoritmo_genetico():
    poblacion = crear_poblacion()

    for generacion in range(GENERACIONES):
        # Ordenamos la población por aptitud (de mayor a menor)
        poblacion = sorted(poblacion, key=calcular_aptitud, reverse=True)

        # Imprimimos el mejor individuo de la generación actual
        mejor_individuo = poblacion[0]
        print(f"Generación {generacion + 1}: Mejor solución = {mejor_individuo}, Aptitud = {calcular_aptitud(mejor_individuo)}")

        # Nueva generación
        nueva_poblacion = poblacion[:2]  # Los mejores pasan directamente a la siguiente generación

        # Generar nuevos individuos mediante cruzamiento y mutación
        while len(nueva_poblacion) < TAMANO_POBLACION:
            padre1, padre2 = seleccion(poblacion)
            hijo1, hijo2 = cruzar(padre1, padre2)
            nueva_poblacion.extend([mutar(hijo1), mutar(hijo2)])

        poblacion = nueva_poblacion  # Actualizamos la población con la nueva generación

# Ejecutamos el algoritmo genético
algoritmo_genetico()
