from Adafruit_ADS1x15 import ADS1115

# Funcion para mapear un valor de un rango a otro
def mapear(v, re_min, re_max, rs_min, rs_max):
    p = (v - re_min) / (re_max - re_min)
    value = rs_min + p * (rs_max - rs_min)
    return value

#Inicializa una sola instancia del ADC (para evitar inicializarlo en cada lectura)
adc = ADS1115(address=0x48, busnum=1)

def dato_adc(nInput, volMin, volMax, ranMin, ranMax):
        
    Gain = 1
    Scale = {2/3:6.144,
            1:4.096,
            2:2.048,
            4:1.024,
            8:0.512,
            16:0.256}
    
    # Leer el valor del ADc
    value = adc.read_adc(nInput, Gain)
    temp = (value * Scale[Gain]) / 32767
    temp = round(temp, 2)
    
    # Asegurar que el valor esta en el rango
    temp = max(volMin, min(temp, volMax))
    
    # Convertir a la unidad deseada
    valor = mapear(temp, volMin, volMax, ranMin, ranMax)
    valor = round(valor, 2)
    
    # Asegurar que el valor mapeado este dentro de los limites correctos
    valor = max(ranMin, min(valor, ranMax))
    
    return temp, valor

# tocho = dato_adc(0x48)
# print(tocho, type(tocho))