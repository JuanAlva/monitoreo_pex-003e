from tkinter import *
from ttkbootstrap import Style
from datetime import datetime
import time

from adafruit_mlx90614 import MLX90614
from temp_aceite import read_temp
from sensor_ir import read_sensor_ir
from adc import dato_adc

from opcua import Server

server = Server()
url = "opc.tcp://192.168.146.50:4840"
server.set_endpoint(url)

name = "OPCUA_PEX_SERVER"
addSpace = server.register_namespace(name)

node = server.get_objects_node()

ServerInfo = node.add_object(addSpace, "OPCUA Pex Server")
Param = node.add_object(addSpace, "Parameters")


temp_tocho = Param.add_variable(addSpace, "Tocho", 0)
pres_bomba_pri = Param.add_variable(addSpace, "Presion Bomba Principal", 0)
pres_bomba_aux = Param.add_variable(addSpace, "Presion Bomba Auxiliar", 0)
temp_motor = Param.add_variable(addSpace, "Motor", 0)
temp_bomba_pri = Param.add_variable(addSpace, "Bomba principal", 0)
temp_bomba_aux = Param.add_variable(addSpace, "Bomba auxiliar", 0)
temp_aceite = Param.add_variable(addSpace, "Aceite", 0)


temp_tocho.set_writable()
pres_bomba_pri.set_writable()
pres_bomba_aux.set_writable()
temp_motor.set_writable()
temp_bomba_pri.set_writable()
temp_bomba_aux.set_writable()
temp_aceite.set_writable()

server.start()
print("server started at {}".format(url))
    
var = 1

# Configuracion de los canales y rangos de conversion
#canal_0 = {"canal": 0, "volMin": 0.01, "volMax": 3.275, "ranMin": 250.0, "ranMax": 1600.0}, # AIN0
#canal_1 = {"canal": 1, "volMin": 0.01, "volMax": 3.275, "ranMin": 0.0, "ranMax": 300.0}, # AIN1
#canal_2 = {"canal": 2, "volMin": 0.01, "volMax": 3.275, "ranMin": 0.0, "ranMax": 200.0}, #AIN2

#adc = ADS1115(address=0x48, busnum=1)

class MainPage:
    def __init__(self):
        self.ventana = Tk()
        #self.ventana.geometry("590x220")
        self.ventana.wm_attributes("-fullscreen", True)
        self.ventana.title("TEMPERATURA TOCHOS")
        #self.ventana.iconbitmap("img/ememsa.ico")     
        
        imagen = PhotoImage(file="/home/ememsa/mis_archivos/img/ememsa.png")
        estilo = Style()
        estilo.configure("Tframe", background="lightgray")
        #FRAME TOP
        self.frame_top = Frame(self.ventana, borderwidth=3, relief="solid")
        self.frame_top.place(x=5,y=5,width=1270,height=85)
        titulo_general = Label(self.ventana, text="CONTROL TEMPERATURA PEX 003E", font=("Times New Roman", 23, "bold"), fg="blue")
        titulo_general.place(x=385, y=30)
        label_imagen = Label(self.frame_top, image=imagen)
        label_imagen.place(x=5,y=0)
        #FRAME LEFT
        self.frame_left = Frame(self.ventana, borderwidth=3, relief="solid")
        self.frame_left.place(x=5, y=87, width=1270, height=900)
        self.reloj = Label(self.frame_left,font=("Times New Roman", 20, "bold"))
        self.reloj.place(x=580, y=5)
        #imgTemp = PhotoImage(file="img/sensorr.png")
        #label_imgTemp = Label(self.frame_left, image=imgTemp)
        #label_imgTemp.place(x=320, y=40)
        tempTocho = Label(self.frame_left, text="TEMPERATURA DEL TOCHO:", font=("Times New Roman", 20, "bold"))
        tempTocho.place(x=15, y=5)

        self.datoTemp = StringVar()
        #self.datoMensage = StringVar()
        #self.datoMensage2 = StringVar()
        self.presionBombaPri = StringVar()
        self.presionBombaAux = StringVar()
        self.tempAceite = StringVar()
        self.tempBombaAuxiliar =StringVar()
        self.tempBombaPrincipal = StringVar()
        self.tempMotor = StringVar()
        
        self.botonTemp = Button(self.frame_left, textvariable=self.datoTemp, font=("Times New Roman", 240, "bold"))
        self.botonTemp.place(x=15, y=45)

        self.popUp = Label(self.frame_left)
        self.popUp.place(x=14, y=45)

        self.popUp2 = Label(self.frame_left)
        self.popUp2.place(x=14, y=218)

        #self.LabelMesage = Label(self.frame_left, textvariable=self.datoMensage, font=("Times New Roman", 20, "bold"))
        #self.LabelMesage.place(x=15, y=420)

        #self.LabelMesage2 = Label(self.frame_left, textvariable=self.datoMensage2, font=("Times New Roman", 20, "bold"))
        #self.LabelMesage2.place(x=15, y=450)

        #indicador de la presion de la bomba principal
        presionBombaPri = Label(self.frame_left, text="PRESION B. PRINCIPAL:", font=("Times New Roman", 20, "bold"))
        presionBombaPri.place(x=15, y=425)

        self.botonPresBombaPri = Button(self.frame_left, textvariable=self.presionBombaPri, font=("Times New Roman", 60, "bold"))
        self.botonPresBombaPri.place(x=15, y=460)
        
        #indicador de la presion de la bomba auxiliar
        presionBombaAux = Label(self.frame_left, text="PRESION B. AUXILIAR:", font=("Times New Roman", 20, "bold"))
        presionBombaAux.place(x=450, y=425)

        self.botonPresBombaAux = Button(self.frame_left, textvariable=self.presionBombaAux, font=("Times New Roman", 60, "bold"))
        self.botonPresBombaAux.place(x=450, y=460)
        
        #indicador de la temperatura del motor
        tempMotor = Label(self.frame_left, text="MOTOR:", font=("Times New Roman", 20, "bold"))
        tempMotor.place(x=950, y=5)

        self.botonTempMotor = Button(self.frame_left, textvariable=self.tempMotor, font=("Times New Roman", 60, "bold"))
        self.botonTempMotor.place(x=950, y=40)

        #indicador de la temperatura de la bomba principal
        tempBombaPrincipal = Label(self.frame_left, text="BOMBA PRINCIPAL:", font=("Times New Roman", 20, "bold"))
        tempBombaPrincipal.place(x=950, y=145)

        self.botonTempBombaPrincipal = Button(self.frame_left, textvariable=self.tempBombaPrincipal, font=("Times New Roman", 60, "bold"))
        self.botonTempBombaPrincipal.place(x=950, y=180)

        #indicador de la temperatura de la bomba auxiliar
        tempBombaAuxiliar = Label(self.frame_left, text="BOMBA AUXILIAR:", font=("Times New Roman", 20, "bold"))
        tempBombaAuxiliar.place(x=950, y=285)

        self.botonTempBombaAuxiliar = Button(self.frame_left, textvariable=self.tempBombaAuxiliar, font=("Times New Roman", 60, "bold"))
        self.botonTempBombaAuxiliar.place(x=950, y=320)

        #indicador de la temperatura del aceite
        tempAceite = Label(self.frame_left, text="ACEITE:", font=("Times New Roman", 20, "bold"))
        tempAceite.place(x=950, y=425)

        self.botonTempAceite = Button(self.frame_left, textvariable=self.tempAceite, font=("Times New Roman", 60, "bold"))
        self.botonTempAceite.place(x=950, y=460)

        #self.boton = Button(self.frame_left, text="OBTENER TEMPERATURA", command=self.analizarTemperatura)
        #self.boton.place(x=55, y=130)

        buttonClose = Button(self.ventana, text="X", font=("Times New Roman", 42, "bold"), command=self.close_aplication)
        buttonClose.place(x=1202, y=9)

        buttonClose.config(bg="red")
        buttonClose.config(fg="black")

        self.actualizar_reloj()
        self.analizarTemperatura()
        self.ventana.mainloop()
        
    def close_aplication(self):
        self.ventana.destroy()
    
    def actualizar_reloj(self):
        hora = datetime.now().strftime("%H:%M:%S")
        self.reloj.config(text=hora)
        self.reloj.after(1000, self.actualizar_reloj)
        
    def analizarTemperatura(self):
        time.sleep(0.06)
        try:
            # Lectura del primer canal (AIN0)
            temp_0, dato_0 = dato_adc(1, 0.05, 2.977, 250.0, 1600.0)
            valueLectura = int(float(dato_0))
            temp_tocho.set_value(valueLectura)
            self.datoTemp.set(f"{valueLectura}°C")
            print(f"tocho: {temp_0}, {dato_0}")
            
            if valueLectura < 275:
                self.popUp.config(text="FUERA DE", font=("Times New Roman", 127, "bold"), bg="#ffcc00", fg="red")
                self.popUp2.config(text="   RANGO  ", font=("Times New Roman", 127, "bold"), bg="#ffcc00", fg="red")
            else:
                self.popUp.config(text="", font=("Times New Roman", 1, "bold"), bg="white")
                self.popUp2.config(text="", font=("Times New Roman", 1, "bold"), bg="white")

            if  valueLectura < 700:
                self.botonTemp.config(bg="#ffcc00")
                #self.datoMensage.set("ESPERE...")
                #self.datoMensage2.set("TEMPERATURA SUBIENDO")
                #self.LabelMesage2.config(fg="#ffcc00")
            
            elif 700 <= valueLectura <= 800:
                self.botonTemp.config(bg="green")
                #self.datoMensage.set("TEMPERATURA ÓPTIMA!!!")
                #self.datoMensage2.set("RETIRAR EL TOCHO.")
                #self.LabelMesage2.config(fg="green")
                
            elif 800 <= valueLectura:
                self.botonTemp.config(bg="red")
                #self.datoMensage.set("TEMPERATURA NO APTA!!!")
                #self.datoMensage2.set("TOCHO MUY CALIENTE.")
                #self.LabelMesage2.config(fg="red")
            #time.sleep(0.1)
        except OSError as e:
            if e.errno == 121:
                time.sleep(0.1)
        
        time.sleep(0.06)
        try:
            pres_1, dato_1 = dato_adc(2, 0.05, 3.15, 0.0, 300.0)
            valueLectura6 = int(float(dato_1) * 14.5038)
            pres_bomba_pri.set_value(valueLectura6)
            self.presionBombaPri.set(f"{valueLectura6} psi")
            print(f"presion pri: {pres_1}, {dato_1}")
            #time.sleep(0.1)
        
        except OSError as e:
            if e.errno == 121:
                time.sleep(0.1)
                
        time.sleep(0.06)
        try:
            pres_2, dato_2 = dato_adc(0, 0.05, 3.15, 0.0, 200.0)
            valueLectura7 = int(float(dato_2) * 14.5038)
            pres_bomba_aux.set_value(valueLectura7)
            self.presionBombaAux.set(f"{valueLectura7} psi")
            print(f"presion aux: {pres_2}, {dato_2}")
            #time.sleep(0.1)
        
        except OSError as e:
            if e.errno == 121:
                time.sleep(0.1)
        
        try:
            valueLectura5 = "{:.2f}".format(read_temp())
#             if valueLectura5 != 0.0:
#                 var = valueLectura5
            temp_aceite.set_value(valueLectura5)
            self.tempAceite.set(f"{valueLectura5}°C")#SE CAMBIO DE VARIABLE A 0
#             else:
#                 self.tempAceite.set(f"{var}°C")
        except:
#             var = valueLectura5
#             self.tempAceite.set(f"{valueLectura5}°C")
            time.sleep(0.1)
        
        try:
            valueLectura4 = read_sensor_ir(0x5C)
            temp_motor.set_value(valueLectura4)
            self.tempMotor.set(f"{valueLectura4}°C")

            valueLectura3 = read_sensor_ir(0x5B)
            temp_bomba_pri.set_value(valueLectura3)
            self.tempBombaPrincipal.set(f"{valueLectura3}°C")

            valueLectura2= read_sensor_ir(0x5A)
            temp_bomba_aux.set_value(valueLectura2)
            self.tempBombaAuxiliar.set(f"{valueLectura2}°C")
        except:
            time.sleep(0.1)
        
        self.ventana.after(2000, self.analizarTemperatura)

MainPage()

