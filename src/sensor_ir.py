import board
import busio as io
from adafruit_mlx90614 import MLX90614
import time

def read_sensor_ir(addr):
    try:
        i2c = io.I2C(board.SCL, board.SDA)
        sensor = MLX90614(i2c, address=addr)
        valor = "{:.2f}".format(sensor.object_temperature)
        return valor
    
    except OSError as e:
        if e.errno == 5:
            print("Error de entrada/salida detectado. Reintentando...")
            time.sleep(1) # Espera antes de reintentar
            # Intentar reestablecer la conexin I2C
            i2c = io.I2C(board.SCL. board.SDA)
            sensor = MLX90614(i2c, address=addr)

# Descomentar las siguientes lineas para prueba unitaria
#while(1):
        
#    temp = read_sensor_ir(0x5A)
#    temp2 = read_sensor_ir(0x5B)
#    temp3 = read_sensor_ir(0x5C)
#    print(temp," ",temp2," ",temp3," ",type(temp3))
#    time.sleep(1)