############################################################
#
#   音のデータを生成する基底クラス
#
############################################################
#

from SoundBase import SoundBase


class SoundSrc(SoundBase):
    def __init__(self):
        super().__init__()
        self.data = None

    def get_data(self):
        print(len(self.data))
        return self.data
