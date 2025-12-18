import threading
import time
import random

def consulta_bd(nombre):
    espera = random.randint(1, 5)
    print(f"Hilo: Iniciando {nombre} (Espera: {espera}s)")
    time.sleep(espera)
    print(f"Hilo: Finalizó {nombre}")

tareas = ["Consulta 1", "Consulta 2", "Consulta 3"]

print("--- EJECUCIÓN CON HILOS ---")
inicio = time.time()

hilos = []
for nombre in tareas:
    h = threading.Thread(target=consulta_bd, args=(nombre,))
    h.start()
    hilos.append(h)

for h in hilos:
    h.join()

print("Tiempo total Hilos:", time.time() - inicio)