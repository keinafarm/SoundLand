import numpy as np

class SoundSrc:
    sample_rate = 16000
    frame_length = 1024

    def __init__(self):
        # マイク設定
        self.CHUNK = SoundSrc.frame_length  # 1度に読み取る音声のデータ幅
        self.RATE = SoundSrc.sample_rate  # サンプリング周波数

        self.data = np.zeros(self.CHUNK)

    def get_data(self):
        pass
