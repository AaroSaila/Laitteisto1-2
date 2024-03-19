from machine import Pin, I2C
import ssd1306
from time import sleep_ms

# Initial position of UFO
INITX = 52
INITY = 56
# Screen dimensions
SCREENW = 128
SCREENH = 64


class textBlock:
    def __init__(self, text, oled, x, y):
        self.x = x
        self.y = y
        self.text = text
        self.oled = oled
        self.size = (len(self.text) * 8, 8)
        self.borders = (SCREENW - self.size[0], SCREENH - self.size[1])
    
    def spawn(self):
        self.oled.fill(0)
        self.oled.text(self.text, self.x, self.y)
        self.oled.show()
    
    def move(self, moveX, moveY):
        moved = False
        self.oled.fill(0)
        if self.x + moveX < self.borders[0] and self.x + moveX >= 0:
            self.x += moveX
            moved = True
        if self.y + moveY < self.borders[1] and self.y + moveY >= 1:
            self.y += moveY
            moved = True
        self.oled.text(self.text, self.x, self.y)
        self.oled.show()
        return moved


class Ufo(textBlock):
    def __init__(self, btnL, btnR, btnU, btnD, oled, x, y):
        super().__init__("<=>", oled, x, y)
        self.btnL = btnL
        self.btnR = btnR
        self.btnU = btnU
        self.btnD = btnD
    
    def execute(self):
        self.right()
        self.left()
        self.up()
        self.down()
    
    def otherButtonPressed(self, currentBtn):
        for btn in btns:
            if btn != currentBtn and btn.value() == 0:
                return True
            return False
        
    def setInMotion(self, btn, x, y):
        if btn.value() == 0:
            moving = True
            while moving:
                if self.move(x, y) is False:
                    moving = False
                if otherButtonPressed(btn):
                    moving = False
    
    def right(self):
        self.setInMotion(self.btnR, 1, 0)
    
    def left(self):
        self.setInMotion(self.btnL, -1, 0)
    
    def up(self):
        self.setInMotion(self.btnU, 0, -1)
    
    def down(self):
        self.setInMotion(self.btnD, 0, 1)


def otherButtonPressed(currentButton):
    for btn in btns:
        if btn != currentButton and btn.value() == 0:
            return True
    return False


i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = ssd1306.SSD1306_I2C(SCREENW, SCREENH, i2c)
btnL = Pin(7, Pin.IN, Pin.PULL_UP)
btnU = Pin(8, Pin.IN, Pin.PULL_UP)
btnR = Pin(9, Pin.IN, Pin.PULL_UP)
btnD = Pin(12, Pin.IN, Pin.PULL_UP)
btns = (btnL, btnU, btnR, btnD)

ufo = Ufo(btnL, btnR, btnU, btnD, oled, INITX, INITY)
ufo.spawn()

while True:
    ufo.execute()
    sleep_ms(50)
