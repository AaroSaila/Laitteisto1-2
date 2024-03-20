from machine import Pin, I2C
import ssd1306
from time import sleep_ms


# Screen dimensions
SCREENW = 128
SCREENH = 64

# First pixel position 
PIXELX = 0
PIXELY = int(SCREENH / 2)

# Bottom and right corners for pixel
BORDERX = SCREENW
BORDERY = SCREENH - 1


def checkCoord(coords):
    if coords["x"] > BORDERX:
        coords["x"] = PIXELX
    if coords["y"] < 0:
        coords["y"] = 0
    if coords["y"] > BORDERY:
        coords["y"] = BORDERY
    return coords
        

def updatePixel(oled, coords, btnD, btnU, btnR):
    if btnR.value() == 0:
        oled.fill(0)
        coords = {"x": PIXELX, "y": PIXELY}
    if btnU.value() == 0:
        coords["y"] -= 1
    if btnD.value() == 0:
        coords["y"] += 1
    coords = checkCoord(pixelPos)
    oled.pixel(coords["x"], coords["y"], 1)
    oled.show()
    coords["x"] += 1
    
    return coords


btnD = Pin(9, Pin.IN, Pin.PULL_UP)
btnU = Pin(7, Pin.IN, Pin.PULL_UP)
btnR = Pin(8, Pin.IN, Pin.PULL_UP)

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)

# First pixel coordinates
pixelPos = {"x": PIXELX, "y": PIXELY}

while True:
    pixelPos = updatePixel(oled, pixelPos, btnD, btnU, btnR)
    sleep_ms(10)
    