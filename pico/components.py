from machine import Pin, I2C
import ssd1306


# Screen dimensions
SCREENW = 128
SCREENH = 64


class LED:
    def __init__(self, pin):
        self.pin = pin
        self.PWM = PWM(Pin(pin))
        self.PWM.freq(1000)
        self.on_brightness = 100
        self.current_brightness = 0
        
    def brightness(self, duty):
        self.PWM.duty_u16(duty)
        
    def toggle(self):
        if self.current_brightness == self.on_brightness:
            self.current_brightness = 0
            self.brightness(self.current_brightness)
        else:
            self.current_brightness = self.on_brightness
            self.brightness(self.current_brightness)
    
    def off(self):
        self.current_brightness = 0
        self.brightness(self.current_brightness)
    
    def on(self):
        self.current_brightness = self.on_brightness
        self.brightness(self.current_brightness)
        

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

sw00 = Pin(9, Pin.IN, Pin.PULL_UP)
sw02 = Pin(7, Pin.IN, Pin.PULL_UP)

D1 = LED(22)
D2 = LED(21)
D3 = LED(20)

knob = Pin(12, Pin.IN, Pin.PULL_UP)
