import numpy as np


n_nodos = 10  # Número de ciudades/comidas
distance_matriz = np.random.randint(10, 50, (n_nodos, n_nodos))  # Matriz de distancias entre ciudades/nodos
np.fill_diagonal(distance_matriz, 0)  # Distancia de una ciudad a sí misma es 0

# Parámetros del algoritmo ACO
n_ants = 50  # Número de hormigas
n_iterations = 100  # Número de iteraciones
alpha = 0.1  # Importancia relativa de las feromonas
beta = 2  # Importancia relativa de la visibilidad (heurística)
rho = 0.5  # Tasa de evaporación de feromonas
Q = 10  # Constante para la actualización de feromonas

# Inicialización de feromonas
pheromone = np.ones((n_nodos, n_nodos))

# Función para calcular la visibilidad (heurística), que es el inverso de la distancia
visibility = 1 / (distance_matriz + np.diag([np.inf] * n_nodos))  # Evitar división por 0

# Función para elegir la siguiente ciudad
def choose_next_city(pheromone, visibility, visited, actual_city):
    probabilities = []
    for city in range(n_nodos):
        if city not in visited:
            prob = (pheromone[actual_city][city] * alpha) * (visibility[actual_city][city] * beta)
            probabilities.append(prob)
        else:
            probabilities.append(0)
    probabilities = probabilities / np.sum(probabilities)  # Normalizar probabilidades
    return np.random.choice(range(n_nodos), p=probabilities)

# Algoritmo de colonia de hormigas
best_distance = np.inf
best_solution = []

for iteration in range(n_iterations):
    all_solutions = []
    all_distances = []

    # Cada hormiga construye una solución
    for ant in range(n_ants):
        actual_city = np.random.randint(n_nodos)  # Ciudad inicial aleatoria
        visited = [actual_city]

        while len(visited) < n_nodos:
            next_city = choose_next_city(pheromone, visibility, visited, actual_city)
            visited.append(next_city)
            actual_city = next_city
        
        visited.append(visited[0])  # Volver a la ciudad inicial
        total_distance = sum(distance_matriz[visited[i], visited[i + 1]] for i in range(n_nodos))
        
        all_solutions.append(visited)
        all_distances.append(total_distance)
        
        # Actualizar la mejor solución
        if total_distance < best_distance:
            best_distance = total_distance
            best_solution = visited

    # Evaporación de feromonas
    pheromone *= (1 - rho)

    # Actualización de feromonas
    for i, solution in enumerate(all_solutions):
        for j in range(n_nodos):
            pheromone[solution[j], solution[j + 1]] += Q / all_distances[i]

print("Mejor solución encontrada:", best_solution)
print("Distancia total:", best_distance)