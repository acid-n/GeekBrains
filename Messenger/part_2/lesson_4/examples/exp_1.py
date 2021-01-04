# Подключаем файл с разметкой интерфейса, созданного через qtdesinger

import sys
from PyQt5.QtWidgets import QWidget, QApplication, qApp
from PyQt5 import uic


class MyWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        # Использование функции loadUi()
        uic.loadUi('test.ui', self)
        # Обработка события нажимая кнопки
        self.btnQuit.clicked.connect(qApp.quit)


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    WINDOW_OBJ = MyWindow()
    WINDOW_OBJ.show()
    sys.exit(APP.exec_())