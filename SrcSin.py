from SoundSrc import SoundSrc
import numpy as np

class SrcSin(SoundSrc):

    def __init__(self):
        super().__init__()
        self.data = np.zeros(self.CHUNK)
        self.set_frequency(440)

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.angle = self.frequency/self.RATE * np.pi * 2
        self.start = 0

    def set_volume(self, volume):
        self.volume = volume

    def update(self):
        angle = np.arange( self.start, self.start + self.angle*self.CHUNK, self.angle )
        self.data = np.sin( angle ) * self.volume

        self.start += self.CHUNK
        if self.start > 2*np.pi:
            self.start -= 2*np.pi
