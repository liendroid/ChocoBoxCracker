#Main Driver for the game
from gpiozero import Button
from gpiozero import RGBLED


#LED column button selection
col1Btn = Button() #pin location
col2Btn = Button() 
col3Btn = Button()
col4Btn = Button()

#LED colour selection
blackBtn = Button() #1
orangeBtn = Button() #2 
blueBtn = Button()  #3
pinkBtn = Button() #4

#LED code
aLED = RGBLED(1, 1, 1).off()
bLED = RGBLED(1, 1, 1).off()
cLED = RGBLED(1, 1, 1).off()
dLED = RGBLED(1, 1, 1).off()

#Submit button
submitBtn = Button() 

#LED correct status
wLED = RGBLED(1, 1, 1).off()
xLED = RGBLED(1, 1, 1).off()
yLED = RGBLED(1, 1, 1).off()
zLED = RGBLED(1, 1, 1).off()

def start()
	

def initalizeDevices()

	