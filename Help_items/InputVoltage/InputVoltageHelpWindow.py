# Form implementation generated from reading ui file 'InputVoltageHelpWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_InputVoltageHelpMainWindow(object):
    def setupUi(self, InputVoltageHelpMainWindow):
        InputVoltageHelpMainWindow.setObjectName("InputVoltageHelpMainWindow")
        InputVoltageHelpMainWindow.resize(923, 565)
        self.centralwidget = QtWidgets.QWidget(InputVoltageHelpMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 851, 521))
        self.label.setStyleSheet("background-image: url(Help_items/InputVoltage/Input_voltage_help.jpg);")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label.setPixmap(QtGui.QPixmap("Help_items/InputVoltage/Input_voltage_help.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        InputVoltageHelpMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(InputVoltageHelpMainWindow)
        self.statusbar.setObjectName("statusbar")
        InputVoltageHelpMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InputVoltageHelpMainWindow)
        QtCore.QMetaObject.connectSlotsByName(InputVoltageHelpMainWindow)

    def retranslateUi(self, InputVoltageHelpMainWindow):
        _translate = QtCore.QCoreApplication.translate
        InputVoltageHelpMainWindow.setWindowTitle(_translate("InputVoltageHelpMainWindow", "MainWindow"))
