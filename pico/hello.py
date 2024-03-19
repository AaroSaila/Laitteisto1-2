from machine import Pin, I2C
import ssd1306
from time import sleep_ms

# Initial position of UFO
INITX = 52
INITY = 56
# Screen dimensions
SCREENW = 128
SCREENH = 64


class movingText:
    def __init__(self, text, oled):
        self.x = INITX
        self.y = INITY
        self.text = text
        self.oled = oled
        self.size = (len(self.text) * 8 + 1, 8)
        self.borders = (SCREENW - self.size[0], SCREENH - self.size[1])
    
    def spawn(self):
        self.oled.fill(0)
        self.oled.text(self.text, self.x, self.y)
        self.oled.show()
        
    def checkBorderX(self):
        if self.x < 1 or self.x > self.borders[0]:
            return True
    
    def checkBorderY(self):
        if self.y < 1 or self.y > self.borders[1]:
            return True
    
    def move(self, moveX, moveY):
        moved = False
        self.oled.fill(0)
        if self.x + moveX < self.borders[0] and self.x + moveX > 1:
            self.x += moveX
            moved = True
        if self.y + moveY < self.borders[1] and self.y + moveY > 1:
            self.y += moveY
            moved = True
        self.oled.text(self.text, self.x, self.y)
        self.oled.show()
        return moved


class Ufo(movingText):
    def __init__(self, btnL, btnR, oled):
        super().__init__("<=>", oled)
        self.btnL = btnL
        self.btnR = btnR
    
    def execute(self):
        self.right()
        self.left()
    
    def right(self):
        if self.btnR.value() == 0:
            moving = True
            while moving:
                if self.move(1, 0) is False:
                    moving = False
                if otherButtonPressed(btnR):
                    moving = False
    
    def left(self):
        if btnL.value() == 0:
            moving = True
            while moving:
                if self.move(-1, 0) is False:
                    moving = False
                if otherButtonPressed(btnL):
                    moving = False


def otherButtonPressed(currentButton):
    for btn in btns:
        if btn != currentButton and btn.value() == 0:
            return True
    return False


i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = ssd1306.SSD1306_I2C(SCREENW, SCREENH, i2c)
btnL = Pin(7, Pin.IN, Pin.PULL_UP)
btnR = Pin(9, Pin.IN, Pin.PULL_UP)
btns = (btnL, btnR)

ufo = Ufo(btnL, btnR, oled)
ufo.spawn()

while True:
    ufo.execute()
    sleep_ms(50)
