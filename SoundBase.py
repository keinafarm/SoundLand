############################################################
#
#   音の抽象クラス
#   https://qiita.com/bluepost59/items/eef6f48fdd322b0b9791
#
############################################################
#
from abc import ABCMeta


class SoundBase(metaclass=ABCMeta):
    sample_rate = 16000
    frame_length = 1024

    def __init__(self):
        """
        音の基底クラス
        """
        self.CHUNK = SoundBase.frame_length  # 1度に読み取る音声のデータ幅
        self.RATE = SoundBase.sample_rate  # サンプリング周波数
