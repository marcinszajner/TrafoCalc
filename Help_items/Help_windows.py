from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from Help_items.InputVoltage import InputVoltageHelpWindow
from Help_items.OutputVoltage import OutputVoltageHelpWindow
from Help_items.OutputPower import OutputPowerHelpWindow
from Help_items.Frequency import FrequencyHelpWindow
from Help_items.Bmax import BmaxHelpWindow
from Help_items.CoreDimensions import CoreWindingAreaHelpWindow
from Help_items.CoreCrossSection import CoreCrossSectionHelpWindow
from Help_items.VoltSecond import VoltSecondHelpWindow
from Help_items.FillFactor import FillFactorHelpWindow

import os


def InitHelpObject(HelpWindow):
    HelpWindow.Window = QMainWindow()
    HelpWindow.setupUi(HelpWindow.Window)
    return HelpWindow


class HelpWindows:
    def __init__(self):
        super().__init__()
        self.InputVoltageHelpWindowObj = InitHelpObject(InputVoltageHelpWindow.Ui_InputVoltageHelpMainWindow())
        self.OutputVoltageHelpWindowObj = InitHelpObject(OutputVoltageHelpWindow.Ui_OutputVoltageHelpWindow())
        self.OutputPowerHelpWindowObj = InitHelpObject(OutputPowerHelpWindow.Ui_OutputPowerHelpWindow())
        self.FrequencyHelpWindowObj = InitHelpObject(FrequencyHelpWindow.Ui_FrequencyHelpWindow())
        self.BmaxHelpWindowObj = InitHelpObject(BmaxHelpWindow.Ui_BmaxHelpWindow())
        self.CoreWindingAreaHelpWindowObj = InitHelpObject(CoreWindingAreaHelpWindow.Ui_CoreWindingAreaHelpWindow())
        self.CoreCrossSectionHelpWindowObj = InitHelpObject(CoreCrossSectionHelpWindow.Ui_CoreCrossSectionHelpWindow())
        self.VoltSecondHelpWindowObj = InitHelpObject(VoltSecondHelpWindow.Ui_VoltSecondHelpWindow())

        for file in os.listdir("Help_items/VoltSecond"):
            if file.endswith("VoltSecond1.jpg"):
                path = os.path.join("/Help_items/VoltSecond", file)
            if file.endswith("VoltSecond2.jpg"):
                path2 = os.path.join("/Help_items/VoltSecond", file)
            if file.endswith("equations.jpg"):
                path4 = os.path.join("/Help_items/VoltSecond", file)

        self.VoltSecondHelpWindowObj.label.setPixmap(QPixmap(path[1:]))
        self.VoltSecondHelpWindowObj.label2.setPixmap(QPixmap(path2[1:]))
        self.VoltSecondHelpWindowObj.label4.setPixmap(QPixmap(path4[1:]))
        self.FillFactorHelpWindowObj = InitHelpObject(FillFactorHelpWindow.Ui_FillFactorHelpWindow())

    def PushInputVoltageHelpButton(self):
        self.InputVoltageHelpWindowObj.Window.show()

    def PushOutputVoltageHelpButton(self):
        self.OutputVoltageHelpWindowObj.Window.show()

    def PushOutputPowerHelpButton(self):
        self.OutputPowerHelpWindowObj.Window.show()

    def PushFrequencyHelpButton(self):
        self.FrequencyHelpWindowObj.Window.show()

    def PushBmaxHelpButton(self):
        self.BmaxHelpWindowObj.Window.show()

    def PushCoreWindingAreaHelpButton(self):
        self.CoreWindingAreaHelpWindowObj.Window.show()

    def PushCoreCrossSectionHelpButton(self):
        self.CoreCrossSectionHelpWindowObj.Window.show()

    def PushVoltSecondHelpButton(self):
        self.VoltSecondHelpWindowObj.Window.show()

    def PushFillFactorHelpButton(self):
        self.FillFactorHelpWindowObj.Window.show()
