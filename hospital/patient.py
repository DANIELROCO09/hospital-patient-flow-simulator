#hospital/patient.py
import asyncio
from hospital.registration import register_patient
from hospital.diagnosis import diagnose_patient
from hospital.resource_allocation import allocate_resources
from hospital.followup import followup_patient

async def patient_flow(patient_id):
    print(f"Paciente {patient_id} llegó al hospital.")
    await register_patient(patient_id)
    await diagnose_patient(patient_id)
    await allocate_resources(patient_id)
    await followup_patient(patient_id)
    print(f"Paciente {patient_id} ha sido dado de alta.\n")
