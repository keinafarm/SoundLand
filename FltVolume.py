############################################################
#
#   ボォリュームコントロール
#
############################################################
#

from SoundFilter import SoundFilter
import numpy as np


class FltVolume(SoundFilter):
    def __init__(self):
        super().__init__()
        self.value = 1.0

    def update(self, *args):
        """
        データを更新する
        :return:
        """
        self.sound_source.update()
        data = self.sound_source.get_data() * self.value
        self.data = np.array(data, dtype="int16")

    def set_volume(self, value):
        self.value = value
