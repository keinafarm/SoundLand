############################################################
#
#   sin波を出力する
#
############################################################
#

from SoundSrc import SoundSrc
import numpy as np


class SrcSin(SoundSrc):

    def __init__(self):
        """
        sin波を出力する
        """
        super().__init__()
        self.data = np.zeros(self.CHUNK)
        self.frequency = 0.0
        self.angle = 0.0
        self.start = 0.0
        self.volume = 1.0

    def set_frequency(self, frequency):
        """
        周波数をセットする
        :param frequency: 周波数(Hz)
        :return:
        """
        self.frequency = float(frequency)
        #        self.angle = self.frequency/self.RATE * np.pi * 2

        samples = float(self.RATE) / self.frequency         # 周波数に対するサンプル数
        self.angle = np.pi * 2 / samples                    # １サンプル分の角度
        print("angle={0}".format(self.angle))
        self.start = 0.0

    def set_volume(self, volume):
        """
        ボリュームをセットする
        :param volume: 音量（0 ~ 1までの値）
        :return:
        """
        self.volume = volume

    def update(self):
        """
        波形データを生成する
        :return:
        """
        angle = [self.start + (i * self.angle) for i in range(self.CHUNK)]  # sin関数に入力する、角度値の配列
        data = np.sin(angle) * self.volume                                  # -32767～32767までの数値に変換
        self.data = np.array(data, dtype="float64")                         # 型をint16に変換(Mic入力フォーマットに合わせる）

        self.start = self.start + (self.CHUNK * self.angle)                 # 次の角度を演算
        print("self.start={0}".format(self.start))
        if self.start > 2 * np.pi:                                          # 2πを超えていたら
            a = int(self.start / (2 * np.pi))                               # 2π以内に収まるように、角度を補正する
            self.start = self.start - (a * 2 * np.pi)

        print("sin.update={0}".format(self.data[0]))
