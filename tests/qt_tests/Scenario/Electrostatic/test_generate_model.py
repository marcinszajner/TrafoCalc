import pytest
from PyQt6 import QtCore
import keyboard
import filecmp
import os

from src.TrafoCalc import MainClass

@pytest.fixture
def TrafoCalc(qtbot):
    test_Trafocalc = MainClass()
    qtbot.addWidget(test_Trafocalc)

    return test_Trafocalc

def test_normal_model(TrafoCalc):
    name = 'tc_sinus_normal'
    path = 'tests\\qt_tests\\Scenario\\Electrostatic\\' + name + '\\'
    QtCore.QTimer.singleShot(50, lambda: keyboard.write(path + name + '.json'))
    QtCore.QTimer.singleShot(150, lambda: keyboard.send('enter'))
    QtCore.QTimer.singleShot(1000, lambda: keyboard.write(path + name + '.FEE'))
    QtCore.QTimer.singleShot(1200, lambda: keyboard.send('enter'))
    QtCore.QTimer.singleShot(1400, lambda: keyboard.send('tab'))
    QtCore.QTimer.singleShot(1800, lambda: keyboard.send('enter'))
    TrafoCalc.load_state()
    TrafoCalc.run_calc()
    TrafoCalc.save_FEMM_model()
    print(os.getcwd())
    print(path + name + '.FEE')
    print(path + name + '_ref.FEE')
    result = filecmp.cmp(path + name + '.FEE', path + name + '_ref.FEE')
    print(result)
    assert result

def test_simplified_model(TrafoCalc):
    name = 'tc_sinus_simplified'
    path = 'tests\\qt_tests\\Scenario\\Electrostatic\\' + name + '\\'
    QtCore.QTimer.singleShot(50, lambda: keyboard.write(path + name + '.json'))
    QtCore.QTimer.singleShot(150, lambda: keyboard.send('enter'))
    QtCore.QTimer.singleShot(1000, lambda: keyboard.write(path + name + '.FEE'))
    QtCore.QTimer.singleShot(1200, lambda: keyboard.send('enter'))
    QtCore.QTimer.singleShot(1400, lambda: keyboard.send('tab'))
    QtCore.QTimer.singleShot(1800, lambda: keyboard.send('enter'))
    TrafoCalc.load_state()
    TrafoCalc.run_calc()
    TrafoCalc.save_FEMM_model()
    print(os.getcwd())
    result = filecmp.cmp(path + name + '.FEE', path + name + '_ref.FEE')
    print(result)
    assert result
