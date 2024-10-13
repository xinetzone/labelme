from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Slot, Signal, QObject
from rect import RectItem

class EditorScene(QtWidgets.QGraphicsScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 一些关于网格背景的设置
        self.setBackgroundBrush(QtGui.QColor(0, 0, 200, 100))  # 背景颜色
        self.photo = QtGui.QImage(r"C:\Users\xinzo\Desktop\study\color_mapping\image_side\1.JPG")

    def drawBackground(self, painter, rect):
        painter.drawImage(0, 0, self.photo)
        super().drawBackground(painter, rect)


class MainWindow(QtWidgets.QGraphicsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设定视图尺寸
        #self.resize(600, 600)
        # 创建场景
        self.scene = EditorScene()

        # x1, y1, w, h
        self.item = RectItem(20, 25, 120, 120)  # 可塑性矩形
        self.scene.addItem(self.item)
        self.scene.addItem(RectItem(200, 250, 120, 120))
        # self.item = QtWidgets.QGraphicsEllipseItem(20, 25, 120, 120)
        # self.scene.addItem(self.item) 

        # 设定视图的场景
        self.setScene(self.scene)
        self.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.ViewportUpdateMode.FullViewportUpdate) # 消除重影 移动重影
        self.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)  # 设置可以进行鼠标的拖拽选择
        # 这里是左上角方式显示
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec())