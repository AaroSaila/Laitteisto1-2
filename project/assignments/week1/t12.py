from machine import Pin, I2C
import ssd1306
from time import sleep_ms


# Screen dimensions
SCREENW = 128
SCREENH = 64


class textBlock:
    textBlocks = []
    
    def __init__(self, text, oled, x, y):
        self.x = x
        self.y = y
        self.text = text
        self.oled = oled
        self.size = (len(self.text) * 8, 8)
        self.borders = (SCREENW - self.size[0], SCREENH - self.size[1])
        self.textBlocks.append(self)
        
    def spawn(self):
        self.oled.text(self.text, self.x, self.y)
    
    def move(self, moveX, moveY):
        self.x += moveX
        self.y += moveY
        self.oled.text(self.text, self.x, self.y)


def scrollingText():
    text = input()
    if textBlock.textBlocks:
        prevBlock = textBlock.textBlocks[-1]
        block = textBlock(text, oled, prevBlock.x, prevBlock.y + 8)
        if block.y > 56:
            del textBlock.textBlocks[0]
            oled.fill(0)
            for b in textBlock.textBlocks:
                b.move(0, -8)
        else:
            block.spawn()
    else:
        block = textBlock(text, oled, 0, 0)
        block.spawn()
    oled.show()


i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)

oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)

while True:
    scrollingText()
    sleep_ms(50)