from OutGraph import OutGraph
from SrcSin import SrcSin
from SrcMic import SrcMic
from OutSpeaker import OutSpeaker
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import sys

plot_window = OutGraph()
sound_out = OutSpeaker()
# sound_source = SrcMic()

sound_source = SrcSin()
sound_source.set_frequency(440)
sound_source.set_volume(0.5)

plot_window.set_sound(sound_source)
sound_out.set_sound(sound_source)


def update():
    #        sound_source.update()
    plot_window.callback()


#       sound_out.update()

timer = QtCore.QTimer()
# アップデート時間設定
timer.timeout.connect(update)
timer.start(63)  # 5mSec

if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    QtGui.QApplication.instance().exec_()
