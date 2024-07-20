# Form implementation generated from reading ui file 'añadirEmpleado.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 649)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(parent=self.frame)
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 26))
        self.frame_superior.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame_superior)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_minimize = QtWidgets.QPushButton(parent=self.frame_superior)
        self.bt_minimize.setMinimumSize(QtCore.QSize(0, 20))
        self.bt_minimize.setMouseTracking(False)
        self.bt_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/minimizar-ventana.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_minimize.setIcon(icon)
        self.bt_minimize.setObjectName("bt_minimize")
        self.horizontalLayout.addWidget(self.bt_minimize)
        self.bt_maximize = QtWidgets.QPushButton(parent=self.frame_superior)
        self.bt_maximize.setMinimumSize(QtCore.QSize(0, 20))
        self.bt_maximize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/expandir.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_maximize.setIcon(icon1)
        self.bt_maximize.setObjectName("bt_maximize")
        self.horizontalLayout.addWidget(self.bt_maximize)
        self.bt_normal = QtWidgets.QPushButton(parent=self.frame_superior)
        self.bt_normal.setMinimumSize(QtCore.QSize(0, 20))
        self.bt_normal.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/comprimir.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_normal.setIcon(icon2)
        self.bt_normal.setObjectName("bt_normal")
        self.horizontalLayout.addWidget(self.bt_normal)
        self.bt_close = QtWidgets.QPushButton(parent=self.frame_superior)
        self.bt_close.setMinimumSize(QtCore.QSize(0, 20))
        self.bt_close.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/x/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bt_close.setIcon(icon3)
        self.bt_close.setObjectName("bt_close")
        self.horizontalLayout.addWidget(self.bt_close)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(80, 10, 500, 600))
        self.frame_4.setMinimumSize(QtCore.QSize(400, 600))
        self.frame_4.setMaximumSize(QtCore.QSize(500, 500))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(148, 148, 148);\n"
"color:rgb(247, 247, 247);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_8 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.rutEmplNuevo = QtWidgets.QLineEdit(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rutEmplNuevo.setFont(font)
        self.rutEmplNuevo.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(148,148,148);\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.rutEmplNuevo.setObjectName("rutEmplNuevo")
        self.verticalLayout_3.addWidget(self.rutEmplNuevo)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.nombreEmplNuevo = QtWidgets.QLineEdit(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nombreEmplNuevo.setFont(font)
        self.nombreEmplNuevo.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(148,148,148);\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.nombreEmplNuevo.setObjectName("nombreEmplNuevo")
        self.verticalLayout_3.addWidget(self.nombreEmplNuevo)
        self.label_7 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.direcEmplNuevo = QtWidgets.QLineEdit(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.direcEmplNuevo.setFont(font)
        self.direcEmplNuevo.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(148,148,148);\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.direcEmplNuevo.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.direcEmplNuevo.setObjectName("direcEmplNuevo")
        self.verticalLayout_3.addWidget(self.direcEmplNuevo)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.telefonoEmplNuevo = QtWidgets.QLineEdit(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.telefonoEmplNuevo.setFont(font)
        self.telefonoEmplNuevo.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(148,148,148);\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.telefonoEmplNuevo.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.telefonoEmplNuevo.setObjectName("telefonoEmplNuevo")
        self.verticalLayout_3.addWidget(self.telefonoEmplNuevo)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.CorreoEmplNuevo = QtWidgets.QLineEdit(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CorreoEmplNuevo.setFont(font)
        self.CorreoEmplNuevo.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(148,148,148);\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.CorreoEmplNuevo.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.CorreoEmplNuevo.setObjectName("CorreoEmplNuevo")
        self.verticalLayout_3.addWidget(self.CorreoEmplNuevo)
        self.label_10 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cargoTrabajador = QtWidgets.QRadioButton(parent=self.frame_4)
        self.cargoTrabajador.setObjectName("cargoTrabajador")
        self.horizontalLayout_2.addWidget(self.cargoTrabajador, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.cargoSupervisor = QtWidgets.QRadioButton(parent=self.frame_4)
        self.cargoSupervisor.setObjectName("cargoSupervisor")
        self.horizontalLayout_2.addWidget(self.cargoSupervisor, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.EspecialidadEmplNuevo = QtWidgets.QLineEdit(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.EspecialidadEmplNuevo.setFont(font)
        self.EspecialidadEmplNuevo.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(148,148,148);\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.EspecialidadEmplNuevo.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.EspecialidadEmplNuevo.setObjectName("EspecialidadEmplNuevo")
        self.verticalLayout_3.addWidget(self.EspecialidadEmplNuevo)
        self.label_9 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.contrasenaEmplNuevo = QtWidgets.QLineEdit(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.contrasenaEmplNuevo.setFont(font)
        self.contrasenaEmplNuevo.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(148,148,148);\n"
"border-radius: 3px;\n"
"}\n"
"")
        self.contrasenaEmplNuevo.setObjectName("contrasenaEmplNuevo")
        self.verticalLayout_3.addWidget(self.contrasenaEmplNuevo)
        spacerItem2 = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.lblmss = QtWidgets.QLabel(parent=self.frame_4)
        self.lblmss.setText("")
        self.lblmss.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblmss.setObjectName("lblmss")
        self.verticalLayout_3.addWidget(self.lblmss)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.anadirEmpleado = QtWidgets.QPushButton(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.anadirEmpleado.setFont(font)
        self.anadirEmpleado.setStyleSheet("QPushButton {\n"
"border-radius: 8px;\n"
"border: 2px solid rgb(148,148,148);\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.anadirEmpleado.setObjectName("anadirEmpleado")
        self.verticalLayout_3.addWidget(self.anadirEmpleado)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nuevo Empleado"))
        self.label_2.setText(_translate("MainWindow", "Añadir un nuevo Empleado"))
        self.label_8.setText(_translate("MainWindow", "Rut"))
        self.label_3.setText(_translate("MainWindow", "Nombre Completo"))
        self.label_7.setText(_translate("MainWindow", "Dirección de residencia"))
        self.label_6.setText(_translate("MainWindow", "Teléfono"))
        self.label_4.setText(_translate("MainWindow", "Correo"))
        self.label_10.setText(_translate("MainWindow", "Cargo"))
        self.cargoTrabajador.setText(_translate("MainWindow", "Trabajador"))
        self.cargoSupervisor.setText(_translate("MainWindow", "Supervisor"))
        self.label_5.setText(_translate("MainWindow", "Especialidad"))
        self.label_9.setText(_translate("MainWindow", "Contraseña"))
        self.anadirEmpleado.setText(_translate("MainWindow", "Anadir Empleado"))