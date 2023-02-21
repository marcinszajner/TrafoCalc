# Form implementation generated from reading ui file 'VoltSecondHelpWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VoltSecondHelpWindow(object):
    def setupUi(self, VoltSecondHelpWindow):
        VoltSecondHelpWindow.setObjectName("VoltSecondHelpWindow")
        VoltSecondHelpWindow.setEnabled(True)
        VoltSecondHelpWindow.resize(1199, 1500)
        VoltSecondHelpWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(VoltSecondHelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1183, 1443))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setPixmap(QtGui.QPixmap("VoltSecond1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label4.setFont(font)
        self.label4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label4.setText("")
        self.label4.setPixmap(QtGui.QPixmap("equations.jpg"))
        self.label4.setScaledContents(True)
        self.label4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label4.setObjectName("label4")
        self.gridLayout_2.addWidget(self.label4, 0, 1, 4, 1)
        self.label2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label2.setStyleSheet("")
        self.label2.setText("")
        self.label2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label2.setPixmap(QtGui.QPixmap("VoltSecond2.jpg"))
        self.label2.setScaledContents(True)
        self.label2.setObjectName("label2")
        self.gridLayout_2.addWidget(self.label2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 450))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 4, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        VoltSecondHelpWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VoltSecondHelpWindow)
        self.statusbar.setObjectName("statusbar")
        VoltSecondHelpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VoltSecondHelpWindow)
        QtCore.QMetaObject.connectSlotsByName(VoltSecondHelpWindow)

    def retranslateUi(self, VoltSecondHelpWindow):
        _translate = QtCore.QCoreApplication.translate
        VoltSecondHelpWindow.setWindowTitle(_translate("VoltSecondHelpWindow", "MainWindow"))
        self.label_2.setText(_translate("VoltSecondHelpWindow", "Fig. 1 Asymmetrical operation"))
        self.label_3.setText(_translate("VoltSecondHelpWindow", "Fig. 2 Symmetrical operation"))
        self.textBrowser.setHtml(_translate("VoltSecondHelpWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Volt-second is a same as weber - magnetic flux unit. Using volt-second is much more flexible that using some predefined value as itegral result. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If we start converter with 0 degree phase (fig 1) current have much higher value that we run converter with 90 degree phase shift (fig 2). After few cycle asymmetrical operation go to symmetrical operation but it could saturate core at begine and damage circuit.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    If we plan work with Asymmetrical operation we should assume much higher value of Bmax or use some softstart mechanizm or use control algorithm to start with symmetrical operation statement from begine</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If we look at input voltage as definite integral from point of start converter to few periods after we can see constant component in current. This is asymmetrical operation and could couse problem with saturating core if we caltulate voltage with indefinite integral. If we plan work with Asymmetrical operation we should assume much higher value of Bmax or use some softstart mechanizm or use control algorithm to start with symmetrical operation statement from begine</p></body></html>"))
