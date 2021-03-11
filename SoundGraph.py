#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# https://tam5917.hatenablog.com/entry/2019/04/28/130641
# https://watlab-blog.com/2019/05/21/pyaudio-install/
#  PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl


import sys

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui


class SoundGraph:
    def __init__(self):
        self.win = pg.GraphicsWindow()
        self.win.setWindowTitle(u"波形のリアルタイムプロット")
        self.win.resize(1100, 800)
        self.plt = self.win.addPlot()  # プロットのビジュアル関係
        self.ymin = -100
        self.ymax = 80
        self.plt.setYRange(-1.0, 1.0)  # y軸の上限、下限の設定
        self.curve = self.plt.plot()  # プロットデータを入れる場所

        self.sound_source = None

    def set_sound(self, sound_source):
        self.sound_source = sound_source

    def update(self):
        data = self.sound_source.get_data()
        self.curve.setData(data)


if __name__ == "__main__":
    from SrcMic import SrcMic


    plotwin = SoundGraph()
    sound_source = SrcMic()
    plotwin.set_sound(sound_source)

    def update():
        sound_source.update()
        plotwin.update()

    timer = QtCore.QTimer()
    # アップデート時間設定
    timer.timeout.connect(update)
    timer.start(5)  # 5msec


    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()