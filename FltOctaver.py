############################################################
#
#   オクターバー
#
############################################################
#
from SoundFilter import SoundFilter
import numpy as np


class FiltOctaver(SoundFilter):
    def __init__(self):
        super().__init__()

    def update(self, *args):
        """
        データを更新する
        :return:
        """
        self.sound_source.update()
        data = np.abs(self.sound_source.get_data())
        average = np.average(data)
        data = data * 2  # 2倍にして平均値分下げる
        self.data = data - average
