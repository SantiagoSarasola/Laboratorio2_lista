from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
from PyQt5 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("listaa.ui", self)
        self.agregar.clicked.connect(self.on_agregar)
        self.editar.clicked.connect(self.on_editar)
        self.eliminar.clicked.connect(self.on_eliminar)  
        #self.limpiar.clicked.connect(self.on_eliminar_todos)  
        self.derecha.clicked.connect(self.on_pasar)
    
    def on_agregar(self):
        self.lista1.addItem(self.nombre.text())
        self.nombre.setText('')
    
    def on_pasar(self):
        self.lista2.addItem(self.lista1.currentItem().text())
        self.lista1.takeItem(self.lista1.currentRow())
        
        
    def on_editar(self):
        texto_item = self.lista2.currentItem().text()
        nuevo_texto,ok = QInputDialog.getText(self,'Editar','Ingrese nuevo nombre',text=texto_item)  
        if ok:
            self.lista2.currentItem().setText(nuevo_texto)     
    
    def on_eliminar(self):
        self.lista2.takeItem(self.lista2.currentRow())
    
    def on_eliminar_todos(self):
        self.lista2.clear()
    

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()
