# Form implementation generated from reading ui file 'FrequencyHelpWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FrequencyHelpWindow(object):
    def setupUi(self, FrequencyHelpWindow):
        FrequencyHelpWindow.setObjectName("FrequencyHelpWindow")
        FrequencyHelpWindow.resize(430, 282)
        self.centralwidget = QtWidgets.QWidget(FrequencyHelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 351, 61))
        self.textEdit.setObjectName("textEdit")
        FrequencyHelpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrequencyHelpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        FrequencyHelpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrequencyHelpWindow)
        self.statusbar.setObjectName("statusbar")
        FrequencyHelpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FrequencyHelpWindow)
        QtCore.QMetaObject.connectSlotsByName(FrequencyHelpWindow)

    def retranslateUi(self, FrequencyHelpWindow):
        _translate = QtCore.QCoreApplication.translate
        FrequencyHelpWindow.setWindowTitle(_translate("FrequencyHelpWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("FrequencyHelpWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Minimal frequency of input voltage</p></body></html>"))
