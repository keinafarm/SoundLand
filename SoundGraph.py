# https://tam5917.hatenablog.com/entry/2019/04/28/130641
# https://watlab-blog.com/2019/05/21/pyaudio-install/
#  PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl

############################################################
#
#   波形を表示する
#
############################################################
#

import sys
import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui


class SoundGraph:
    def __init__(self):
        """
        波形の表示
        """
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle(u"波形のリアルタイムプロット")
        self.win.resize(1100, 800)
        self.plt = self.win.addPlot()  # プロットのビジュアル関係
        self.plt.setYRange(-1.0, 1.0)  # y軸の上限、下限の設定
        self.curve = self.plt.plot()  # プロットデータを入れる場所

        self.sound_source = None

    def set_sound(self, source):
        """
        波形データの入力元をセットする
        :param source:波形データの入力元
        :return:
        """
        self.sound_source = source

    def update(self):
        """
        表示を更新する
        :return:
        """
        data = self.sound_source.get_data()
        data = np.frombuffer(data, dtype="int16") / 32768

        self.curve.setData(data)


if __name__ == "__main__":
    from SrcSin import SrcSin
    from SrcMic import SrcMic
    from SoundOut import SoundOut

    plot_window = SoundGraph()
    sound_out = SoundOut()
    sound_source = SrcMic()

    #    sound_source = SrcSin()
    #    sound_source.set_frequency(440)
    #    sound_source.set_volume(0.5)

    plot_window.set_sound(sound_source)
    sound_out.set_sound(sound_source)


    def update():
        #        sound_source.update()
        plot_window.update()


    #       sound_out.update()

    timer = QtCore.QTimer()
    # アップデート時間設定
    timer.timeout.connect(update)
    timer.start(63)  # 5mSec

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
