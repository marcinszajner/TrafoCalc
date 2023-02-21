import sys
import gui
from Help_items import Help_windows
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from Transformer import *
from SaveLoad import SaveLoad
from FEMM_generator import File_format
import json

#!!!!!TODO!!!!! W napięciu wyjściowym dodać helpa o układzie zastępczym prostownika Robert L. Steigerwald
#https://www.youtube.com/watch?v=-P-tDMr50mk

#TODO opisać relatywną przenikalność jako średnia
#TODO default values for some params
#TODO do helpa voltosekundy zmienic tylko wzmiankę o asymmetric
#TODO jednoski jako lista by nie wpisywać 0.00004 itp
#TODO przejrzeć excela i dodać niektóre pola
#TODO Dodać współczynnik sprzężenia uzwojeń
class MainClass(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)
        self.Transformer = Transformer()
        self.SaveLoad = SaveLoad()
        self.FEMMmodel = File_format.FEMMmodelclass()

        self.HelpWindowsObject = Help_windows.HelpWindows()
        # self.InputVoltageHelpButton.clicked.connect(self.HelpWindowsObject.PushInputVoltageHelpButton)
        # self.OutputVoltageButton.clicked.connect(self.HelpWindowsObject.PushOutputVoltageHelpButton)
        # self.OutputPowerButton.clicked.connect(self.HelpWindowsObject.PushOutputPowerHelpButton)
        # self.FrequencyButton.clicked.connect(self.HelpWindowsObject.PushFrequencyHelpButton)
        # self.BmaxButton.clicked.connect(self.HelpWindowsObject.PushBmaxHelpButton)
        # self.CoreWindingAreaButton.clicked.connect(self.HelpWindowsObject.PushCoreWindingAreaHelpButton)
        # self.CoreCrossSectionButton.clicked.connect(self.HelpWindowsObject.PushCoreCrossSectionHelpButton)
        # self.VoltSecondButton.clicked.connect(self.HelpWindowsObject.PushVoltSecondHelpButton)
        # self.FillFactorButton.clicked.connect(self.HelpWindowsObject.PushFillFactorHelpButton)
        self.RunButton.clicked.connect(self.run_calc)
        self.actionSave.triggered.connect(self.save_state)
        self.actionLoad.triggered.connect(self.load_state)
        self.CreateModelButton.clicked.connect(self.save_FEMM_model)

    def parse_main_window_value_to_transformer_class(self):
        transformer_value = TransformerValueClass()
        a = vars(transformer_value)
        name = 'Value'
        for key, value in a.items():
            main_menu_transformer_values = getattr(self, key + name)
            if getattr(main_menu_transformer_values, 'text', None):
                setattr(transformer_value, key, main_menu_transformer_values.text())
            elif getattr(main_menu_transformer_values, 'currentText', None):
                setattr(transformer_value, key, main_menu_transformer_values.currentText())
        return transformer_value

    def run_calc(self):
        try:
            transformer_value = self.parse_main_window_value_to_transformer_class()
            self.Transformer.update_params(transformer_value)
            self.Transformer.validate_input_data_basic_simulation()
            self.Transformer.Calculate_winding_number()
            self.Transformer.Calculate_magnetization_current()
            self.Transformer.Calculate_wire_cross_section()
            self.Transformer.Calculate_Ap()
        except Exception as inst:
            print(inst.args)

        SelectedColour = QPalette()
        DeselectedColour = QPalette()
        SelectedColour.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Base, QColor(51, 240, 65))
        DeselectedColour.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Base, QColor(255, 255, 255))
        if float(self.PrimaryWindingSelectedValue.text()) > 0:
            self.PrimaryWindingSelectedValue.setPalette(SelectedColour)
        else:
            self.PrimaryWindingSelectedValue.setPalette(DeselectedColour)

        if float(self.PrimaryWindingSelectedValue.text()):
            self.PrimaryWindingSelectedValue.setPalette(SelectedColour)
        else:
            self.PrimaryWindingSelectedValue.setPalette(DeselectedColour)

        transformer_output_value = self.Transformer.TransformerOutputValue
        a = vars(transformer_output_value)
        name = 'Value'
        for key, value in a.items():
            data = getattr(transformer_output_value , key)
            main_menu_transformer_values = getattr(self, key + name)
            main_menu_transformer_values.setText(str(float("{:.5e}".format(data))))

        result_palette = QPalette()
        if float(self.ApCalculatedValue.text()) >= float(self.ApTheoryValue.text()):
            result_palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.WindowText, QColor(240, 51, 65))
            self.ApResultLabel.setText('Fail')
        else:
            result_palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.WindowText, QColor(51, 240, 65))
            self.ApResultLabel.setText('Pass')
        self.ApResultLabel.setPalette(result_palette)

    def save_state(self):
        transformer_value = self.parse_main_window_value_to_transformer_class()
        self.Transformer.update_params(transformer_value)
        self.SaveLoad.create_json(self.Transformer.TransformerValue)
        self.SaveLoad.save_json(self)

    def load_state(self):
        transformer_value = TransformerValueClass()
        self.SaveLoad.load_json(self, transformer_value)

    def save_FEMM_model(self):
        self.run_calc()

        if self.Transformer.TransformerValue.ModelType == 'Magnetic field simulation':
            name, _ = QFileDialog.getSaveFileName(self, 'Save file', '', 'FEMM(*.FEM);;all Files(*)')
            if name:
                if not name.find('.*'):
                    name = name + '.FEM'
            self.Transformer.validate_dimensions()
            self.FEMMmodel.CreateFEMMfile(self.Transformer, name)
        elif self.Transformer.TransformerValue.ModelType == 'Electrostatic field simulation':
            name, _ = QFileDialog.getSaveFileName(self, 'Save file', '', 'FEMM(*.FEE);;all Files(*)')
            if name:
                if not name.find('.*'):
                    name = name + '.FEE'
            #try:
            self.Transformer.validate_dimensions()
            self.FEMMmodel.CreateFEMMfile(self.Transformer, name)
            #except Exception as inst:
                #print(inst.args)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainClass()
    win.MainWindow.show()
    sys.exit(app.exec())