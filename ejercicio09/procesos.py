import multiprocessing
import time
import random

def consulta_bd(nombre):
    espera = random.randint(1, 5)
    print(f"Proceso: Iniciando {nombre} (Espera: {espera}s)")
    time.sleep(espera)
    print(f"Proceso: Finalizó {nombre}")

tareas = ["Consulta 1", "Consulta 2", "Consulta 3"]

if __name__ == '__main__':
    print("\n--- EJECUCIÓN CON PROCESOS ---")
    inicio = time.time()

    procesos = []
    for nombre in tareas:
        p = multiprocessing.Process(target=consulta_bd, args=(nombre,))
        p.start()
        procesos.append(p)

    for p in procesos:
        p.join()

    print("Tiempo total Procesos:", time.time() - inicio)