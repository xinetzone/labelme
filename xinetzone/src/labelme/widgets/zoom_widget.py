from ..qt_utils import QtCore, QtGui, QtWidgets
from .. import QT6

class ZoomWidget(QtWidgets.QSpinBox):
    def __init__(self, value=100):
        super(ZoomWidget, self).__init__()
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.setRange(1, 1000)
        self.setSuffix(" %")
        self.setValue(value)
        self.setToolTip("Zoom Level")
        self.setStatusTip(self.toolTip())
        self.setAlignment(QtCore.Qt.AlignCenter)

    def minimumSizeHint(self):
        height = super(ZoomWidget, self).minimumSizeHint().height()
        fm = QtGui.QFontMetrics(self.font())
        if QT6:
            rect = fm.boundingRect(str(self.maximum()))
            width = rect.width()
        else:
            width = fm.width(str(self.maximum()))
        return QtCore.QSize(width, height)
