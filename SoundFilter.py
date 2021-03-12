############################################################
#
#   音データ変換の抽象クラス
#
############################################################
#

from SoundOut import SoundOut
from SoundSrc import SoundSrc

from abc import abstractmethod


class SoundFilter(SoundOut, SoundSrc):
    def __init__(self):
        super().__init__()

    def output(self, *args):
        pass

    @abstractmethod
    def update(self, *args):
        """
        データを更新する(仮想関数)
        :return:
        """
        pass
