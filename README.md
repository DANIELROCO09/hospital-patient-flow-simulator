🏥 Simulación de Procesos de Urgencias en un Hospital

Descripción General

Este proyecto simula el flujo de pacientes que llegan a un hospital, pasando por diferentes etapas:

- Registro

- Diagnóstico automatizado

- Asignación de recursos hospitalarios

- Seguimiento y alta

Características Principales

    Programación asíncrona: Uso de asyncio para manejar múltiples pacientes concurrentemente

    Procesamiento paralelo: Diagnósticos intensivos se ejecutan en procesos separados

    Gestión de recursos limitados: Semáforos para controlar acceso a camas y doctores

    Simulación realista: Tiempos de espera y procesamiento similares a un entorno real

```
📁 hospital_system/
├── main.py
├── hospital/
│   ├── __init__.py
│   ├── patient.py
│   ├── registration.py
│   ├── diagnosis.py
│   ├── resource_allocation.py
│   └── followup.py
└── README.md
```

Tecnologías utilizadas
Python 3.11+

asyncio (programación asíncrona)

multiprocessing (procesamiento paralelo)

threading y asyncio.Semaphore (control de concurrencia)

Librerías estándar de Python

Ejecución

1- Clona el repositorio:
``` gitclone 
2- Ejecuta la simulación:

3- Se simularán múltiples pacientes procesándose en paralelo y asincronía, mostrando el paso de cada paciente por el sistema.

Puedes modificar:

    Número de pacientes: Editar el rango en main.py

    Recursos disponibles: Ajustar los semáforos en resource_allocation.py

    Tiempos de procesamiento: Modificar los await asyncio.sleep() en los módulos correspondientes


