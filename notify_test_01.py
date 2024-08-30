# instalar la libreria wint10toast que permite enviar notifiaciones
#pip install win10toast

import time
from win10toast import ToastNotifier

Ruta1= "C:/Users/JelizmarAgreda/OneDrive/Escritorio/Notifica_win/led_on.ico"
Ruta2= "C:/Users/JelizmarAgreda/OneDrive/Escritorio/Notifica_win/led_off.ico"
print("Sale notifiación led ON")
""""
# Enviar solo notificación
toaster = ToastNotifier()
toaster.show_toast("Título de la Notificación", "Este es el mensaje de la notificación", duration=20)
"""


toaster = ToastNotifier()

# Enviar notificación con imagen led ON
toaster.show_toast("Estado de LED", 
                   "Se ha encendido el LED", 
                   icon_path="C:/Users/JelizmarAgreda/OneDrive/Escritorio/Notifica_win/led_on.ico", 
                   duration=10,)

print("Esperando 30 segundos...")
time.sleep(30)

print("Sale notificación con led OFF")
# Enviar notificación con imagen led OFF
toaster.show_toast("Estado de LED", 
                   "Se ha apagado el LED", 
                   icon_path=Ruta2, 
                   duration=10)

