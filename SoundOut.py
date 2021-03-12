############################################################
#
#   出力先の抽象クラス
#
############################################################
#

from SoundBase import SoundBase
from abc import abstractmethod


class SoundOut(SoundBase):
    def __init__(self):
        """
        音データ生成クラスの基底クラス
        """
        super().__init__()
        self.data = None

    def set_sound(self, source):
        """
        波形データの入力元をセットする
        :param source:波形データの入力元
        :return:
        """
        self.sound_source = source
