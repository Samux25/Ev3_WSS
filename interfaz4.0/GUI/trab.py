import sys
#sys.path.append("D:/Codigos/Python Desarrollo/Ev3_WSS/Model")
sys.path.append("C:/taller/WSS/Control") #Ruta Tito
from CTRR import * 
from PyQt6.QtWidgets import QMainWindow
from GUI.ui_trabajador import Ui_MainWindow
from GUI.Art import ART
from PyQt6 import QtCore, QtWidgets

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt, QPointF

class Trabajador(QMainWindow, Ui_MainWindow):
    def __init__(self,datos):
        super().__init__()
        self.setupUi(self)
        self.bt_normal.hide()
        self.click_posicion = None
        self.bt_minimize.clicked.connect(lambda: self.showMinimized())
        self.bt_normal.clicked.connect(self.control_bt_normal)
        self.bt_maximize.clicked.connect(self.control_bt_maximize)
        self.bt_close.clicked.connect(lambda: self.close())
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        self.contr = Controlador()
        self.show()

        self.resultado = None
        self.datos = datos


        self.NombreTrab.setText(datos[0])
        self.DireccionTrab.setText(datos[1])
        self.TelefonoTrab.setText(datos[2])
        self.CorreoTrab.setText(datos[3])

        self.ElegirArt.activated.connect(self.decision)
        self.IniciarArt()


    def control_bt_normal(self): 
        self.showNormal()
        self.bt_normal.hide()
        self.bt_maximize.show()

    def control_bt_maximize(self): 
        self.showMaximized()
        self.bt_maximize.hide()
        self.bt_normal.show()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.click_posicion = event.globalPosition()

    def mover_ventana(self, event):
        if not self.isMaximized():
            if event.buttons() == Qt.MouseButton.LeftButton:
                delta = QPointF(event.globalPosition() - self.click_posicion)
                self.move(self.pos() + delta.toPoint())
                self.click_posicion = event.globalPosition()
                event.accept()
        if event.globalPosition().y() <= 5 or event.globalPosition().x() <= 5:
            self.showMaximized()
            self.bt_maximize.hide()
            self.bt_normal.show()
        else:
            self.showNormal()
            self.bt_normal.hide()
            self.bt_maximize.show()

    def procesarSeleccion(self, seleccion):
        if seleccion == 'Lavado de material':
            return 'Lavado de material'
        elif seleccion == 'Lecturas en equipo de A.A.':
            return 'Lectura de muestras por absorcion.' #Lecturas en equipo de A.A.
        elif seleccion == 'Masado de muestras':
            return 'Masado de muestras'
        elif seleccion == 'Digestión acida de muestras':
            return 'Digestión acida'
        elif seleccion == 'Lixivición de muestras':
            return 'Lixiviaxión'
        else:
            return 'Selección desconocida'

    def decision(self):
        seleccion = self.ElegirArt.currentText()
        self.resultado = self.procesarSeleccion(seleccion)

    def abrirArt(self):
        resultado = self.resultado
        datos = self.datos
        riesgoCrit = self.contr.visualizarRiesgoActividad(resultado)
        controlRiesgo = self.contr.visualizarControlRiesgo(resultado)
        self.supervisor = ART(datos, riesgoCrit,controlRiesgo)
        self.hide()

    def IniciarArt(self):
        self.iniciarArt.clicked.connect(self.abrirArt)

if __name__ == "__main__":
        app = QApplication([])
        window = Trabajador()
        window.show()
        app.exec()
