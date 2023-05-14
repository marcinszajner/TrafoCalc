from PyQt6 import QtCore
import keyboard

def load_file(path, name, extension):
    QtCore.QTimer.singleShot(500, lambda: keyboard.write(path + name + '.json'))
    QtCore.QTimer.singleShot(2000, lambda: keyboard.send('enter'))
    QtCore.QTimer.singleShot(3500, lambda: keyboard.write(path + name + extension))
    QtCore.QTimer.singleShot(5000, lambda: keyboard.send('enter'))
    QtCore.QTimer.singleShot(6000, lambda: keyboard.send('tab'))
    QtCore.QTimer.singleShot(7500, lambda: keyboard.send('enter'))