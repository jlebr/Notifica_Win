from winotify import Notification, audio

# Ruta donde esta la imagen del led
ruta_led_on="C:/Users/JelizmarAgreda/OneDrive/Escritorio/Notifica_win/led_on.ico"

# Datos de la notificación
toast = Notification(app_id="Ardu LED",
                     title="Informe de estado", 
                     msg="LED Encendido",
                     duration="long",
                     icon=ruta_led_on)

# Configuración de los tipos de audio en la  notifiación
#toast.set_audio(audio.Default, loop=False)
#toast.set_audio(audio.SMS, loop=False)
#toast.set_audio(audio.Mail, loop=False)
#toast.set_audio(audio.LoopingAlarm, loop=True)
toast.set_audio(audio.LoopingCall, loop=True)

# agregar una acción cuando a la notificación se le de Click
toast.add_actions(label="Ir a Dash board", launch="https://www.google.com/")

# Mostar el objeto 
toast.show()