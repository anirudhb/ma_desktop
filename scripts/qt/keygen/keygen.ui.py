# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keygen.ui'
#
# Created: Sun Dec 28 11:07:29 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import decompress
from PyQt4 import QtCore, QtGui
import sys
from keygen import KeyGen


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

class DragDropListWidget(QtGui.QListWidget):
	def __init__(self, parent):
		super(DragDropListWidget, self).__init__(parent)
		self.setAcceptDrops(True)
		self.setDragEnabled(True)
		self.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
		self.setDragDropOverwriteMode(False)
		self.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
	
	def dragEnterEvent(self, e):
		if e.mimeData().hasFormat("text/plain"):
			e.accept()
		else:
			super(DragDropListWidget, self).dragEnterEvent(e)
	
	def dragMoveEvent(self, e):
		if e.mimeData().hasFormat("text/plain"):
			e.setDropAction(QtCore.Qt.CopyAction)
			e.accept()
		else:
			super(DragDropListWidget, self).dragMoveEvent(e)	

	def dropEvent(self, e):
		self.addItem(e.mimeData().text())

	
	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Delete:
			self.delItems()
	
	def delItems(self):
		for item in self.selectedItems():
			self.takeItem(self.row(item))
		



class Ui_Form(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
        self.gen = KeyGen()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = DragDropListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.verticalLayout.addWidget(self.pushButton2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    @QtCore.pyqtSignature("on_pushButton_clicked()")
    def gen_keys(self):
        self.gen.change_method("uuid")
        for i in range(500):
            item = QtGui.QListWidgetItem()
            item.setText(self.gen.get_key())
            self.listWidget.addItem(item)
        self.gen.change_method("str")
        for i in range(500):
            item = QtGui.QListWidgetItem()
            item.setText(self.gen.get_key())
            self.listWidget.addItem(item)

    @QtCore.pyqtSignature("on_pushButton2_clicked()")
    def clearAll(self):
        self.listWidget.clear()
	
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Fake Key Generator", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "Generate Keys", None))
        self.pushButton2.setText(_translate("Form", "Clear All", None))

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	ex = Ui_Form()
	# ex.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
	ex.show()
	app.exec_()
	import cleanup
