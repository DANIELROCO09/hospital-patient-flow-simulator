# hospital/followup.py
import asyncio

async def followup_patient(patient_id):
    print(f"Paciente {patient_id}: seguimiento post-tratamiento...")
    await asyncio.sleep(1)  # Simula tiempo de observación
    print(f"Paciente {patient_id}: listo para alta.")
