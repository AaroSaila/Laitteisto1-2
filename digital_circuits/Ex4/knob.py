from machine import Pin, PWM
from time import sleep_ms, sleep

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


def knob_cycle():
    i = 0
    while True:
        if knob.value() == 0:
            i += 1
            if i > 7:
                i = 0
            print(f"Decimal {i}")
            sleep_ms(200)
        if i == 0:
            D1.off()
            D2.off()
            D3.off()
        if i == 1:
            D1.on()
            D2.off()
            D3.off()
        if i == 2:
            D1.off()
            D2.on()
            D3.off()
        if i == 3:
            D1.on()
            D2.on()
            D3.off()
        if i == 4:
            D1.off()
            D2.off()
            D3.on()
        if i == 5:
            D1.on()
            D2.off()
            D3.on()
        if i == 6:
            D1.off()
            D2.on()
            D3.on()
        if i == 7:
            D1.on()
            D2.on()
            D3.on()
        

knob = Pin(12, Pin.IN, Pin.PULL_UP)
D1 = LED(22)
D2 = LED(21)
D3 = LED(20)

knob_cycle()