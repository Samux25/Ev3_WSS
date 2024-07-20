import sys
sys.path.append("C:/taller/WSS/Control") #Ruta Tito
from CTRR import * 
from PyQt6.QtWidgets import QMainWindow
from GUI.ui_ART import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton,QRadioButton
from PyQt6.QtCore import Qt, QPointF

class ART(QMainWindow, Ui_MainWindow):
    def __init__(self,rut,datos, riesgoCrit,controlRiesgo):
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
        self.datos = datos
        self.riesgoCrit = riesgoCrit
        self.rut = rut
        if riesgoCrit[1] == '6':
            self.RC1PR6.setVisible(False)
            self.RC1PR7.setVisible(False)
            self.RC1PR8.setVisible(False)
        if riesgoCrit[3] == '7':
            self.RC2PR8.setVisible(False)
        elif riesgoCrit[3] == (''):
            self.frame_27.setVisible(False)
        else:
            self.frame_27.setVisible(True)

        self.NombreActividad.setText(riesgoCrit[0])
        self.nombreRiesgo1.setText(riesgoCrit[2])
        self.nombreRiesgo2.setText(riesgoCrit[4])
        self.NumCod1.setText(riesgoCrit[1])
        self.NumCod2.setText(riesgoCrit[3])
        self.mostrarOtroRiesgo.setText(controlRiesgo[0])
        self.mostrarMedidasControl.setText(controlRiesgo[1])
        self.CargoTrab.setText(datos[4])
        self.nombreTrab.setText(datos[0])
        self.terminarART.clicked.connect(self.EndART)
        self.nombreSuper()
        self.show()

        self.respuestasPt = []
        self.respuestasRc1 = []
        self.respuestasRc2 = []
        self.contextTrab = []

        self.respuestaTurno = None
        self.seleccionadoSupervisor = None

        self.respuesta_PT1 = None
        self.respuesta_PT2 = None
        self.respuesta_PT3 = None
        self.respuesta_PT4 = None
        self.respuesta_PT5 = None
        self.respuesta_PT6 = None

        self.respuesta_Rc1Pr1 = None
        self.respuesta_Rc1Pr2 = None
        self.respuesta_Rc1Pr3 = None
        self.respuesta_Rc1Pr4 = None
        self.respuesta_Rc1Pr5 = None
        self.respuesta_Rc1Pr6 = None
        self.respuesta_Rc1Pr7 = None
        self.respuesta_Rc1Pr8 = None

        self.respuesta_Rc2Pr1 = None
        self.respuesta_Rc2Pr2 = None
        self.respuesta_Rc2Pr3 = None
        self.respuesta_Rc2Pr4 = None
        self.respuesta_Rc2Pr5 = None
        self.respuesta_Rc2Pr6 = None
        self.respuesta_Rc2Pr7 = None
        self.respuesta_Rc2Pr8 = None

        self.respuesta_trabSimult = None
        self.respuesta_CoordLider = None
        self.respuesta_VerifCCritic = None
        self.respuesta_TSVerificado = None
        self.respuesta_confirCondicion = None

        self.dia.clicked.connect(self.turno)
        self.noche.clicked.connect(self.turno)

        self.nombresSuper.currentIndexChanged.connect(self.ElijeSuper)

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

        self.Rc1Pr1_si.clicked.connect(self.RiesgCrit1Pr1)
        self.Rc1Pr1_no.clicked.connect(self.RiesgCrit1Pr1)
        self.Rc1Pr2_si.clicked.connect(self.RiesgCrit1Pr2)
        self.Rc1Pr2_no.clicked.connect(self.RiesgCrit1Pr2)
        self.Rc1Pr3_si.clicked.connect(self.RiesgCrit1Pr3)
        self.Rc1Pr3_no.clicked.connect(self.RiesgCrit1Pr3)
        self.Rc1Pr4_si.clicked.connect(self.RiesgCrit1Pr4)
        self.Rc1Pr4_no.clicked.connect(self.RiesgCrit1Pr4)
        self.Rc1Pr5_si.clicked.connect(self.RiesgCrit1Pr5)
        self.Rc1Pr5_no.clicked.connect(self.RiesgCrit1Pr5)
        self.Rc1Pr6_si.clicked.connect(self.RiesgCrit1Pr6)
        self.Rc1Pr6_no.clicked.connect(self.RiesgCrit1Pr6)
        self.Rc1Pr7_si.clicked.connect(self.RiesgCrit1Pr7)
        self.Rc1Pr7_no.clicked.connect(self.RiesgCrit1Pr7)
        self.Rc1Pr8_si.clicked.connect(self.RiesgCrit1Pr8)
        self.Rc1Pr8_no.clicked.connect(self.RiesgCrit1Pr8)

        self.Rc2Pr1_si.clicked.connect(self.RiesgCrit2Pr1)
        self.Rc2Pr1_no.clicked.connect(self.RiesgCrit2Pr1)
        self.Rc2Pr2_si.clicked.connect(self.RiesgCrit2Pr2)
        self.Rc2Pr2_no.clicked.connect(self.RiesgCrit2Pr2)
        self.Rc2Pr3_si.clicked.connect(self.RiesgCrit2Pr3)
        self.Rc2Pr3_no.clicked.connect(self.RiesgCrit2Pr3)
        self.Rc2Pr4_si.clicked.connect(self.RiesgCrit2Pr4)
        self.Rc2Pr4_no.clicked.connect(self.RiesgCrit2Pr4)
        self.Rc2Pr5_si.clicked.connect(self.RiesgCrit2Pr5)
        self.Rc2Pr5_no.clicked.connect(self.RiesgCrit2Pr5)
        self.Rc2Pr6_si.clicked.connect(self.RiesgCrit2Pr6)
        self.Rc2Pr6_no.clicked.connect(self.RiesgCrit2Pr6)
        self.Rc2Pr7_si.clicked.connect(self.RiesgCrit2Pr7)
        self.Rc2Pr7_no.clicked.connect(self.RiesgCrit2Pr7)
        self.Rc2Pr8_si.clicked.connect(self.RiesgCrit2Pr8)
        self.Rc2Pr8_no.clicked.connect(self.RiesgCrit2Pr8)

        self.trabSimult_si.clicked.connect(self.trabSimultaneo)
        self.trabSimult_no.clicked.connect(self.trabSimultaneo)

        self.contextoTrabajo1.stateChanged.connect(self.contexto)
        self.contextoTrabajo2.stateChanged.connect(self.contexto)
        self.contextoTrabajo3.stateChanged.connect(self.contexto)
        self.contextoTrabajo4.stateChanged.connect(self.contexto)

        self.CoordLider_si.clicked.connect(self.coordinLider)
        self.CoordLider_no.clicked.connect(self.coordinLider)

        self.VerifCCritic_si.clicked.connect(self.verifCCr)
        self.VerifCCritic_no.clicked.connect(self.verifCCr)        

        self.TSVerificado_si.clicked.connect(self.verifTrab)
        self.TSVerificado_no.clicked.connect(self.verifTrab)

        self.confirCondicion_si.clicked.connect(self.condicionFisica)
        self.confirCondicion_no.clicked.connect(self.condicionFisica)


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

    def nombreSuper(self):
        empleados = self.contr.mostrarSuper()
        for empleado in empleados:
            self.nombresSuper.addItem(empleado)

    def ElijeSuper(self):
        self.seleccionadoSupervisor = self.nombresSuper.currentText()
        print(f"Supervisor seleccionado: {self.seleccionadoSupervisor}")

    def turno(self):
        if self.sender() == self.dia:
            self.respuestaTurno = '20:00:00'
        elif self.sender() == self.noche:
            self.respuestaTurno = '08:00:00'
        print(f"turno: {self.respuestaTurno}")

    def pregunta1(self):
        if self.sender() == self.PT1_si:
            self.respuesta_PT1 = "SI"
        elif self.sender() == self.PT1_no:
            self.respuesta_PT1 = "NO"
        print(f"Pregunta 1: {self.respuesta_PT1}")

    def pregunta2(self):
        if self.sender() == self.PT2_si:
            self.respuesta_PT2 = "SI"
        elif self.sender() == self.PT2_no:
            self.respuesta_PT2 = "NO"
        print(f"Pregunta 2: {self.respuesta_PT2}")

    def pregunta3(self):
        if self.sender() == self.PT3_si:
            self.respuesta_PT3 = "SI"
        elif self.sender() == self.PT3_no:
            self.respuesta_PT3 = "NO"
        print(f"Pregunta 3: {self.respuesta_PT3}")

    def pregunta4(self):
        if self.sender() == self.PT4_si:
            self.respuesta_PT4 = "SI"
        elif self.sender() == self.PT4_no:
            self.respuesta_PT4 = "NO"
        print(f"Pregunta 4: {self.respuesta_PT4}")

    def pregunta5(self):
        if self.sender() == self.PT5_si:
            self.respuesta_PT5 = "SI"
        elif self.sender() == self.PT5_no:
            self.respuesta_PT5 = "NO"
        print(f"Pregunta 5: {self.respuesta_PT5}")

    def pregunta6(self):
        if self.sender() == self.PT6_si:
            self.respuesta_PT6 = "SI"
        elif self.sender() == self.PT6_no:
            self.respuesta_PT6 = "NO"
        print(f"Pregunta 6: {self.respuesta_PT6}")


    def RiesgCrit1Pr1(self):
        if self.sender() == self.Rc1Pr1_si:
            self.respuesta_Rc1Pr1 = "SI"
        elif self.sender() == self.Rc1Pr1_no:
            self.respuesta_Rc1Pr1 = "NO"
        print(f"ResgoCrit1Pregunta 1: {self.respuesta_Rc1Pr1}")

    def RiesgCrit1Pr2(self):
        if self.sender() == self.Rc1Pr2_si:
            self.respuesta_Rc1Pr2 = "SI"
        elif self.sender() == self.Rc1Pr2_no:
            self.respuesta_Rc1Pr2 = "NO"
        print(f"ResgoCrit1Pregunta 2: {self.respuesta_Rc1Pr2}")

    def RiesgCrit1Pr3(self):
        if self.sender() == self.Rc1Pr3_si:
            self.respuesta_Rc1Pr3 = "SI"
        elif self.sender() == self.Rc1Pr3_no:
            self.respuesta_Rc1Pr3 = "NO"
        print(f"ResgoCrit1Pregunta 3: {self.respuesta_Rc1Pr3}")

    def RiesgCrit1Pr4(self):
        if self.sender() == self.Rc1Pr4_si:
            self.respuesta_Rc1Pr4 = "SI"
        elif self.sender() == self.Rc1Pr4_no:
            self.respuesta_Rc1Pr4 = "NO"
        print(f"ResgoCrit1Pregunta 4: {self.respuesta_Rc1Pr4}")

    def RiesgCrit1Pr5(self):
        if self.sender() == self.Rc1Pr5_si:
            self.respuesta_Rc1Pr5 = "SI"
        elif self.sender() == self.Rc1Pr5_no:
            self.respuesta_Rc1Pr5 = "NO"
        print(f"ResgoCrit1Pregunta 5: {self.respuesta_Rc1Pr5}")

    def RiesgCrit1Pr6(self):
        if self.sender() == self.Rc1Pr6_si:
            self.respuesta_Rc1Pr6 = "SI"
        elif self.sender() == self.Rc1Pr6_no:
            self.respuesta_Rc1Pr6 = "NO"
        print(f"ResgoCrit1Pregunta 6: {self.respuesta_Rc1Pr6}")

    def RiesgCrit1Pr7(self):
        if self.sender() == self.Rc1Pr7_si:
            self.respuesta_Rc1Pr7 = "SI"
        elif self.sender() == self.Rc1Pr7_no:
            self.respuesta_Rc1Pr7 = "NO"
        print(f"ResgoCrit1Pregunta 7: {self.respuesta_Rc1Pr7}")

    def RiesgCrit1Pr8(self):
        if self.sender() == self.Rc1Pr8_si:
            self.respuesta_Rc1Pr8 = "SI"
        elif self.sender() == self.Rc1Pr8_no:
            self.respuesta_Rc1Pr8 = "NO"
        print(f"ResgoCrit1Pregunta 8: {self.respuesta_Rc1Pr8}")



    def RiesgCrit2Pr1(self):
        if self.sender() == self.Rc2Pr1_si:
            self.respuesta_Rc2Pr1 = "SI"
        elif self.sender() == self.Rc2Pr1_no:
            self.respuesta_Rc2Pr1 = "NO"
        print(f"ResgoCrit2Pregunta 1: {self.respuesta_Rc2Pr1}")

    def RiesgCrit2Pr2(self):
        if self.sender() == self.Rc2Pr2_si:
            self.respuesta_Rc2Pr2 = "SI"
        elif self.sender() == self.Rc2Pr2_no:
            self.respuesta_Rc2Pr2 = "NO"
        print(f"ResgoCrit2Pregunta 2: {self.respuesta_Rc2Pr2}")

    def RiesgCrit2Pr3(self):
        if self.sender() == self.Rc2Pr3_si:
            self.respuesta_Rc2Pr3 = "SI"
        elif self.sender() == self.Rc2Pr3_no:
            self.respuesta_Rc2Pr3 = "NO"
        print(f"ResgoCrit2Pregunta 3: {self.respuesta_Rc2Pr3}")

    def RiesgCrit2Pr4(self):
        if self.sender() == self.Rc2Pr4_si:
            self.respuesta_Rc2Pr4 = "SI"
        elif self.sender() == self.Rc2Pr4_no:
            self.respuesta_Rc2Pr4 = "NO"
        print(f"ResgoCrit2Pregunta 4: {self.respuesta_Rc2Pr4}")

    def RiesgCrit2Pr5(self):
        if self.sender() == self.Rc2Pr5_si:
            self.respuesta_Rc2Pr5 = "SI"
        elif self.sender() == self.Rc2Pr5_no:
            self.respuesta_Rc2Pr5 = "NO"
        print(f"ResgoCrit2Pregunta 5: {self.respuesta_Rc2Pr5}")

    def RiesgCrit2Pr6(self):
        if self.sender() == self.Rc2Pr6_si:
            self.respuesta_Rc2Pr6 = "SI"
        elif self.sender() == self.Rc2Pr6_no:
            self.respuesta_Rc2Pr6 = "NO"
        print(f"ResgoCrit2Pregunta 6: {self.respuesta_Rc2Pr6}")

    def RiesgCrit2Pr7(self):
        if self.sender() == self.Rc2Pr7_si:
            self.respuesta_Rc2Pr7 = "SI"
        elif self.sender() == self.Rc2Pr7_no:
            self.respuesta_Rc2Pr7 = "NO"
        print(f"ResgoCrit2Pregunta 7: {self.respuesta_Rc2Pr7}")

    def RiesgCrit2Pr8(self):
        if self.sender() == self.Rc2Pr8_si:
            self.respuesta_Rc2Pr8 = "SI"
        elif self.sender() == self.Rc2Pr8_no:
            self.respuesta_Rc2Pr8 = "NO"
        print(f"ResgoCrit2Pregunta 8: {self.respuesta_Rc2Pr8}")


    def trabSimultaneo(self):
        if self.sender() == self.trabSimult_si:
            self.respuesta_trabSimult = 1
        elif self.sender() == self.trabSimult_no:
            self.respuesta_trabSimult = 0
        print(f"respuesta_trabSimult: {self.respuesta_trabSimult}")

    def contexto(self):
        if self.contextoTrabajo1.isChecked():
            if 'Trabajo junto a personal de aseo' not in self.contextTrab:
                self.contextTrab.append('Trabajo junto a personal de aseo')
        else:
            if 'Trabajo junto a personal de aseo' in self.contextTrab:
                self.contextTrab.remove('Trabajo junto a personal de aseo')

        if self.contextoTrabajo2.isChecked():
            if 'Trabajo sala compartida' not in self.contextTrab:
                self.contextTrab.append('Trabajo sala compartida')
        else:
            if 'Trabajo sala compartida' in self.contextTrab:
                self.contextTrab.remove('Trabajo sala compartida')

        if self.contextoTrabajo3.isChecked():
            if 'Trabajo en equipo' not in self.contextTrab:
                self.contextTrab.append('Trabajo en equipo')
        else:
            if 'Trabajo en equipo' in self.contextTrab:
                self.contextTrab.remove('Trabajo en equipo')

        if self.contextoTrabajo4.isChecked():
            if 'Trabajo entre actividades' not in self.contextTrab:
                self.contextTrab.append('Trabajo entre actividades')
        else:
            if 'Trabajo entre actividades' in self.contextTrab:
                self.contextTrab.remove('Trabajo entre actividades')

        print(self.contextTrab)

    def coordinLider(self):
        if self.sender() == self.CoordLider_si:
            self.respuesta_CoordLider = "1"
        elif self.sender() == self.CoordLider_no:
            self.respuesta_CoordLider = "0"
        print(f"respuesta_CoordLider: {self.respuesta_CoordLider}")

    def verifCCr(self):
        if self.sender() == self.VerifCCritic_si:
            self.respuesta_VerifCCritic = "1"
        elif self.sender() == self.VerifCCritic_no:
            self.respuesta_VerifCCritic = "0"
        print(f"respuesta_VerifCCritic: {self.respuesta_VerifCCritic}")
        
    def verifTrab(self):
        if self.sender() == self.TSVerificado_si:
            self.respuesta_TSVerificado = "1"
        elif self.sender() == self.TSVerificado_no:
            self.respuesta_TSVerificado = "0"
        print(f"respuesta_TSVerificado: {self.respuesta_TSVerificado}")

    def condicionFisica(self):
        if self.sender() == self.confirCondicion_si:
            self.respuesta_confirCondicion = 1
        elif self.sender() == self.confirCondicion_no:
            self.respuesta_confirCondicion = 0
        print(f"respuesta_confirCondicion: {self.respuesta_confirCondicion}")

    def EndART(self):
        self.terminarART.setVisible(False)
        resultadosComparacion = True
        nPreguntasR1 = self.contr.sacarNumeroPreguntas(self.riesgoCrit[2])
        self.respuestasPt.append(self.respuesta_PT1)
        self.respuestasPt.append(self.respuesta_PT2)
        self.respuestasPt.append(self.respuesta_PT3)
        self.respuestasPt.append(self.respuesta_PT4)
        self.respuestasPt.append(self.respuesta_PT5)
        self.respuestasPt.append(self.respuesta_PT6)
        self.respuestasRc1.append(self.respuesta_Rc1Pr1)
        self.respuestasRc1.append(self.respuesta_Rc1Pr2)
        self.respuestasRc1.append(self.respuesta_Rc1Pr3)
        self.respuestasRc1.append(self.respuesta_Rc1Pr4)
        self.respuestasRc1.append(self.respuesta_Rc1Pr5)
        if  int(nPreguntasR1) > 5:
            self.respuestasRc1.append(self.respuesta_Rc1Pr6)
            self.respuestasRc1.append(self.respuesta_Rc1Pr7)
            self.respuestasRc1.append(self.respuesta_Rc1Pr8)
        elif self.riesgoCrit[4] != '' :
            nPreguntasR2 = self.contr.sacarNumeroPreguntas(self.riesgoCrit[4])
            self.respuestasRc2.append(self.respuesta_Rc2Pr1)
            self.respuestasRc2.append(self.respuesta_Rc2Pr2)
            self.respuestasRc2.append(self.respuesta_Rc2Pr3)
            self.respuestasRc2.append(self.respuesta_Rc2Pr4)
            self.respuestasRc2.append(self.respuesta_Rc2Pr5)
            self.respuestasRc2.append(self.respuesta_Rc2Pr6)
            self.respuestasRc2.append(self.respuesta_Rc2Pr7)
            print(self.respuestasPt)
            print(self.respuestasRc1)
            print(self.respuestasRc2)
            Rpreguntas = self.contr.mostrarResPreguntas()
            if Rpreguntas == self.respuestasPt:
                Rcrit1Resp = self.contr.mostrarRcRespuestas(self.riesgoCrit[2],self.riesgoCrit[4])
                for elemento in self.respuestasRc1:
                    if elemento != Rcrit1Resp[0]:
                        resultadosComparacion = False
                        break   
                if resultadosComparacion == True:
                    for elemento in self.respuestasRc2:
                        if elemento != Rcrit1Resp[1]:
                            resultadosComparacion = False
                            break   
                    if resultadosComparacion == True:
                        self.contr.crearART(self.rut,self.respuesta_trabSimult,self.riesgoCrit[0],self.respuesta_confirCondicion,self.respuestaTurno)
                        idArtCreado = self.contr.idUltimaARTRut(self.rut)
                        self.contr.incorpora(idArtCreado,1,1)   #self.respuestasPt[0] en el ultimo
                        self.contr.incorpora(idArtCreado,2,1)   #self.respuestasPt[1] en el ultimo
                        self.contr.incorpora(idArtCreado,3,1)   #self.respuestasPt[2] en el ultimo
                        self.contr.incorpora(idArtCreado,4,1)   #self.respuestasPt[3] en el ultimo
                        self.contr.incorpora(idArtCreado,5,1)   #self.respuestasPt[4] en el ultimo
                        self.contr.incorpora(idArtCreado,6,1)   #self.respuestasPt[5] en el ultimo
                        self.contr.actualizarEstadoArt1(str(idArtCreado))
                        if self.respuesta_trabSimult == 0:
                            self.contr.ingresartrabSimut((["No existe trabajo simultaneo"]),"0","0","0",str(idArtCreado))
                            self.contr.asignarSuper(self.seleccionadoSupervisor,str(idArtCreado))
                            self.infoEndArt.setText("ART creada correctamente puede cerrar la pestaña")
                            if self.respuesta_confirCondicion == 0:
                                self.contr.actualizarEstadoArt3(str(idArtCreado))
                                self.infoEndArt.setText("Se notificara targeta verde al supervisor")
                        else:
                            self.contr.ingresartrabSimut((self.contextTrab),(self.respuesta_CoordLider),(self.respuesta_VerifCCritic),(self.respuesta_TSVerificado),(str(idArtCreado)))
                            self.infoEndArt.setText("ART creada correctamente puede cerrar la pestaña")
                            self.contr.asignarSuper(self.seleccionadoSupervisor,str(idArtCreado))
                            if self.respuesta_confirCondicion == 0:
                                self.contr.actualizarEstadoArt3(str(idArtCreado))
                                self.infoEndArt.setText("Se notificara targeta verde al supervisor")
                        print("ART creada correctamente")
                    else:
                        self.contr.crearART(self.rut,self.respuesta_trabSimult,self.riesgoCrit[0],self.respuesta_confirCondicion,self.respuestaTurno)
                        if self.respuesta_trabSimult == 0:
                            idArtCreado = self.contr.idUltimaARTRut(self.rut)
                            self.contr.ingresartrabSimut((["No existe trabajo simultaneo"]),"0","0","0",str(idArtCreado))
                            self.contr.asignarSuper(self.seleccionadoSupervisor,str(idArtCreado))
                        idArtCreado = self.contr.idUltimaARTRut(self.rut)
                        self.contr.actualizarEstadoArt3(str(idArtCreado))
                        self.infoEndArt.setText("Se notificara targeta verde al supervisor")
                        print("no se creo la ART no coincide con las respuestas Rc1")
                else:
                    self.contr.crearART(self.rut,self.respuesta_trabSimult,self.riesgoCrit[0],self.respuesta_confirCondicion,self.respuestaTurno)
                    if self.respuesta_trabSimult == 0:
                        idArtCreado = self.contr.idUltimaARTRut(self.rut)
                        self.contr.ingresartrabSimut((["No existe trabajo simultaneo"]),"0","0","0",str(idArtCreado))
                        self.contr.asignarSuper(self.seleccionadoSupervisor,str(idArtCreado))
                    idArtCreado = self.contr.idUltimaARTRut(self.rut)
                    self.contr.actualizarEstadoArt3(str(idArtCreado))
                    self.infoEndArt.setText("Se notificara targeta verde al supervisor")
                    print("no se creo la ART no coincide con las respuestas Rc2")
                if int(nPreguntasR2) > 7:
                    self.respuestasRc2.append(self.respuesta_Rc2Pr8)
            else:
                self.infoEndArt.setText("No se creo la ART faltan preguntas transversales")
                print("no se creo la ART faltan preguntas transversales")
        else:
            self.respuestasRc2.append(None)
            print(self.respuestasPt)
            print(self.respuestasRc1)
            print(self.respuestasRc2)
            Rpreguntas = self.contr.mostrarResPreguntas()
            if Rpreguntas == self.respuestasPt:
                Rcrit1Resp = self.contr.mostrarRcRespuestas(self.riesgoCrit[2],self.riesgoCrit[4])
                for elemento in self.respuestasRc1:
                    if elemento != Rcrit1Resp[0]:
                        resultadosComparacion = False
                        break   
                if resultadosComparacion == True:
                    self.contr.crearART(self.rut,self.respuesta_trabSimult,self.riesgoCrit[0],self.respuesta_confirCondicion,self.respuestaTurno)
                    idArtCreado = self.contr.idUltimaARTRut(self.rut)
                    self.contr.incorpora(idArtCreado,1,1)   #self.respuestasPt[0] en el ultimo
                    self.contr.incorpora(idArtCreado,2,1)   #self.respuestasPt[1] en el ultimo
                    self.contr.incorpora(idArtCreado,3,1)   #self.respuestasPt[2] en el ultimo
                    self.contr.incorpora(idArtCreado,4,1)   #self.respuestasPt[3] en el ultimo
                    self.contr.incorpora(idArtCreado,5,1)   #self.respuestasPt[4] en el ultimo
                    self.contr.incorpora(idArtCreado,6,1)   #self.respuestasPt[5] en el ultimo
                    self.contr.actualizarEstadoArt1(str(idArtCreado))
                    if self.respuesta_trabSimult == 0:
                        self.contr.ingresartrabSimut((["No existe trabajo simultaneo"]),"0","0","0",str(idArtCreado))
                        self.contr.asignarSuper(self.seleccionadoSupervisor,str(idArtCreado))
                        self.infoEndArt.setText("ART creada correctamente puede cerrar la pestaña")
                        if self.respuesta_confirCondicion == 0:
                            self.contr.actualizarEstadoArt3(str(idArtCreado))
                            self.infoEndArt.setText("Se notificara targeta verde al supervisor")
                    else:
                        self.contr.ingresartrabSimut((self.contextTrab),(self.respuesta_CoordLider),(self.respuesta_VerifCCritic),(self.respuesta_TSVerificado),(str(idArtCreado)))
                        self.infoEndArt.setText("ART creada correctamente puede cerrar la pestaña")
                        self.contr.asignarSuper(self.seleccionadoSupervisor,str(idArtCreado))
                        if self.respuesta_confirCondicion == 0:
                            self.contr.actualizarEstadoArt3(str(idArtCreado))
                            self.infoEndArt.setText("Se notificara targeta verde al supervisor")
                    print("ART creada correctamente")
                else:
                    self.contr.crearART(self.rut,self.respuesta_trabSimult,self.riesgoCrit[0],self.respuesta_confirCondicion,self.respuestaTurno)
                    if self.respuesta_trabSimult == 0:
                        idArtCreado = self.contr.idUltimaARTRut(self.rut)
                        self.contr.ingresartrabSimut((["No existe trabajo simultaneo"]),"0","0","0",str(idArtCreado))
                        self.contr.asignarSuper(self.seleccionadoSupervisor,str(idArtCreado))
                    idArtCreado = self.contr.idUltimaARTRut(self.rut)
                    self.contr.actualizarEstadoArt3(str(idArtCreado))
                    self.infoEndArt.setText("Se notificara tarjeta verde al supervisor")
                    print("no se creo la ART")
            else:
                self.infoEndArt.setText("No se creo la ART faltan preguntas transversales")
                print("no se creo la ART falta preguntas transversales")
                self.hide