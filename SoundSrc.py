############################################################
#
#   音データ生成クラスの基底クラス
#
############################################################
#

from SoundBase import SoundBase
from abc import abstractmethod


class SoundSrc(SoundBase):
    def __init__(self):
        """
        音データ生成クラスの基底クラス
        """
        super().__init__()
        self.data = None

    @abstractmethod
    def get_data(self):
        """
        波形データを得る
        :return:波形データ(np.ndarray:int16)
        """
#        print(len(self.data))
        return self.data

    @abstractmethod
    def update(self):
        """
        データを更新する(仮想関数)
        :return:
        """
        pass