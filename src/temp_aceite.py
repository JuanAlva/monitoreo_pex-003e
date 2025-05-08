import os
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
try:
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
except Exception as e:
    print(f'no hay dato acetite {e}')
    

 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    try:
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(1)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            var = temp_c
            return temp_c
    except:
        temp_c = 0.00
        time.sleep(1)
        return temp_c

# Descomentar las siguientes lineas para prueba unitaria
# while(1):
#     tempe = read_temp() 
#     print(tempe)
#     time.sleep(1)
