import pytest
from tests.qt_tests.Scenario.common import load_file
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
    extension = '.FEM'
    load_file(path, name, extension)
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
    extension = '.FEM'
    load_file(path, name, extension)
    TrafoCalc.load_state()
    TrafoCalc.run_calc()
    TrafoCalc.save_FEMM_model()
    print(os.getcwd())
    result = filecmp.cmp(path + name + '.FEM', path + name + '_ref.FEM')
    print(result)
    assert result
