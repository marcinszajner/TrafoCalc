# Form implementation generated from reading ui file 'CoreWindingAreaHelpWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CoreWindingAreaHelpWindow(object):
    def setupUi(self, CoreWindingAreaHelpWindow):
        CoreWindingAreaHelpWindow.setObjectName("CoreDimensionsHelpWindow")
        CoreWindingAreaHelpWindow.resize(430, 282)
        self.centralwidget = QtWidgets.QWidget(CoreWindingAreaHelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 351, 61))
        self.textEdit.setObjectName("textEdit")
        CoreWindingAreaHelpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CoreWindingAreaHelpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 21))
        self.menubar.setObjectName("menubar")
        CoreWindingAreaHelpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CoreWindingAreaHelpWindow)
        self.statusbar.setObjectName("statusbar")
        CoreWindingAreaHelpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CoreWindingAreaHelpWindow)
        QtCore.QMetaObject.connectSlotsByName(CoreWindingAreaHelpWindow)

    def retranslateUi(self, CoreWindingAreaHelpWindow):
        _translate = QtCore.QCoreApplication.translate
        CoreWindingAreaHelpWindow.setWindowTitle(_translate("CoreDimensionsHelpWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("CoreDimensionsHelpWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CoreDimensions</p></body></html>"))
