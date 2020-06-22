import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout, QLineEdit, QSizePolicy

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora do Anderson")
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display,0,0,1,5)
        self.display.setDisabled(True)
        self.setStyleSheet("*{background: white; color: black; font-size:37px}")
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add(QPushButton('7'), 1, 0, 1, 1)
        self.add(QPushButton('8'), 1, 1, 1, 1)
        self.add(QPushButton('9'), 1, 2, 1, 1)
        self.add(QPushButton('+'), 1, 3, 1, 1)
        self.add(QPushButton('C'), 1, 4, 1, 1, lambda: self.display.setText(""))

        self.add(QPushButton('4'), 2, 0, 1, 1)
        self.add(QPushButton('5'), 2, 1, 1, 1)
        self.add(QPushButton('6'), 2, 2, 1, 1)
        self.add(QPushButton('-'), 2, 3, 1, 1)
        self.add(QPushButton('<-'), 2, 4, 1, 1, lambda: self.display.setText(self.display.text()[:-1]))

        self.add(QPushButton('1'), 3, 0, 1, 1)
        self.add(QPushButton('2'), 3, 1, 1, 1)
        self.add(QPushButton('3'), 3, 2, 1, 1)
        self.add(QPushButton('*'), 3, 3, 1, 1)
        self.add(QPushButton(''), 3, 4, 1, 1)

        self.add(QPushButton('.'), 4, 0, 1, 1)
        self.add(QPushButton('0'), 4, 1, 1, 1)
        self.add(QPushButton(''), 4, 2, 1, 1)
        self.add(QPushButton('/'), 4, 3, 1, 1)
        self.add(QPushButton('='), 4, 4, 1, 1, self.evale)


        self.setCentralWidget(self.cw)

    def add(self, btn, row, col, rowspan, colspan, funcao = None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

    def evale(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText("Conta invalidade")

if __name__=='__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec()