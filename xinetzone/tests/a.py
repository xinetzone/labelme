from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QPixmap, QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint

class ImageAnnotationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Annotation")
        self.setGeometry(100, 100, 800, 600)
        
        # 创建主布局
        layout = QVBoxLayout()
        
        # 加载图像
        self.image_label = QLabel(self)
        pixmap = QPixmap("path/to/your/image.jpg")
        self.image_label.setPixmap(pixmap)
        layout.addWidget(self.image_label)
        
        # 创建画笔用于绘制标注
        self.pen = QPen(Qt.red, 3)
        
        # 绑定鼠标事件
        self.image_label.mousePressEvent = self.mousePressEvent
        self.image_label.mouseMoveEvent = self.mouseMoveEvent
        self.image_label.mouseReleaseEvent = self.mouseReleaseEvent
        
        # 创建一个按钮用于清除标注
        clear_button = QPushButton("Clear", self)
        clear_button.clicked.connect(self.clearAnnotations)
        layout.addWidget(clear_button)
        
        # 设置主窗口的中心部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # 初始化变量
        self.last_point = None
        self.drawing = False
        self.annotations = []
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()
    
    def mouseMoveEvent(self, event):
        if self.drawing and self.last_point is not None:
            painter = QPainter(self.image_label.pixmap())
            painter.setPen(self.pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.image_label.update()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.last_point = None
    
    def clearAnnotations(self):
        painter = QPainter(self.image_label.pixmap())
        painter.eraseRect(self.image_label.rect())
        self.image_label.update()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    w = ImageAnnotationWindow()
    w.show()
    sys.exit(app.exec())
