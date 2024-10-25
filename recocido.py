import math
import random
# Definir la función de costo (puedes ajustarla según el problema específico)
def f(solution):
    # Ejemplo de una función de costo que se puede optimizar (minimización de x^2)
    return solution**2
# Generar una solución vecina (modificar la solución actual ligeramente)
def neighbor(S):
    # Modificar la solución actual sumando o restando un pequeño valor aleatorio
    return S + random.uniform(-1, 1)
# Algoritmo de recocido simulado
def simulated_annealing(S0, T_initial, cooling_rate, max_iter):
    S = S0  # Solución inicial
    T = T_initial  # Temperatura inicial
    best_solution = S0
    best_cost = f(S0)
    
    for i in range(max_iter):
        # Generar una solución vecina
        S_prime = neighbor(S)
        # Evaluar el cambio de energía/costo
        delta_E = f(S_prime) - f(S)
        # Si la nueva solución es mejor, la aceptamos
        if delta_E < 0:
            S = S_prime
            if f(S) < best_cost:
                best_solution = S
                best_cost = f(S)
        # Si no es mejor, la aceptamos con una probabilidad dependiente de la temperatura
        else:
            if math.exp(-delta_E / T) > random.random():
                S = S_prime
        # Reducir la temperatura
        T = T * cooling_rate
        # Mostrar el progreso cada 10 iteraciones
        if i % 10 == 0:
            print(f"Iteración {i}: Mejor solución = {best_solution}, Mejor costo = {best_cost}")
        # Criterio de parada (podemos detener si la temperatura es muy baja)
        if T < 1e-10:
            break

    return best_solution, best_cost
# Parámetros de ejemplo
S0 = random.uniform(-1, 10)  # Solución inicial aleatoria en el rango [-10, 10]
T_initial = 100  # Temperatura inicial
cooling_rate = 0.88  # Tasa de enfriamiento
max_iter = 100  # Número máximo de iteraciones

# Ejecutar el algoritmo de recocido simulado
best_solution, best_cost = simulated_annealing(S0, T_initial, cooling_rate, max_iter)

print(f"La mejor solución encontrada es {best_solution} con un costo de {best_cost}")