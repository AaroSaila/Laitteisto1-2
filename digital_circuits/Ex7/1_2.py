from machine import Pin, PWM
from time import sleep_ms


CLOCK = 50


class Led:
    def __init__(self, pin):
        self.led = Pin(pin, Pin.OUT)
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(1000)
        self.duty = 100
        
    def off(self):
        self.pwm.duty_u16(0)
    
    def on(self):
        self.pwm.duty_u16(self.duty)


class System:
    def __init__(self, lamp, siren, btn, alarmSwitch):
        self.lamp = lamp
        self.siren = siren
        self.btn = btn
        self.alarmSw = alarmSwitch
        self.state = self.init
        self.alarm = False
    
    def execute(self):
        self.state()
        
    def reset(self):
        self.state = self.init
        
    def allOff(self):
        self.lamp.off()
        self.siren.off()
    
    def checkAlarm(self):
        if self.alarm == False and self.alarmSw.value() == 0:
            self.alarm = True
            pressedDown(self.alarmSw)
        elif self.alarm == True and self.alarmSw.value() == 0:
            self.alarm = False
            pressedDown(self.alarmSw)
    
    def init(self):
        self.allOff()
        self.checkAlarm()
        if self.alarm == True:
            self.state = self.lampAndSiren
        #print("init")
    
    def lampAndSiren(self):
        self.lamp.on()
        self.siren.on()
        self.checkAlarm()
        if self.alarm == True and self.btn.value() == 0:
            self.state = self.lampOnly
            pressedDown(self.btn)
        elif self.alarm == False:
            self.state = self.lampOnly2
        #print("ls")
    
    def lampOnly(self):
        self.lamp.on()
        self.state = self.off
        
    def lampOnly2(self):
        self.lamp.on()
        self.siren.off()
        if self.btn.value() == 0:
            self.reset()
            pressedDown(self.btn)
        #print("l2")
    
    def off(self):
        self.allOff()
        self.checkAlarm()
        if self.alarm == True:
            self.state = self.lampOnly
        elif self.alarm == False:
            self.reset()
        #print("off")


def pressedDown(btn):
    while btn.value() == 0:
        pass


button = Pin(7, Pin.IN, Pin.PULL_UP)
alarmSwitch = Pin(9, Pin.IN, Pin.PULL_UP)
redLamp = Led(22)
siren = Led(20)
system = System(redLamp, siren, button, alarmSwitch)

while True:
    system.execute()
    sleep_ms(CLOCK)