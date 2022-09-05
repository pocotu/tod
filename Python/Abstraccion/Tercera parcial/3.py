# crear un keyloger que capture las teclas presionadas del teclado y los muestre en pantalla

import pyautogui
import time

# bucle
while True:
    # capturar la tecla presionada
    x, y = pyautogui.position()
    # mostrar la tecla presionada
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    # 
    print(positionStr, end='')
    print('\b' * len(positionStr), end='', flush=True)
    time.sleep(0.1)
    if pyautogui.pixel(x, y) != (255, 255, 255):
        print('\nClick detected at ' + str(x) + ', ' + str(y))
        break

print('Done.')