from PyQt4 import QtCore, QtGui
from code import InteractiveInterpreter
import sys

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent=parent)
        self.newshell = True
        self.stmt = True
        self.construct = False
        self.initUI()
        self.index = 0
        self.interpreter = InteractiveInterpreter()

    def initUI(self):
        self.sh = QtGui.QTextEdit('''
Python 2.7.6 on linux2
** DO NOT DELETE SHELL PROMPT! **
>>> ''', self)
        self.sh.textChanged.connect(self.shellop)
        self.sh.setReadOnly(True)
        self.sh.setReadOnly(False)

    def shellop(self):
        self.index += 1
        if self.sh.toPlainText()[self.index] == "\n" and self.sh.toPlainText()[self.index-1] == ":":
            self.stmt = False
            self.construct = True
        elif self.sh.toPlainText()[self.index] == "\n" and not self.construct:
            self.stmt = not self.stmt
            class stdoutProxy:
                def write(self, s):
                    self.sh.insertPlainText(s)
            stdout = sys.stdout
            sys.stdout = stdoutProxy()
            self.interpreter.runsource(self.sh.toPlainText())
            self.sh.insertPlainText("\n")
            self.index += 1
            while self.interpreter.showtraceback():
                print self.interpreter.showtraceback()
            sys.stdout = stdout
        if self.sh.toPlainText()[self.index] == "\n" and not self.construct and not self.stmt:
            self.stmt = not self.stmt
            self.sh.insertPlainText(">>> ")
            self.index += 4
        if self.construct and self.sh.toPlainText()[self.index] == "\n" and self.sh.toPlainText()[self.index-1] == " ":
            self.construct = False
            self.sh.insertPlainText(">>> ")
            self.index += 4
        if self.construct:
            self.sh.insertPlainText("... ")
            index += 4

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
