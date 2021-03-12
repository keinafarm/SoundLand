############################################################
#
#   出力先の抽象クラス
#
############################################################
#

from SoundBase import SoundBase
from abc import abstractmethod
import numpy as np

class SoundOut(SoundBase):
    def __init__(self):
        """
        音データ生成クラスの基底クラス
        """
        super().__init__()
        self.sound_source = None
        self.data = np.zeros(self.CHUNK, dtype="int16")

    def set_sound(self, source):
        """
        波形データの入力元をセットする
        :param source:波形データの入力元
        :return:
        """
        self.sound_source = source

    @abstractmethod
    def output(self, *args):
        pass
