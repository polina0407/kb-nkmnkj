from PyQt5.QtWidgets import (QApplication, QWidget,
QFileDialog,
QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout)

from PyQt5 import QtGui
from PyQt5.QtCore import Qt

app = QApplication([])
win = QWidget()

win.setStyleSheet('background-color:#e366be; font-size:24px; padding: 5px')
win.setWindowIcon(QtGui.QIcon("1686894616_celes-club-p-kotiki-milie-nyashnie-risunki-dlya-srisovk-2.jpg"))

win.resize (1200, 700)
win.setWindowTitle('Easy Editor')

lb_image = QLabel("Картинка")

btn_dir = QPushButton("Папка")
btn_dir.setStyleSheet('border:2px solid #708899; border-radius:20px; background-color:#ecf545')
btn_dir.setCursor(Qt.PointingHandCursor)

lw_files = QListWidget()
lw_files.setStyleSheet('border:2px solid #708899; border-radius:20px; background-color:#ecf545 ')

btn_left = QPushButton("Вліво")
btn_left.setStyleSheet('border:2px solid #102738; border-radius:20px; background-color:#ecf545')
btn_left.setCursor(Qt.PointingHandCursor)

btn_right = QPushButton("Вправо")
btn_right.setStyleSheet('border:2px solid #102738; border-radius:20px; background-color:#ecf545')
btn_right.setCursor(Qt.PointingHandCursor)

btn_flip = QPushButton("Дзеркально")
btn_flip.setStyleSheet('border:2px solid #102738; border-radius:20px; background-color:#ecf545')
btn_flip.setCursor(Qt.PointingHandCursor)

btn_sharp = QPushButton("Різкість")
btn_sharp.setStyleSheet('border:2px solid #102738; border-radius:20px; background-color:#ecf545')
btn_sharp.setCursor(Qt.PointingHandCursor)

btn_bw = QPushButton("Ч/б")
btn_bw.setStyleSheet('border:2px solid #102738; border-radius:20px; background-color:#ecf545')
btn_bw.setCursor(Qt.PointingHandCursor)

row = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()
col3 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

col2.addWidget(lb_image, 95)

col3.addWidget(btn_left)
col3.addWidget(btn_right)
col3.addWidget(btn_flip)
col3.addWidget(btn_sharp)
col3.addWidget(btn_bw)

row.addLayout(col1, 20)
row.addLayout(col2, 60)
row.addLayout(col3, 20)
win.setLayout(row)

win.show()
app.exec()
