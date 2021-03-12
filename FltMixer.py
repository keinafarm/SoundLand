############################################################
#
#   サウンドミキサー
#
############################################################
#
from SoundFilter import SoundFilter
import numpy as np


class FltMixer(SoundFilter):
    def __init__(self):
        super().__init__()
        self.sound_source = []

    def set_sound(self, source):
        """
        波形データの入力元をセットする
        :param source:波形データの入力元
        :return:
        """
        self.sound_source.append(source)

    def remove_sound(self, source):
        """
        指定した波形データの入力元を削除する
        :param source:波形データの入力元
        :return:
        """
        self.sound_source.remove(source)

    def update(self, *args):
        """
        データを合成する
        :return:
        """
        data_sum = np.zeros(self.CHUNK)
        for sound in self.sound_source:
            sound.update()
            data = sound.get_data()
            print("data[0]={0}".format(data[0]))
            data_sum = data_sum + data

        print("mixer.update")
        print("data_sum[0]={0}".format(data_sum[0]))
        self.data = np.array(data_sum, dtype="int16")
