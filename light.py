import R64.GPIO as GPIO
from Device import BinaryDevice

class Light(BinaryDevice):
    def __init__(self, id, name, pin,  voice_triggers=None, default=GPIO.LOW,
                 autodefault=True):
        BinaryDevice.__init__(self, id, name)
        self.pin = pin
        self.state = default
        self.voice_triggers = voice_triggers

        GPIO.setup(self.pin, GPIO.OUT)

        if autodefault:
            GPIO.output(self.pin, default)

    def server_event(self, event=None):
        self.toggle()

    def voice_event(self, event=None):
        self.toggle()

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def toggle(self):
        GPIO.setup(self.pin, GPIO.OUT) # I'm as confused as you are. The GPIO
                                       # library does not think I setup the pin
                                       # before. Oh well, guess the light takes
                                       # 4 times as much time to toggle.
        if self.state == GPIO.LOW:
            self.state = GPIO.HIGH
            GPIO.output(self.pin, self.state)
        else:
            self.state = GPIO.LOW
            GPIO.output(self.pin, self.state)

