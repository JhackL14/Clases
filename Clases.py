#Autor: Joel Garcia
import random
class Sistema_solar:
    contador_id = 1  

    def __init__(self, nombre):
        self.nombre = nombre
        self.planetas = []

    def agregar_planeta(self, nombre, masa, densidad, diametro, distancia_sol):
        planeta = {
            "id": Sistema_solar.contador_id,
            "nombre": nombre,
            "masa": masa,
            "densidad": densidad,
            "diametro": diametro,
            "distancia_sol": distancia_sol
        }
        Sistema_solar.contador_id += 1
        self.planetas.append(planeta)
        print(f"Planeta {nombre} agregado con ID {planeta['id']}.")
        return planeta


    def mostrar_planeta_por_id(self, id_busqueda):
        for planeta in self.planetas:
            if planeta['id'] == id_busqueda:
                print(f"ID: {planeta['id']}, Nombre: {planeta['nombre']}, Masa: {planeta['masa']}, "
                      f"Densidad: {planeta['densidad']}, Diámetro: {planeta['diametro']}, "
                      f"Distancia al Sol: {planeta['distancia_sol']}")
                return
        print(f"No se encontró una planeta con ID: {id_busqueda}")

    def mostrar_todas_los_planetas(self):
        for planeta in self.planetas:
            print(f"ID: {planeta['id']}, Nombre: {planeta['nombre']}, Masa: {planeta['masa']}, "
                  f"Densidad: {planeta['densidad']}, Diámetro: {planeta['diametro']}, "
                  f"Distancia al Sol: {planeta['distancia_sol']}")
    
    def gravitacion(self, id1, id2):
        G = 6.67430e-11
        p1 = self.planetas[id1 - 1]
        p2 = self.planetas[id2 - 1]
        
        m1, m2 = p1['masa'], p2['masa']
        d = abs(p1['distancia_sol'] - p2['distancia_sol']) * 1e3  # km a m
        if d == 0:
            print("Los planetas tienen la misma distancia al Sol.")
            return None
        f = G * m1 * m2 / d**2
        print(f"Fuerza gravitacional entre {p1['nombre']} y {p2['nombre']}: {f:.3e} N")
        return f


# sol = Sistema_solar("Sol")
# sol.agregar_planeta("Mercurio", 3.30e23, 5.43, 4879, 57.9e6)
# sol.agregar_planeta("Venus", 4.87e24, 5.24, 12104, 108.2e6)
# sol.agregar_planeta("Tierra", 5.97e24, 5.52, 12756, 149.6e6)

# sol.mostrar_planeta_por_id(3)

# sol.mostrar_todas_los_planetas()

# sol.gravitacion(1, 3)

import random

class Lista_Aleatoria:
    def __init__(self, n):
        self.n = n
        self.lista = random.sample(range(1, n + 1), n)
        print(f"Lista aleatoria: {self.lista}")

    def ordenar_burbuja(self):
        arr = self.lista.copy()
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Lista ordenada por burbuja: {arr}")
        return arr

    def ordenar_quicksort(self):
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivote = arr[0]
            menores = [x for x in arr[1:] if x <= pivote]
            mayores = [x for x in arr[1:] if x > pivote]
            return quicksort(menores) + [pivote] + quicksort(mayores)
        ordenada = quicksort(self.lista)
        print(f"Lista ordenada por quicksort: {ordenada}")
        return ordenada


nums  = Lista_Aleatoria(10)
Lista_Aleatoria.ordenar_burbuja(nums)
Lista_Aleatoria.ordenar_quicksort(nums)