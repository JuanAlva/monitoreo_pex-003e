# Sistema de Monitoreo de Temperaturas para PEX 003E

Este proyecto implementa una interfaz gráfica en `Tkinter` para visualizar en tiempo real parámetros críticos de temperatura y presión en un entorno industrial, junto con un servidor OPC UA que expone dichos datos a sistemas externos.

![WhatsApp Image 2025-05-08 at 11 48 29_3accfee3](https://github.com/user-attachments/assets/9742fba1-4ee4-406c-afa5-58aa2f54c02a)

## 📌 Características

- 🖥 Interfaz gráfica de usuario en pantalla completa con `Tkinter` y `ttkbootstrap`.
- 🌡 Monitoreo de temperatura del tocho, motor, bomba principal, bomba auxiliar y aceite.
- ⚙️ Lectura de presión de bomba principal y auxiliar mediante conversión analógica-digital.
- 🔌 Servidor OPC UA embebido para integración con sistemas SCADA.
- 🕒 Reloj en tiempo real.
- ⚠️ Indicadores visuales de alerta si los valores están fuera de rango.

## 🔼 Diagrama de conexiones

![diagrama6 drawio](https://github.com/user-attachments/assets/ca56fa0e-f211-4188-8949-dcdb676030e0)

## 🧰 Tecnologías usadas

- Python 3
- Tkinter + ttkbootstrap
- Adafruit MLX90614 (sensor IR)
- Librería `opcua` para servidor OPC UA
- ADS1115 para lectura analógica (via módulo `adc.py`)
- Módulos personalizados:
  - `temp_aceite.py`
  - `sensor_ir.py`
  - `adc.py`

## 🛠 Características

Esto abrirá la interfaz en modo pantalla completa y levantará el servidor OPC UA en la dirección:

opc.tcp://192.168.146.50:4840

📁 Estructura del proyecto

├── adc.py                  # Funciones para lectura analógica
├── temp_aceite.py          # Lectura de temperatura de aceite
├── sensor_ir.py            # Lectura desde sensor MLX90614
├── main.py                 # Archivo principal con interfaz y lógica
├── img/
│   └── ememsa.png          # Imagen del logo
├── requirements.txt        # Lista de dependencias
└── README.md               # Este archivo

## 🧪 Variables OPC UA expuestas

- Tocho
- Presion Bomba Principal
- Presion Bomba Auxiliar
- Motor
- Bomba principal
- Bomba auxiliar
- Aceite

## 📄 Créditos

Desarrollado por Juan Alva
