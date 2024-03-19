from machine import Pin, I2C
import ssd1306


i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

sw02 = Pin(7, Pin.IN, Pin.PULL_UP)