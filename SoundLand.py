from OutGraph import OutGraph
from SrcSin import SrcSin
from SrcMic import SrcMic
from OutSpeaker import OutSpeaker
from pyqtgraph.Qt import QtCore, QtGui
import sys
from FltVolume import FltVolume
from FltMixer import FltMixer

plot_window = OutGraph()
sound_out = OutSpeaker()
volume = FltVolume()
mixer = FltMixer()

sound_source = SrcMic()
#mixer.set_sound(sound_source)

sound_source0 = SrcSin()
sound_source0.set_frequency(440)
sound_source1 = FltVolume()
sound_source1.set_sound(sound_source0)
sound_source1.set_volume(0.3)
mixer.set_sound(sound_source1)

sound_source2 = SrcSin()
sound_source2.set_frequency(660)
sound_source4 = FltVolume()
sound_source4.set_sound(sound_source2)
sound_source4.set_volume(0.3)

mixer.set_sound(sound_source4)

sound_source3 = SrcSin()
sound_source3.set_frequency(880)
sound_source5 = FltVolume()
sound_source5.set_sound(sound_source3)
sound_source5.set_volume(0.3)

mixer.set_sound(sound_source5)

volume.set_sound(mixer)
volume.set_volume(0.8)

plot_window.set_sound(volume)
sound_out.set_sound(volume)

if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    QtGui.QApplication.instance().exec_()
