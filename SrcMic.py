############################################################
#
#   マイクからの音を出力するクラス
#
############################################################
#

# https://tam5917.hatenablog.com/entry/2019/04/28/130641
# https://watlab-blog.com/2019/05/21/pyaudio-install/
#  PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl

from SoundSrc import SoundSrc

import numpy as np
import pyaudio


class SrcMic(SoundSrc):

    def __init__(self):
        super().__init__()
        # マイク設定
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=self.RATE,
                                      input=True,
                                      output=False,
                                      frames_per_buffer=self.CHUNK)

        self.data = np.zeros(self.CHUNK)
        self.raw = np.zeros(self.CHUNK)

    def update(self):
        data = self.stream.read(self.CHUNK)
        self.data = np.frombuffer(data, dtype="int16")
        self.data = self.data / 32767.0
        print("mic={0}".format(len(self.data)))
