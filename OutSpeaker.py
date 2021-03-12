############################################################
#
#   音を出力する
#
############################################################
#

# https://www.wizard-notes.com/entry/python/pyaudio-recplay
import pyaudio
from SoundOut import SoundOut

# https://people.csail.mit.edu/hubert/pyaudio/docs/

class OutSpeaker(SoundOut):

    def __init__(self):
        """
        音声出力
        """
        super().__init__()
        self.audio = pyaudio.PyAudio()
        self.sound_source = None
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=self.RATE,
                                      input=False,
                                      output=True,
                                      frames_per_buffer=self.CHUNK,
                                      stream_callback=self.output)

    def set_sound(self, sound_source):
        """
        出力する音のオブジェクトを指定する
        :param sound_source:
        :return:
        """
        self.sound_source = sound_source
        self.stream.start_stream()

    def output(self, in_data, frame_count, time_info, status):
        self.sound_source.update()
        data = self.sound_source.get_data()
        print("out2={0}".format(len(data)))
        return data, pyaudio.paContinue
