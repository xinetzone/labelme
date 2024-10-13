"""PySide6 port of the widgets/imageviewer example from Qt v6.0"""
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtWidgets import (QApplication)
from imageviewer import ImageViewer
from pathlib import Path
root_dir = Path(__file__).parents[2]
data_dir = root_dir/"data"
import sys
sys.path.extend([str(root_dir)])
from labelme.widgets import LabelDialog
from labelme.widgets import LabelQLineEdit

if __name__ == '__main__':
    
    from argparse import ArgumentParser, RawTextHelpFormatter
    arg_parser = ArgumentParser(description="Image Viewer",
                                formatter_class=RawTextHelpFormatter)
    arg_parser.add_argument('file', type=str, nargs='?', help='Image file')
    args = arg_parser.parse_args()

    app = QApplication(sys.argv)
    image_viewer = ImageViewer()
    list_widget = QtWidgets.QListWidget()
    list_widget.addItems(["cat", "dog", "person"])
    widget = LabelQLineEdit()
    widget.setListWidget(list_widget)
    # image_viewer.addWidget(widget)

    # key press to navigate in label list
    item = widget.list_widget.findItems("cat", QtCore.Qt.MatchExactly)[0]
    widget.list_widget.setCurrentItem(item)

    # key press to enter label
    image_viewer.keyPress(widget, QtCore.Qt.Key_P)
    image_viewer.keyPress(widget, QtCore.Qt.Key_E)
    image_viewer.keyPress(widget, QtCore.Qt.Key_R)
    image_viewer.keyPress(widget, QtCore.Qt.Key_S)
    image_viewer.keyPress(widget, QtCore.Qt.Key_O)
    image_viewer.keyPress(widget, QtCore.Qt.Key_N)

    if args.file and not image_viewer.load_file(args.file):
        sys.exit(-1)

    image_viewer.show()
    sys.exit(app.exec())