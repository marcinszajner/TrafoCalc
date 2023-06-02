import pytest
import keyboard
import json
import os

from PyQt6 import QtCore
from src.TrafoCalc import MainClass

@pytest.fixture
def TrafoCalc(qtbot):
    test_Trafocalc = MainClass()
    qtbot.addWidget(test_Trafocalc)

    return test_Trafocalc

def test_save_json_cancel(TrafoCalc):
    QtCore.QTimer.singleShot(200, lambda: keyboard.send('esc'))
    TrafoCalc.save_state()

def test_load_json_cancel(TrafoCalc):
    QtCore.QTimer.singleShot(200, lambda: keyboard.send('esc'))
    TrafoCalc.load_state()

def test_save_json(TrafoCalc):
    if os.path.isfile('tests\\qt_tests\\Load_and_save\\save_test.json'):
        os.remove('tests\\qt_tests\\Load_and_save\\save_test.json')
    QtCore.QTimer.singleShot(50, lambda: keyboard.write('tests\\qt_tests\\Load_and_save\\save_test.json'))
    QtCore.QTimer.singleShot(250, lambda: keyboard.send('enter'))
    QtCore.QTimer.singleShot(450, lambda: keyboard.send('tab'))
    QtCore.QTimer.singleShot(650, lambda: keyboard.send('enter'))
    TrafoCalc.save_state()
    json_file = open('tests\\qt_tests\\Load_and_save\\save_test.json')
    data = json.load(json_file)

    assert TrafoCalc.InputVoltageValue.text() == str(data['InputVoltage'])
    assert TrafoCalc.InputVoltageShapeValue.currentText() == data['InputVoltageShape']
    assert TrafoCalc.OutputVoltageValue.text() == str(data['OutputVoltage'])
    assert TrafoCalc.OutputPowerValue.text() == str(data['OutputPower'])
    assert TrafoCalc.FrequencyValue.text() == str(data['Frequency'])
    assert TrafoCalc.CurrentDensityValue.text() == str(data['CurrentDensity'])
    assert TrafoCalc.BmaxValue.text() == str(data['Bmax'])
    assert TrafoCalc.CoreMaterialNameValue.text() == str(data['CoreMaterialName'])
    assert TrafoCalc.CorePermeabilityValue.text() == str(data['CorePermeability'])
    assert TrafoCalc.CoreCrossSectionValue.text() == str(data['CoreCrossSection'])
    assert TrafoCalc.MagneticPathLengthValue.text() == str(data['MagneticPathLength'])
    assert TrafoCalc.FillFactorValue.text() == str(data['FillFactor'])
    assert TrafoCalc.CoreWindingAreaValue.text() == str(data['CoreWindingArea'])
    assert TrafoCalc.PrimaryWindingSelectedValue.text() == str(data['PrimaryWindingSelected'])
    assert TrafoCalc.SecondaryWindingSelectedValue.text() == str(data['SecondaryWindingSelected'])
    assert TrafoCalc.PrimaryWireCrossSectionSelectedValue.text() == str(data['PrimaryWireCrossSectionSelected'])
    assert TrafoCalc.SecondaryWireCrossSectionSelectedValue.text() == str(data['SecondaryWireCrossSectionSelected'])
    assert TrafoCalc.CorePermittivityValue.text() == str(data['CorePermittivity'])
    assert TrafoCalc.CoreConductivityValue.text() == str(data['CoreConductivity'])
    assert TrafoCalc.PrimaryWindingMaterialValue.text() == str(data['PrimaryWindingMaterial'])
    assert TrafoCalc.PrimaryWindingMaterialConductivityValue.text() == str(data['PrimaryWindingMaterialConductivity'])
    assert TrafoCalc.SecondaryWindingMaterialValue.text() == str(data['SecondaryWindingMaterial'])
    assert TrafoCalc.SecondaryWindingMaterialConductivityValue.text()\
           == str(data['SecondaryWindingMaterialConductivity'])
    assert TrafoCalc.BobbinMaterialValue.text() == str(data['BobbinMaterial'])
    assert TrafoCalc.BobbinMaterialPermittivityValue.text() == str(data['BobbinMaterialPermittivity'])
    assert TrafoCalc.BetweenWireLayerInsulationMaterialValue.text() == str(data['BetweenWireLayerInsulationMaterial'])
    assert TrafoCalc.BetweenWireLayerInsulationMaterialPermittivityValue.text()\
           == str(data['BetweenWireLayerInsulationMaterialPermittivity'])
    assert TrafoCalc.BetweenWireLayerInsulationThicknessValue.text() == str(data['BetweenWireLayerInsulationThickness'])
    assert TrafoCalc.PrimaryWireInsulationNameValue.text() == str(data['PrimaryWireInsulationName'])
    assert TrafoCalc.PrimaryWireInsulationMaterialPermittivityValue.text()\
           == str(data['PrimaryWireInsulationMaterialPermittivity'])
    assert TrafoCalc.PrimaryWireInsulationThicknessValue.text() == str(data['PrimaryWireInsulationThickness'])
    assert TrafoCalc.SecondaryWireInsulationNameValue.text() == str(data['SecondaryWireInsulationName'])
    assert TrafoCalc.SecondaryWireInsulationMaterialPermittivityValue.text()\
           == str(data['SecondaryWireInsulationMaterialPermittivity'])
    assert TrafoCalc.SecondaryWireInsulationThicknessValue.text() == str(data['SecondaryWireInsulationThickness'])
    assert TrafoCalc.CoreShapeValue.currentText() == str(data['CoreShape'])
    assert TrafoCalc.SizeAValue.text() == str(data['SizeA'])
    assert TrafoCalc.SizeBValue.text() == str(data['SizeB'])
    assert TrafoCalc.SizeCValue.text() == str(data['SizeC'])
    assert TrafoCalc.SizeDValue.text() == str(data['SizeD'])
    assert TrafoCalc.SizeEValue.text() == str(data['SizeE'])
    assert TrafoCalc.SizeFValue.text() == str(data['SizeF'])
    assert TrafoCalc.BobbinXmargineValue.text() == str(data['BobbinXmargine'])
    assert TrafoCalc.BobbinY1margineValue.text() == str(data['BobbinY1margine'])
    assert TrafoCalc.BobbinY2margineValue.text() == str(data['BobbinY2margine'])
    assert TrafoCalc.InductanceValue.text() == str(data['Inductance'])
    assert TrafoCalc.CurrentMaxValue.text() == str(data['CurrentMax'])
    assert TrafoCalc.WindingNumInductanceValue.text() == str(data['WindingNumInductance'])
    assert TrafoCalc.WindingNumInductanceSelectedValue.text() == str(data['WindingNumInductanceSelected'])
    assert TrafoCalc.GapValue.text() == str(data['Gap'])
    assert TrafoCalc.WireCrossSectionSelectedInductanceValue.text() == str(data['WireCrossSectionSelectedInductance'])
    assert TrafoCalc.WireCrossSectionInductanceValue.text() == str(data['WireCrossSectionInductance'])
    assert TrafoCalc.SimplifiedWireModelValue.isChecked() == data['WireCrossSectionInductance']


def test_load_json(TrafoCalc):
    QtCore.QTimer.singleShot(250, lambda: keyboard.write('tests\\qt_tests\\Load_and_save\\example.json'))
    QtCore.QTimer.singleShot(750, lambda: keyboard.send('enter'))
    TrafoCalc.load_state()
    assert TrafoCalc.InputVoltageValue.text() == '162.0'
    assert TrafoCalc.InputVoltageShapeValue.currentText() == 'Sinus'
    assert TrafoCalc.OutputVoltageValue.text() == '1000.0'
    assert TrafoCalc.OutputPowerValue.text() == '1000.0'
    assert TrafoCalc.FrequencyValue.text() == '100000.0'
    assert TrafoCalc.CurrentDensityValue.text() == '4.5'
    assert TrafoCalc.BmaxValue.text() == '35.0'
    assert TrafoCalc.CoreMaterialNameValue.text() == '3f3'
    assert TrafoCalc.CorePermeabilityValue.text() == '1900.0'
    assert TrafoCalc.CoreCrossSectionValue.text() == '357.0'
    assert TrafoCalc.MagneticPathLengthValue.text() == '127.0'
    assert TrafoCalc.FillFactorValue.text() == '0.3'
    assert TrafoCalc.CoreWindingAreaValue.text() == '450.0'
    assert TrafoCalc.PrimaryWindingSelectedValue.text() == '50.0'
    assert TrafoCalc.SecondaryWindingSelectedValue.text() == '0.0'
    assert TrafoCalc.PrimaryWireCrossSectionSelectedValue.text() == '0.0'
    assert TrafoCalc.SecondaryWireCrossSectionSelectedValue.text() == '0.0'
    assert TrafoCalc.CorePermittivityValue.text() == '100000.0'
    assert TrafoCalc.CoreConductivityValue.text() == '2.0'
    assert TrafoCalc.PrimaryWindingMaterialValue.text() == 'Copper'
    assert TrafoCalc.PrimaryWindingMaterialConductivityValue.text() == '58000000.0'
    assert TrafoCalc.SecondaryWindingMaterialValue.text() == 'Copper'
    assert TrafoCalc.SecondaryWindingMaterialConductivityValue.text() == '58000000.0'
    assert TrafoCalc.BobbinMaterialValue.text() == 'Bobbin material name'
    assert TrafoCalc.BobbinMaterialPermittivityValue.text() == '1.0'
    assert TrafoCalc.BetweenWireLayerInsulationMaterialValue.text() == 'Kapton 100'
    assert TrafoCalc.BetweenWireLayerInsulationMaterialPermittivityValue.text() == '3.9'
    assert TrafoCalc.BetweenWireLayerInsulationThicknessValue.text() == '0.2'
    assert TrafoCalc.PrimaryWireInsulationNameValue.text() == 'polyamide'
    assert TrafoCalc.PrimaryWireInsulationMaterialPermittivityValue.text() == '4.0'
    assert TrafoCalc.PrimaryWireInsulationThicknessValue.text() == '0.02'
    assert TrafoCalc.SecondaryWireInsulationNameValue.text() == 'Polyesterimide'
    assert TrafoCalc.SecondaryWireInsulationMaterialPermittivityValue.text() == '3.3'
    assert TrafoCalc.SecondaryWireInsulationThicknessValue.text() == '0.2'
    assert TrafoCalc.CoreShapeValue.currentText() == 'EE'
    assert TrafoCalc.SizeAValue.text() == '54.5'
    assert TrafoCalc.SizeBValue.text() == '41.2'
    assert TrafoCalc.SizeCValue.text() == '18.9'
    assert TrafoCalc.SizeDValue.text() == '27.6'
    assert TrafoCalc.SizeEValue.text() == '20.2'
    assert TrafoCalc.SizeFValue.text() == '18.9'
    assert TrafoCalc.BobbinXmargineValue.text() == '2.0'
    assert TrafoCalc.BobbinY1margineValue.text() == '2.0'
    assert TrafoCalc.BobbinY2margineValue.text() == '2.0'
    assert TrafoCalc.InductanceValue.text() == '0.05'
    assert TrafoCalc.CurrentMaxValue.text() == '10.0'
    assert TrafoCalc.WindingNumInductanceValue.text() == '28.0112'
    assert TrafoCalc.WindingNumInductanceSelectedValue.text() == '7.0'
    assert TrafoCalc.GapValue.text() == '7.03849'
    assert TrafoCalc.WireCrossSectionSelectedInductanceValue.text() == '0.0'
    assert TrafoCalc.WireCrossSectionInductanceValue.text() == '2.22222'
    assert TrafoCalc.SimplifiedWireModelValue.isChecked() == False
