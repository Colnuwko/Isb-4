## супер-мега-скрипт.... всех Рахит
    #Куплинов :)
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Window(QMainWindow):

    def main_function(self, variant):
        print(1)
    def button_start_click(self):
        if self.variant_label.text() != '':
            if int(self.variant_label.text()) > 20:
                QMessageBox.about(self, "Ошибка", "Нет такого варианта")
                self.variant_label.clear()
            else:
                self.main_function(self.variant_label.text())
                self.button_start.hide()
                self.first_text.hide()
                self.variant_label.hide()
        else:
            QMessageBox.about(self, "Ошибка", "Пустое поле недопустимо")
    def button_restart_click(self):
        print("restart")

    def button_show_graph_click(self):
        print("График")

    def check_by_alg_moon_click(self):
        print("alg")
    def position(self):
        self.first_text.move(390, 200)
        self.variant_label.move(465, 250)
        self.button_start.move(445, 310)



    def set_size(self):
        self.variant_label.setFixedSize(60, 40)
        self.first_text.adjustSize()
        self.button_start.setFixedSize(100, 30)

    def set_value(self):
        self.first_text.setFont(QFont('Times', 14))
        self.first_text.setText("Введите номер варианта")
        self.button_start.setText("Продолжить")


    def __init__(self) -> None:
        super(Window, self).__init__()
        self.first_text = QtWidgets.QLabel(self)
        self.variant_label = QtWidgets.QLineEdit(self)
        self.button_start = QtWidgets.QPushButton(self)
        self.button_restart = QtWidgets.QPushButton(self)
        self.button_show_graph = QtWidgets.QPushButton(self)
        self.check_by_alg_moon = QtWidgets.QPushButton(self)


        reg_variant = QRegExp("[1-9][0-9]")
        input_validator = QRegExpValidator(reg_variant, self.variant_label)
        self.variant_label.setValidator(input_validator)
        self.button_start.clicked.connect(self.button_start_click)
        self.button_restart.clicked.connect(self.button_restart_click)
        self.button_show_graph.clicked.connect(self.button_show_graph_click)
        self.check_by_alg_moon.clicked.connect(self.check_by_alg_moon_click)


        self.set_value()
        self.position()
        self.set_size()
def application() -> None:
    """"Start aplication mainwindow"""

    app = QApplication(sys.argv)
    window = Window()
    window.setObjectName("MainWindow")
    #window.setWindowIcon(QtGui.QIcon("phon.png"))
    window.setMinimumSize(1000, 800)
    window.setMaximumSize(1024, 720)
    window.setStyleSheet("#MainWindow{border-image:url(phon.png)}")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()