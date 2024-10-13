from pathlib import Path
root_dir = Path(__file__).parent
import sys
sys.path.extend([str(root_dir), str(root_dir/"src")])
import codecs
import logging
import os
import os.path as osp
import sys

import yaml
from PySide6 import QtCore
from PySide6 import QtWidgets

from labelme import __appname__
from labelme import __version__
from labelme.app import MainWindow
from labelme.config import get_config, get_default_config
from labelme.logger import logger
from labelme.utils import newIcon

config = get_default_config()

filename = None
output_file = None
output_dir = None

translator = QtCore.QTranslator()
translator.load(
    QtCore.QLocale.system().name(),
    str(root_dir/"src/labelme/translate"),
)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName(__appname__)
    app.setWindowIcon(newIcon("icon"))
    app.installTranslator(translator)
    win = MainWindow(
        config=config,
        # filename=filename,
        # output_file=output_file,
        # output_dir=output_dir,
    )
    win.show()
    # win.raise_()
    sys.exit(app.exec())
