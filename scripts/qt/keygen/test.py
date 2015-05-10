from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
class ListModel(QAbstractListModel):
    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
 
        self._data=["Row %d" % i for i in xrange(10)]
 
    def rowCount(self, parent=QModelIndex()):
        if parent.isValid(): return 0
        return len(self._data)
 
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid(): return QVariant()
        if role==Qt.DisplayRole: return self._data[index.row()]
        return QVariant()
 
    def flags(self, index):
        if index.isValid():
            return Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled
 
        return Qt.ItemIsSelectable|Qt.ItemIsDragEnabled| \
                    Qt.ItemIsDropEnabled|Qt.ItemIsEnabled
 
    def insertRows(self, row, count, parent=QModelIndex()):
        if parent.isValid(): return False
 
        beginRow=max(0,row)
        endRow=min(row+count-1,len(self._data))
 
        self.beginInsertRows(parent, beginRow, endRow)
 
        for i in xrange(beginRow, endRow+1): self._data.insert(i,"")
 
        self.endInsertRows()
        return True
 
    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid() or role!=Qt.DisplayRole: return False
       
        self._data[index.row()]=str(value.toString())
        self.dataChanged.emit(index,index)
        return True
 
    def removeRows(self, row, count, parent=QModelIndex()):
        if parent.isValid(): return False
        if row>=len(self._data) or row+count<=0: return False
 
        beginRow=max(0,row)
        endRow=min(row+count-1,len(self._data)-1)
 
        self.beginRemoveRows(parent, beginRow, endRow)
 
        for i in xrange(beginRow, endRow+1): self._data.pop(i)
 
        self.endRemoveRows()
        return True
 
class ListView(QListView):
    def __init__(self, model, parent=None):
        QTreeView.__init__(self, parent)
 
        self.setModel(model)
        self.setMovement(QListView.Snap)
        self.setDragDropMode(QListView.InternalMove)
        self.setDragDropOverwriteMode(True)
 
class Window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
 
        l=QHBoxLayout(self)
 
        self.model=ListModel(self)
        self.view=ListView(self.model)
        l.addWidget(self.view)
 
if __name__=="__main__":
    from sys import argv, exit
    a=QApplication(argv)
    w=Window()
    w.show()
    w.raise_()
    exit(a.exec_())
