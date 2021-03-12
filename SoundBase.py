############################################################
#
#   音の基底クラス
#
############################################################
#

class SoundBase:
    sample_rate = 16000
    frame_length = 1024

    def __init__(self):
        self.CHUNK = SoundBase.frame_length  # 1度に読み取る音声のデータ幅
        self.RATE = SoundBase.sample_rate  # サンプリング周波数
