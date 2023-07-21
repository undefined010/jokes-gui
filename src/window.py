from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel
from fetchingdata import *
import pyautogui as pg
from time import sleep


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.WIDTH = 1000
        self.HEIGHT = 800

        self.gen_joke_btn = QPushButton(self)
        self.write_it_btn = QPushButton(self)
        self.output = QLabel(self)

        self.setWindowTitle("My App")
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setStyleSheet('background-color: blue;')

        self._init()

    def _init(self) -> None:
        self.gen_joke_btn.setMaximumWidth(80)
        self.gen_joke_btn.setMaximumHeight(30)
        self.gen_joke_btn.setText("generate")
        self.gen_joke_btn.move((self.WIDTH / 2) - 30, (self.HEIGHT / 2))
        self.gen_joke_btn.setStyleSheet('background-color = red;')
        self.gen_joke_btn.clicked.connect(self._update_label)

        self.write_it_btn.setMaximumWidth(80)
        self.write_it_btn.setMaximumHeight(30)
        self.write_it_btn.setText("write it")
        self.write_it_btn.move((self.WIDTH / 2) - 110, self.HEIGHT / 2)
        self.write_it_btn.clicked.connect(self.write_it)

        # todo: write a algorithm to center the output label according to text length

        self.output.setFixedWidth(self.WIDTH)
        self.output.setFixedHeight(100)
        self.output.setText('')
        self.output.move(self.WIDTH / 2 - 350, self.HEIGHT / 2 - 100)

    def _update_label(self) -> None:

        self.output.setText('{}'.format(JokesApi.get_random_joke()))

    def write_it(self) -> None:
        # todo: make the seconds change in the output label
        temp: str = str(self.output.text())
        self.output.setText('after 5 seconds ')
        sleep(5)
        self.output.setText(temp)
        pg.write(self.output.text())
