# AutoClicker con Velocidad Aleatoria

Este proyecto es un **AutoClicker** desarrollado en Python, utilizando la biblioteca `pynput` para controlar el mouse y el teclado. Permite realizar clics automáticos con un intervalo aleatorio dentro de un rango definido. La activación y desactivación del clic automático se realiza con la tecla `T`.

## 🔧 Características
- Simulación de clics automáticos con el botón izquierdo del mouse.
- Intervalo aleatorio entre clics para imitar una interacción más natural.
- Activación y desactivación con la tecla `T`.
- Código optimizado para evitar el uso excesivo del procesador.

![image](https://github.com/user-attachments/assets/948fd53c-b54b-485d-a085-4d2b6b3123a0)

## 🚀 Requisitos
Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install pynput
```


⚙️ Uso
- Ejecuta el script con Python.
- Presiona T para iniciar o detener el clic automático.
- Observa en la consola el intervalo aleatorio entre clics.
- Finaliza el script cerrando la ventana o deteniéndolo con Ctrl + C.
🛠️ Configuración
Si deseas modificar la velocidad de los clics, puedes cambiar los valores de min_click y max_click en el código:
min_click = 50  # Clics por segundo mínimo
max_click = 100 # Clics por segundo máximo

📝 Licencia
Este proyecto es de código abierto y puedes utilizarlo libremente. Se recomienda su uso responsable.
