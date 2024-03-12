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
        
    def off(self):
        self.light_off()
        if self.btn.value() == 0:
            self.state = self.onw
    
    def onw(self):
        self.light_on()
        if self.btn.value() == 1:
            self.state = self.on
            
    def on(self):
        self.light_on()
        if self.btn.value() == 0:
            self.state = self.offw
    
    def offw(self):
        self.light_off()
        if self.btn.value() == 1:
            self.state = self.off
  
    def light_off(self):
        self.pwm.duty_u16(0)
    
    def light_on(self):
        self.pwm.duty_u16(self.on_brightness)


btn = Pin(7, mode=Pin.IN, pull=Pin.PULL_UP)
lamp = Light(20, btn)

while True:
    lamp.execute()
    print(btn.value())
    sleep_ms(lamp.clock)