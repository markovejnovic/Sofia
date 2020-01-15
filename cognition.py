import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import snack
import os, random

def listen_to_command():
    sample_rate = 16000
    chunk_size = 2048

    r = sr.Recognizer()

    for i, mic_name in enumerate(sr.Microphone.list_microphone_names()):
        print str(i) + " " + mic_name

    with sr.Microphone(device_index=0, sample_rate=sample_rate,
                       chunk_size = chunk_size) as source:
        r.adjust_for_ambient_noise(source)

        song = AudioSegment.from_wav(os.path.join('res', 'listening',
            random.choice(os.listdir(os.path.join('res', 'listening')))))
        play(song)

        print('Sofia said what she was supposed to say')

        audio = r.listen(source)
        print('Sofia listened. Now sending to google.')
        try:
            text = r.recognize_google(audio)
	except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            text = ""
	except sr.RequestError as e:
            print("Could not request results from Google " +\
                  "Speech Recognition service; {0}".format(e))
            text = ""

    return text
