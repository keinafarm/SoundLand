import numpy as np
from SoundBase import SoundBase

class SoundSrc(SoundBase):
    def __init__(self):
        super().__init__()

    def get_data(self):
        return self.data
