# Description: This is bot automation script for piano tiles game.
# Descrição: Este é um script de automação de bot para o jogo piano tiles.
https://gameforge.com/en-US/littlegames/magic-piano-tiles/
# Importing libraries
# Importando bibliotecas
import pyautogui
import keyboard
import win32api # click faster in windows
import win32con # click faster in windows
from time import sleep
# coordinates for click button start
# coordenadas para clicar no botão iniciar
pyautogui.click(X, y)
# function to click the tiles
# função para clicar nas teclas do piano
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    sleep(0.05)
# loop to run the code until the key 1 is pressed
# loop para executar o código até que a tecla 1 seja pressionada
while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(X, Y, (0, 0, 0)):
        click(X, Y)
    if pyautogui.pixelMatchesColor(X, Y, (0, 0, 0)):
        click(X, Y)
    #repeat the same for all the piano tiles
    # repita o mesmo para todas as teclas do piano