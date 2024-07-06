import sys 
sys.path.append("D:/Codigos/WSS/Model")
from objDTO import *
from objDAO import *

class Controlador: 
    def __init__(self):
        self.BD = BD_WSS()
    
    def validarFecha(self,fecha):
        resultado = self.BD.buscarFecha(fecha)
        return resultado 

    def validarRut(self,rut):
        resultado = self.BD.buscarRut(rut)
        return resultado

    def visualizarEmpleados(self):
        return self.BD.visualizarEmpleados()

    def visualizarARTS(self):
        return self.BD.visualizarARTS()

    def visualizarPorRut(self,rut):
        validacion = self.validarRut(rut)
        if validacion == "Si":
            msg = self.BD.visualizarPorRut(rut)
        else: 
            msg = 'La Credencial ingresada no es Valida'
        return msg


    def visualizarPorFecha(self,Fecha):
        verificacion = self.validarFecha(Fecha)
        if verificacion == "Si":
            msg = self.BD.visualizarPorFecha(Fecha)
        else: 
            msg = 'No hay ninguna ART creada en esa fecha'
        return msg

    def sacarIdActividad(self,actividad):
        return self.BD.sacarIdActividad(actividad)

    def crearART(self,rut,trabajoSimultaneo,Actividad,estadoTrabajador,horaTermino):
        verificacion = self.validarRut(rut)
        if verificacion == "Si":
            idActividad = self.sacarIdActividad(Actividad)
            tbs = int(trabajoSimultaneo)
            est = int(estadoTrabajador)
            nueva = ART(tbs,idActividad,est,horaTermino)
            self.BD.crearArt(nueva,rut)
            msg = 'ART Agregada'
        else: 
            msg =  'La Credencial Ingresada no es valida'

        return msg
    
    def agregarEmpleado(self,rut,nombre,correo,telefono,direccionResidencia,cargo,contraseña):
        sinRut = rut.replace(" ","")
        if len(sinRut) <9: 
            msg = "La credencial ingresada tiene menos de 9 Caracteres"
        elif len(sinRut) >9:
            msg = "La credencial ingresada contiene mas de 9 Catacteres"
        else: 
            verificacion = self.validarRut(sinRut)
            if verificacion != "Si":
                nuevo = Empleado(sinRut,nombre,correo,telefono,direccionResidencia,cargo,contraseña)
                self.BD.crearEmpleado(nuevo)
                msg = "Empleado Agregado"
            else:
                msg = 'Este empleado ya se encuentra Contratado'
        return msg
    
    def actualizarInformacion(self,rut,campo,dato):
        verificacion = self.validarRut(rut)
        if verificacion == "Si":
            self.BD.actualizarDatos()
            msg = 'Datos Actualizados Correctamente'
        else:
            msg = 'La Credencial ingresada no es valida'
        return msg

C = Controlador()