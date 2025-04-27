#main.py -> Principal por el momento
import asyncio
from hospital.patient import patient_flow

async def main():
    pacientes=[patient_flow(i) for i in range(10)] #10 pasientes "prueba"
    await asyncio.gather(*pacientes)
    
if __name__ == "__main__":
    asyncio.run(main())
