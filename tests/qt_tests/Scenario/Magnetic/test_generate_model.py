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
    path = 'tests\\qt_tests\\Scenario\\Magnetic\\' + name + '\\'
    QtCore.QTimer.singleShot(50, lambda: keyboard.write(path + name + '.json'))
    QtCore.QTimer.singleShot(150, lambda: keyboard.send('enter'))
    QtCore.QTimer.singleShot(1000, lambda: keyboard.write(path + name + '.FEM'))
    QtCore.QTimer.singleShot(1200, lambda: keyboard.send('enter'))
    QtCore.QTimer.singleShot(1400, lambda: keyboard.send('tab'))
    QtCore.QTimer.singleShot(1600, lambda: keyboard.send('enter'))
    TrafoCalc.load_state()
    TrafoCalc.run_calc()
    TrafoCalc.save_FEMM_model()
    print(os.getcwd())
    print(path + name + '.FEM')
    print(path + name + '_ref.FEM')
    result = filecmp.cmp(path + name + '.FEM', path + name + '_ref.FEM')
    print(result)
    assert result

def test_simplified_model(TrafoCalc):
    name = 'tc_sinus_simplified'
    path = 'tests\\qt_tests\\Scenario\\Magnetic\\' + name + '\\'
    QtCore.QTimer.singleShot(50, lambda: keyboard.write(path + name + '.json'))
    QtCore.QTimer.singleShot(150, lambda: keyboard.send('enter'))
    QtCore.QTimer.singleShot(1000, lambda: keyboard.write(path + name + '.FEM'))
    QtCore.QTimer.singleShot(1200, lambda: keyboard.send('enter'))
    QtCore.QTimer.singleShot(1400, lambda: keyboard.send('tab'))
    QtCore.QTimer.singleShot(1600, lambda: keyboard.send('enter'))
    TrafoCalc.load_state()
    TrafoCalc.run_calc()
    TrafoCalc.save_FEMM_model()
    print(os.getcwd())
    result = filecmp.cmp(path + name + '.FEM', path + name + '_ref.FEM')
    print(result)
    assert result
