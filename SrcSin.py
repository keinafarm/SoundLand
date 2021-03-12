from SoundSrc import SoundSrc
import numpy as np

class SrcSin(SoundSrc):

    def __init__(self):
        super().__init__()
        self.data = np.zeros(self.CHUNK)
        self.set_frequency(440)

    def set_frequency(self, frequency):
        self.frequency = float(frequency)
#        self.angle = self.frequency/self.RATE * np.pi * 2

        # 周波数に対するサンプル数
        samples = float(self.RATE) / self.frequency
        # １サンプル分の角度
        self.angle = np.pi * 2 / samples
        print("angle={0}".format(self.angle))
        self.start = 0.0

    def set_volume(self, volume):
        self.volume = volume

    def update(self):
        angle = [ self.start+(i*self.angle) for i in range(self.CHUNK) ]
        data = np.sin( angle ) * 32767.0 * self.volume
        self.data = np.array(data, dtype="int16")

        self.start = self.start+(self.CHUNK*self.angle)
        print("self.start={0}".format(self.start))
        if self.start > 2*np.pi:
            a = int(self.start / (2 * np.pi))
            self.start =  self.start - (a * 2*np.pi)
