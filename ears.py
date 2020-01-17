from threading import Thread
import cognition
from time import sleep
import pyaudio

class Ears:
    def __init__(self, elements=[]):
        self.elements = elements
        self.create_ears()

    def create_ears(self):
        self.listening_thread = ListeningThread('sophia.pmdl',
                                                self.detected_callback)


    def detected_callback(self):
        self.listening_thread.interrupted = True
        self.listening_thread.stop()
        sleep(0.1)

        command = cognition.listen_to_command()
        print("[SOFI]: Sofia recognized: " + command)
        for element in self.elements:
            if command.upper() in (vt.upper() for vt in
                                   element.voice_triggers):
                element.voice_event()

        self.create_ears()
        self.listen()

    def listen(self):
        """Sofia starts listening"""
        self.listening_thread.start()


class ListeningThread(Thread):
    CHANNELS = 4
    RATE = 44100
    FORMAT = pyaudio.paInt16

    def __init__(self, model, detected_callback, sensitivity=0.5):
        Thread.__init__(self)

        self.interrupted = False
        self.detected_callback = detected_callback
        self.model = model
        self.sensitivity = sensitivity

        self.detector = snowboydecoder.HotwordDetector(self.model,
                                                       sensitivity=self.sensitivity)

    def run(self):
        self.detector.start(
            detected_callback=self.detected_callback,
            interrupt_check=lambda: self.interrupted,
            sleep_time=0.03
        )

    def stop(self):
        self.detector.terminate()
