#https://www.wizard-notes.com/entry/python/pyaudio-recplay
import pyaudio
from SoundBase import SoundBase
# https://people.csail.mit.edu/hubert/pyaudio/docs/

class SoundOut(SoundBase):

    def __init__(self):
        super().__init__()
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=self.RATE,
                                      input=False,
                                      output=True,
                                      frames_per_buffer=self.CHUNK)

    def set_sound(self, sound_source):
        self.sound_source = sound_source

    def update(self):
        data = self.sound_source.get_data()
        self.stream.write(data)
