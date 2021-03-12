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
                                      frames_per_buffer=self.CHUNK,
                                      stream_callback=self.callback)

    def set_sound(self, sound_source):
        self.sound_source = sound_source
        self.stream.start_stream()

    def update(self):
        data = self.sound_source.get_data()
        print("out1={0}".format(len(data)))
        self.stream.write(data)

    def callback(self, in_data, frame_count, time_info, status):
        self.sound_source.update()
        data = self.sound_source.get_data()
        print("out2={0}".format(len(data)))
        return (data, pyaudio.paContinue)
