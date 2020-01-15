#!/usr/bin/env python3

import socket
import R64.GPIO as GPIO
import sys
from Server import Server
from light import Light
from ears import Ears
import signal

# Set up GPIO
GPIO.setmode(GPIO.BOARD)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

marko_light = Light(0, "Marko's Light", 8, voice_triggers=[
    "Switch Light 1",
    "Switch Light One"
])

maxim_light = Light(1, "Maxim's Light", 10, voice_triggers=[
    "Switch Light 2",
    "Switch Light Two",
    "Switch Light Too",
    "Switch Light To"
])

night_light = Light(2, "Night Light", 7, voice_triggers=[
    "Switch Night Light"
])

server = Server([marko_light, night_light, maxim_light])
ears = Ears([marko_light, night_light, maxim_light])

server.start()
ears.listen()

GPIO.cleanup()
