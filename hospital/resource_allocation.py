# hospital/resource_allocation.py
import asyncio

# Semáforos globales
camas_disponibles = asyncio.Semaphore(5)  # 5 camas disponibles
doctores_disponibles = asyncio.Semaphore(3)  # 3 doctores disponibles

async def allocate_resources(patient_id):
    print(f"Paciente {patient_id}: esperando cama...")
    async with camas_disponibles:
        print(f"Paciente {patient_id}: obtuvo cama.")
        print(f"Paciente {patient_id}: esperando doctor...")
        async with doctores_disponibles:
            print(f"Paciente {patient_id}: en consulta con doctor...")
            await asyncio.sleep(2)  # Simula tiempo de consulta
            print(f"Paciente {patient_id}: terminó consulta.")
        print(f"Paciente {patient_id}: liberó doctor.")
    print(f"Paciente {patient_id}: liberó cama.")
