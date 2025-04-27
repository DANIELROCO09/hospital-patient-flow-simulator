# hospital/diagnosis.py
import asyncio
import multiprocessing
import time

def intensive_diagnosis(patient_id):
    """Realiza un diagnóstico médico intensivo de forma síncrona.
    Simula un proceso de diagnóstico computacionalmente intensivo que bloquea el hilo de ejecución.
    Args:
        patient_id (str/int): Identificador único del paciente a diagnosticar.    
    Returns:
        None: La función no retorna valores, solo imprime resultados en consola.  
    Side Effects:
        - Bloquea el hilo de ejecución durante aproximadamente 5 segundos.
        - Imprime mensajes sobre el progreso del diagnóstico."""
    
    print(f"Diagnóstico intenso para paciente {patient_id}...")
    time.sleep(5)  # Simula procesamiento pesado
    print(f"Diagnóstico completo para paciente {patient_id}.")

async def diagnose_patient(patient_id):
    """Realiza un diagnóstico médico de forma asíncrona usando un executor.
    Esta función permite ejecutar el diagnóstico intensivo sin bloquear el event loop
    principal, delegando el trabajo a un executor.
    Args:
        patient_id (str/int): Identificador único del paciente a diagnosticar.
    Returns:
        None: La función no retorna valores directamente (es una corrutina).
    Side Effects:
        - Ejecuta intensive_diagnosis en un hilo/process separado.
        - Permite que el event loop continúe procesando otras tareas durante el diagnóstico."""

    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, intensive_diagnosis, patient_id)
