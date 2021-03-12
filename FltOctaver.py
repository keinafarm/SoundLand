############################################################
#
#   オクターバー
#
############################################################
#
from SoundFilter import SoundFilter
import numpy as np

class   FiltOctaver(SoundFilter):
    def __init__(self):
        super().__init__()

    def update(self, *args):
        """
        データを更新する
        :return:
        """
        self.sound_source.update()
        self.data = np.abs(self.sound_source.get_data())
