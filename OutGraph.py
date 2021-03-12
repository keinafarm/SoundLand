# https://tam5917.hatenablog.com/entry/2019/04/28/130641
# https://watlab-blog.com/2019/05/21/pyaudio-install/
#  PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl

############################################################
#
#   波形を表示する
#
############################################################
#

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from SoundOut import SoundOut


class OutGraph(SoundOut):
    def __init__(self):
        """
        波形の表示
        """
        super().__init__()
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle(u"波形のリアルタイムプロット")
        self.win.resize(1100, 800)
        self.plt = self.win.addPlot()  # プロットのビジュアル関係
        self.plt.setYRange(-1.0, 1.0)  # y軸の上限、下限の設定
        self.curve = self.plt.plot()  # プロットデータを入れる場所

        self.sound_source = None
        self.timer = QtCore.QTimer()
        # アップデート時間設定
        self.timer.timeout.connect(self.output)
        self.timer.start(63)  # 5mSec

    def set_sound(self, sound_source):
        """
        出力する音のオブジェクトを指定する
        :param sound_source:
        :return:
        """
        super().set_sound(sound_source)

    def output(self, *args):
        """
        表示を更新する
        :return:
        """
        data = self.sound_source.get_data()

        self.curve.setData(data)
