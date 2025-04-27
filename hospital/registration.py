# hospital/registration.py
import asyncio

async def register_patient(patient_id):
    print(f"Paciente {patient_id}: registro iniciado...")
    await asyncio.sleep(1)  # Simula tiempo de registro
    print(f"Paciente {patient_id}: registro completado.")
