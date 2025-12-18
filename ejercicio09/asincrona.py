import asyncio
import time
import random

async def consulta_bd(nombre):
    espera = random.randint(1, 5)
    print(f"Async: Iniciando {nombre} (Espera: {espera}s)")
    await asyncio.sleep(espera) 
    print(f"Async: Finalizó {nombre}")

async def main():
    tareas_nombres = ["Consulta 1", "Consulta 2", "Consulta 3"]
    
    print("\n--- EJECUCIÓN ASÍNCRONA ---")
    inicio = time.time()

    tareas_async = []
    for nombre in tareas_nombres:
        t = asyncio.create_task(consulta_bd(nombre))
        tareas_async.append(t)

    for t in tareas_async:
        await t

    print("Tiempo total Async:", time.time() - inicio)

asyncio.run(main())