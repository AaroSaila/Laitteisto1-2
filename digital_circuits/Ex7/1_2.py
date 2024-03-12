from machine import Pin, PWM
from time import sleep_ms


class Light:
    def __init__(self, pin, btn):
        self.btn = btn
        self.led = Pin(pin, Pin.OUT)
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(1000)
        self.on_brightness = 100
        self.state = self.off
        self.clock = 50
        
    def execute(self):
        self.state()