import threading
import time
import random
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOOGLE_KEY = KeyCode(char="t") # Esta es la tecla para activar y desactivar el script


clicking = False
mouse = Controller()

def clicker():
    min_click = 50 # Clics por segundo mínimo
    max_click = 100 # Clics por segundo máximo
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            random_speed = random.uniform( 1 / min_click, 1 / max_click)
            time.sleep(random_speed)

        time.sleep(0.00001) # Esta es una pausa para descanzar el procesador

def toggle_event(key):
    if key == TOOGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as Listener:
    Listener.join()