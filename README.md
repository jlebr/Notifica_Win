# Acerca de lo que se encuentra en el proyecto 

En la primer test_01 se puede enviar notifiación con un titulo y un mensaje

```python
toaster = ToastNotifier()

# Enviar notificación con imagen led ON
toaster.show_toast("Estado de LED", 
                   "Se ha encendido el LED", 
                   icon_path="C:/Users/JelizmarAgreda/OneDrive/Escritorio/Notifica_win/led_on.ico", 
                   duration=10,)
```
En el segundo test_02 se puede enviar notifiación, cambiar el tipo de audio, agregar una imagen, colocar una cacción al hacer click en un boton.
```python
toast = Notification(app_id="Ardu LED",
                     title="Informe de estado", 
                     msg="LED Encendido",
                     duration="long",
                     icon=ruta_led_on)
# Configuración de los tipos de audio en la  notifiación
toast.set_audio(audio.LoopingCall, loop=True)

# agregar una acción cuando a la notificación se le de Click
toast.add_actions(label="Ir a Dash board", launch="https://www.google.com/")

# Mostar el objeto 
toast.show()
```

=================================================================

#Se puede instalar todas las librerias usando el requirements.txt
1) acceder a la tuta del txt
2) Ejecutar el comando pip install -r requirements.txt

