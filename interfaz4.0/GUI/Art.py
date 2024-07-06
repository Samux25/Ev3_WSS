from PyQt6.QtWidgets import QMainWindow
from GUI.ui_ART import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt, QPointF

class ART(QMainWindow, Ui_MainWindow):
    def __init__(self):
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
        self.showMaximized()

        self.ElegirArt.currentIndexChanged.connect(self.elegirArt)
        self.PT1_si.clicked.connect(self.pregunta1)
        self.PT1_no.clicked.connect(self.pregunta1)
        self.PT2_si.clicked.connect(self.pregunta2)
        self.PT2_no.clicked.connect(self.pregunta2)
        self.PT3_si.clicked.connect(self.pregunta3)
        self.PT3_no.clicked.connect(self.pregunta3)
        self.PT4_si.clicked.connect(self.pregunta4)
        self.PT4_no.clicked.connect(self.pregunta4)
        self.PT5_si.clicked.connect(self.pregunta5)
        self.PT5_no.clicked.connect(self.pregunta5)
        self.PT6_si.clicked.connect(self.pregunta6)
        self.PT6_no.clicked.connect(self.pregunta6)


        self.respuesta_PT1 = None
        self.respuesta_PT2 = None
        self.respuesta_PT3 = None
        self.respuesta_PT4 = None
        self.respuesta_PT5 = None
        self.respuesta_PT6 = None

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

    def pregunta1(self):
        if self.sender() == self.PT1_si:
            self.respuesta_PT1 = "SI"
        elif self.sender() == self.PT1_no:
            self.respuesta_PT1 = "NO"

    def pregunta2(self):
        if self.sender() == self.PT2_si:
            self.respuesta_PT2 = "SI"
        elif self.sender() == self.PT2_no:
            self.respuesta_PT2 = "NO"

    def pregunta3(self):
        if self.sender() == self.PT3_si:
            self.respuesta_PT3 = "SI"
        elif self.sender() == self.PT3_no:
            self.respuesta_PT3 = "NO"

    def pregunta4(self):
        if self.sender() == self.PT4_si:
            self.respuesta_PT4 = "SI"
        elif self.sender() == self.PT4_no:
            self.respuesta_PT4 = "NO"

    def pregunta5(self):
        if self.sender() == self.PT5_si:
            self.respuesta_PT5 = "SI"
        elif self.sender() == self.PT5_no:
            self.respuesta_PT5 = "NO"

    def pregunta6(self):
        if self.sender() == self.PT6_si:
            self.respuesta_PT6 = "SI"
        elif self.sender() == self.PT6_no:
            self.respuesta_PT6 = "NO"

if __name__ == "__main__":
        app = QApplication([])
        window = ART()
        window.show()
        app.exec()
