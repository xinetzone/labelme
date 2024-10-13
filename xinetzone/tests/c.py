from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QMainWindow, QFileDialog
from PySide6.QtGui import QImage, QImageReader, QPixmap
import sys

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 800, 600)
        
        # 创建主布局
        layout = QVBoxLayout()
        
        # 创建一个标签用于显示图像
        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)
        
        # 创建一个按钮用于选择图像文件
        select_button = QPushButton("Select Image", self)
        select_button.clicked.connect(self.selectImage)
        layout.addWidget(select_button)
        
        # 设置主窗口的中心部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
    def selectImage(self):
        # 打开文件对话框选择图像文件
        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Images (*.png *.xpm *.jpg *.bmp)")
        if image_path:
            # 使用QImageReader加载图像
            reader = QImageReader(image_path)
            reader.setAutoTransform(True)  # 设置自适应窗口大小
            img = reader.read()
            print(type(img))
            image = QImage(img)
            
            # 将图像显示在标签上
            pixmap = QPixmap.fromImage(image)
            self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec())
