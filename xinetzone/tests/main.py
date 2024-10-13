import cv2
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Slot, Signal, QObject


class EditorScene(QtWidgets.QGraphicsScene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 一些关于网格背景的设置
        self.setBackgroundBrush(QtGui.QColor(0, 0, 200, 100))  # 背景颜色
        # # self.font = QtGui.QFont("华文琥珀", 20)
        # # self.addText("Hello, world!", self.font) 
        # self.photo = QtGui.QImage(r"C:\Users\xinzo\Desktop\study\color_mapping\image_side\1.JPG")
        # # 添加矩形
        # self.pen = QtGui.QPen()
        # self.pen.setColor(QtGui.QColor('blue'))
        # self.pen.setWidth(3)
        # self.brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        # self.brush.setColor(QtGui.QColor('yellow'))
        # rect = QtCore.QRectF(130, 130, 100, 150)
        # x, y = 30, 30
        # w, h = 100, 100
        # self.addRect(x, y, w, h, self.pen, self.brush)  # 添加矩形图元--方式一
        # self.addRect(rect, self.pen, self.brush)  # 添加矩形图元--方式二
        # self.addEllipse(200, 250, 12, 12, self.pen, self.brush)  # 可塑性矩形

        # rect = QtCore.QRectF(10, 10, 100, 100)
        # item1 = QtWidgets.QGraphicsRectItem(rect)  # 创建矩形---以场景为坐标
        # self.addItem(item1)

    # def drawBackground(self, painter, rect):
    #     painter.drawImage(0, 0, self.photo)
    #     super().drawBackground(painter, rect)


class GraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设定视图尺寸
        # self.resize(600, 600)
        # 创建场景
        self.scene = EditorScene()
        # self.move(0, 0) # 移动视口到左上角

        # 设定视图的场景
        self.setScene(self.scene)
        self.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.ViewportUpdateMode.FullViewportUpdate) # 消除重影 移动重影
        self.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)  # 设置可以进行鼠标的拖拽选择
        # 这里是左上角方式显示
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

class Window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.setWindowTitle("ROI操作")
        image_path = r"C:\Users\xinzo\Desktop\study\color_mapping\image_side\1.JPG"
        self.view = GraphicsView()
        # self.frame.update_frame(cv2.imread(image_path))
        self.setCentralWidget(self.view)
        self.lastPoint = QtCore.QPoint()
        self.endPoint = QtCore.QPoint()
        # 标志是否正在绘图
        self.isDrawing = False

    def mousePressEvent(self, event):
        # 鼠标左键按下
        if event.button() == QtCore.Qt.LeftButton:
            self.lastPoint = event.position()
            self.endPoint = self.lastPoint
            self.isDrawing = True
        print(event.position())

    def mouseReleaseEvent(self, event):
        # 鼠标左键释放
        if event.button() == QtCore.Qt.LeftButton:
            self.endPoint = event.position()
            # 进行重新绘制
            self.update()
            self.isDrawing = False

    # def paintEvent(self, event):
    #     painter = QtGui.QPainter(self)
    #     x = self.lastPoint.x()
    #     y = self.lastPoint.y()
    #     w = self.endPoint.x() - x
    #     h = self.endPoint.y() - y

    #     # 如果正在绘图，就在辅助画布上绘制
    #     if self.isDrawing:
    #         # 将以前pix中的内容复制到tempPix中，保证以前的内容不消失
    #         self.frame.tempPix = self.frame.pix_map
    #         pp = QtGui.QPainter(self.frame.tempPix)
    #         pp.drawRect(x, y, w, h)
    #         painter.drawPixmap(0, 0, self.frame.tempPix)
    #     else:
    #         pp = QtGui.QPainter(self.frame.pix_map)
    #         pp.drawRect(x, y, w, h)
    #         painter.drawPixmap(0, 0, self.frame.pix_map)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    win = Window()
    # win = GraphicsView()
    win.show()
    sys.exit(app.exec())