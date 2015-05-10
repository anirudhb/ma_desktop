#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'htmlpreview.ui'
#
# Created: Sun Nov 23 09:55:44 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui, QtWebKit

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Widget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1193, 746)
        Widget.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("HTML5_Logo_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Widget.setWindowIcon(icon)
        self.pushButton_3 = QtGui.QPushButton(Widget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 710, 261, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(Widget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 710, 281, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtGui.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 670, 261, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 670, 281, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit = QtGui.QPlainTextEdit(Widget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 20, 561, 651))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtGui.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 81, 17))
        self.label_2.setObjectName("label_2")
        self.label = QtGui.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(730, 0, 91, 17))
        self.label.setObjectName("label")
        self.webView = QtWebKit.QWebView(Widget)
        self.webView.setGeometry(QtCore.QRect(609, 19, 571, 721))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "HTML Preview", None))
        self.pushButton_3.setText(_translate("Widget", "Save", None))
        self.pushButton_4.setText(_translate("Widget", "Open", None))
        self.pushButton.setText(_translate("Widget", "Clear", None))
        self.pushButton_2.setText(_translate("Widget", "Preview", None))
        self.label_2.setText(_translate("Widget", "Html Editor", None))
        self.label.setText(_translate("Widget", "Html Preview", None))

    @QtCore.pyqtSignature("on_pushButton_3_clicked()")
    def saveFile(self):
        text = self.plainTextEdit.toPlainText()
        f = open(QtGui.QFileDialog.getSaveFileName(), "w")
        f.write(text)
        f.close()
        
    @QtCore.pyqtSignature("on_pushButton_4_clicked()")
    def openFile(self):
        f = open(QtGui.QFileDialog.getOpenFileName(), "r")
        self.plainTextEdit.setPlainText(f.read())
        f.close()

    @QtCore.pyqtSignature("on_pushButton_2_clicked()")
    def preview(self):
        self.webView.setHtml(self.plainTextEdit.toPlainText())

    @QtCore.pyqtSignature("on_pushButton_clicked()")
    def clear(self):
        self.webView.setUrl(QtCore.QUrl("about:blank"))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Widget()
    ex.show()
    sys.exit(app.exec_())
