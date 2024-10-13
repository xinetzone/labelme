from PySide6 import QtWidgets, QtCore, QtGui
print(QtWidgets)

class ImageView(QtWidgets.QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 载入图片
        imageLabel = QtWidgets.QLabel(self)
        image = QtGui.QPixmap(r"C:\Users\xinzo\Desktop\study\color_mapping\image_side\1.JPG")
        imageLabel.setPixmap(image)
        # 设定滚动条组件
        self.setBackgroundRole(QtGui.QPalette.Dark)
        self.setWidget(imageLabel)
        # 初始化设定
        self.init_Ui()

    def init_Ui(self):
        # 修改窗口默认尺寸
        self.resize(500, 500)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    win = ImageView()
    win.show()
    sys.exit(app.exec())