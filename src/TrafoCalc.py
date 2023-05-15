import sys
from src import gui
from Help_items import Help_windows
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from src.Transformer import *
from src.SaveLoad import SaveLoad
from FEMM_generator import File_format


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
            if getattr(main_menu_transformer_values, 'isChecked', None):
                setattr(transformer_value, key, main_menu_transformer_values.isChecked())
            elif getattr(main_menu_transformer_values, 'text', None):
                setattr(transformer_value, key, main_menu_transformer_values.text())
            elif getattr(main_menu_transformer_values, 'currentText', None):
                setattr(transformer_value, key, main_menu_transformer_values.currentText())
        return transformer_value

    def run_calc(self):
        #try:
            transformer_value = self.parse_main_window_value_to_transformer_class()
            self.Transformer.update_params(transformer_value)
            if self.Transformer.TransformerValue.ModelType == 'Magnetic field simulation' or \
               self.Transformer.TransformerValue.ModelType == 'Electrostatic field simulation':

                self.Transformer.validate_input_data_basic_simulation()
                self.Transformer.Calculate_winding_number()
                self.Transformer.Calculate_magnetization_current()
                self.Transformer.Calculate_wire_cross_section()
                self.Transformer.Calculate_Ap()

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
                    data = getattr(transformer_output_value, key)
                    main_menu_transformer_values = getattr(self, key + name)
                    main_menu_transformer_values.setText(str(float("{:.5e}".format(data))))

                result_palette = QPalette()
                if float(self.ApCalculatedValue.text()) >= float(self.ApTheoryValue.text()):
                    result_palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.WindowText,
                                            QColor(240, 51, 65))
                    self.ApResultLabel.setText('Fail')
                else:
                    result_palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.WindowText,
                                            QColor(51, 240, 65))
                    self.ApResultLabel.setText('Pass')
                self.ApResultLabel.setPalette(result_palette)
            elif self.Transformer.TransformerValue.ModelType == 'Inductance':
                self.Transformer.Calculate_inductor_gap_turns_wire_cross_section()
                self.Transformer.Calculate_Ap_inductance()
                WindingNumber = self.Transformer.TransformerValue.WindingNumInductance
                gap = self.Transformer.TransformerValue.Gap
                cross_section = self.Transformer.TransformerValue.PrimaryWireCrossSectionInductance
                ApTheory = self.Transformer.TransformerOutputValue.ApTheoryInductance
                ApCalculated = self.Transformer.TransformerOutputValue.ApCalculatedInductance
                self.WindingNumInductanceValue.setText(str(float("{:.5e}".format(WindingNumber))))
                self.WireCrossSectionInductanceValue.setText(str(float("{:.5e}".format(cross_section))))
                self.GapValue.setText(str(float("{:.5e}".format(gap))))
                self.ApTheoryInductanceValue.setText(str(float("{:.5e}".format(ApTheory))))
                self.ApCalculatedInductanceValue.setText(str(float("{:.5e}".format(ApCalculated))))

                result_palette = QPalette()
                if float(self.ApCalculatedInductanceValue.text()) >= float(self.ApTheoryInductanceValue.text()):
                    result_palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.WindowText,
                                            QColor(240, 51, 65))
                    self.ApResultInductanceLabel.setText('Fail')
                else:
                    result_palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.WindowText,
                                            QColor(51, 240, 65))
                    self.ApResultInductanceLabel.setText('Pass')
                self.ApResultInductanceLabel.setPalette(result_palette)

        #except Exception as inst:
        #    print(inst.args)



    def save_state(self):
        transformer_value = self.parse_main_window_value_to_transformer_class()
        self.Transformer.update_params(transformer_value)
        self.SaveLoad.create_json(self.Transformer.TransformerValue)
        self.SaveLoad.save_json(self)

    def load_state(self):
        transformer_value = TransformerValueClass()
        self.SaveLoad.load_json(self, transformer_value)

    def save_FEMM_model(self):
        transformer_value = self.parse_main_window_value_to_transformer_class()
        self.Transformer.update_params(transformer_value)

        if self.Transformer.TransformerValue.ModelType == 'Magnetic field simulation' or\
                self.Transformer.TransformerValue.ModelType == 'Inductance':
            name, _ = QFileDialog.getSaveFileName(self, 'Save file', '', 'FEMM(*.FEM);;all Files(*)')
            if name:
                if not name.find('.*'):
                    name = name + '.FEM'
                self.Transformer.validate_dimensions()
                self.FEMMmodel.CreateFEMMfile(self.Transformer, name, self.SimplifiedWireModelValue.isChecked())
        elif self.Transformer.TransformerValue.ModelType == 'Electrostatic field simulation':
            name, _ = QFileDialog.getSaveFileName(self, 'Save file', '', 'FEMM(*.FEE);;all Files(*)')
            if name:
                if not name.find('.*'):
                    name = name + '.FEE'
                try:
                    self.Transformer.validate_dimensions()
                    self.FEMMmodel.CreateFEMMfile(self.Transformer, name, self.SimplifiedWireModelValue.isChecked())
                except Exception as inst:
                    print(inst.args)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainClass()
    win.MainWindow.show()
    sys.exit(app.exec())
