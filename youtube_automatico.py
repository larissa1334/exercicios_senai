import pyautogui as pag
from time import sleep

# pag.displayMousePosition()

pag.press('win')
pag.write('chrome')
pag.press('enter')
pag.moveTo(960,581)
sleep(2)
pag.click()
sleep(2)
pag.write('www.youtube.com.br')
pag.press('enter')
sleep(2)
pag.moveTo(820,121)
pag.click()
pag.write("Drake - God's Plan")
pag.press('enter')
pag.moveTo(660,394,duration=1)
pag.click()
pag.alert('fim')
