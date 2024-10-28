import pyautogui as py
import time as ti 



#ir para o ACTWEB na barra de favoritos
py.moveTo(290,86,0.5)
ti.sleep(1)

#clicar no link
py.click(290,86,button='left')



#ir para termometro
py.moveTo(46,985,2)
py.click(46,985,button='left')
ti.sleep(2)
py.press('down',presses=2,interval=1)
py.moveTo(117,945,1)
py.click(117,945,button='left')

ti.sleep(1)

#Centro leste
py.moveTo(588,555,1.5)
py.click(588,555,button='left')
py.moveTo(1295,607)
py.leftClick(1295,607)
py.press('down',presses=20,interval=0.5)

#Minas Rio
py.moveTo(441,782,0.5)


