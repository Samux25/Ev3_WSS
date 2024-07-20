import sys 
#sys.path.append("D:/Codigos/Python Desarrollo/Ev3_WSS/Model")
import hashlib as hs
sys.path.append("C:/taller/WSS/Model") #Ruta Tito
from objDTO import *
from objDAO import *

class Controlador: 
    def __init__(self):
        self.BD = BD_WSS()
    
    def inicioSesion(self,rut,ctr):
        ltsIn = []
        verificacion = self.validarRut(rut)
        if verificacion == "Si":
            buena = self.BD.buscarContraseña(rut)
            cargo = self.BD.buscarCargo(rut)
            cont = ctr.encode()
            contra = hs.md5(cont).hexdigest()
            if contra == buena:
                msg = "Sesion Iniciada Correctamente"
                puesto = cargo
                ltsIn.append(msg)
                ltsIn.append(puesto)
            else:
                msg = "La credencial ingresada no es valida"
                ltsIn.append(msg)
        else: 
            msg = "La Credencial ingresada no es valida"
            ltsIn.append(msg)
        return ltsIn
    
    def validarFecha(self,fecha):
        resultado = self.BD.buscarFecha(fecha)
        return resultado 

    def validarRut(self,rut):
        resultado = self.BD.buscarRut(rut)
        return resultado
    
    def buscarCorreo(self,correo):
        resultado = self.BD.buscarCorreo(correo)
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
    
    def agregarEmpleado(self,rut,nombre,correo,telefono,direccionResidencia,cargo,especialidad,contraseña):
        sinRut = rut.replace(" ","")
        ctr = contraseña.encode()
        cont = hs.md5(ctr).hexdigest()
        if len(sinRut) <9: 
            msg = "La credencial ingresada tiene menos de 9 Caracteres"
        elif len(sinRut) >9:
            msg = "La credencial ingresada contiene mas de 9 Catacteres"
        else: 
            verificacion = self.validarRut(sinRut)
            if verificacion != "Si":
                nuevo = Empleado(sinRut,nombre,correo,telefono,direccionResidencia,cargo,especialidad,cont)
                self.BD.crearEmpleado(nuevo)
                msg = "Empleado Agregado"
            else:
                msg = 'Este empleado ya se encuentra Contratado'
        return msg
    
    def actualizarInformacion(self,rut,campo,dato):
        verificacion = self.validarRut(rut)
        if verificacion == "Si":
            self.BD.actualizarDatos(rut,campo,dato)
            msg = 'Datos Actualizados Correctamente'
        else:
            msg = 'La Credencial ingresada no es valida'
        return msg
    
    def visualizarEmpleadoRut(self,rut):
        verificacion = self.validarRut(rut)
        if verificacion == "Si":
            datos = self.BD.visualizarEmpleadoRut(rut)
        else : 
            datos = "No se puede cargar la informacion"
        return datos
    
    def visualizarRiesgoActividad(self,nombre):
        resultado = self.BD.visualizarRiesgoActividad(nombre)
        return resultado
    
    def visualizarControlRiesgo(self,nombre):
        resultado = self.BD.visualizarControlRiesgo(nombre)
        return resultado
    
    def sacarNumeroPreguntas(self,nombre):
        resultado = self.BD.sacarNumeroPreguntas(nombre)
        return resultado
    
    def mostrarTrabajadores(self):
        resultado = self.BD.mostrarTrabajadores()
        return resultado
    
    def mostrarARTCreadas(self,supervisor):
        resultado = self.BD.mostrarARTCreadas(supervisor)
        return resultado
    
    def mostrarARTporActividad(self,nombre,supervisor):
        resultados = self.BD.mostrarARTporActividad(nombre,supervisor)
        return resultados
    
    def mostrarSuper(self):
        resultados = self.BD.mostrarSuper()
        return resultados
    
    def mostrarRcRespuestas(self, nombre, nombre2):
        resultados = self.BD.mostrarRcRespuestas(nombre, nombre2)
        return resultados

    def mostrarResPreguntas(self):
        resultados = self.BD.mostrarResPreguntas()
        return resultados
    
    def idUltimaARTRut(self,rut):
        resultados = self.BD.idUltimaARTRut(rut)
        return resultados
    
    def incorpora(self, id_art, id_pregunta, respuesta):
        resultados = self.BD.incorpora(id_art, id_pregunta, respuesta)
        return resultados
    
    def actualizarEstadoArt1(self,id_ART):
        resultados = self.BD.actualizarEstadoArt1(id_ART)
        return resultados
    
    def actualizarEstadoArt2(self,id_ART):
        resultados = self.BD.actualizarEstadoArt2(id_ART)
        return resultados
    
    def actualizarEstadoArt3(self,id_ART):
        resultados = self.BD.actualizarEstadoArt3(id_ART)
        return resultados
    
    def actualizarEstadoArt4(self,id_ART):
        resultados = self.BD.actualizarEstadoArt4(id_ART)
        return resultados
    
    def ingresartrabSimut(self,contexto, coordinacion, verif_control, comuni_tab, id_ART):
        resultados = self.BD.ingresartrabSimut(contexto, coordinacion, verif_control, comuni_tab, id_ART)
        return resultados
    
    def filtroRut(self,rut):
        resultados = self.BD.filtroRut(rut)
        return resultados
    
    def filtroFecha(self,supervisor,fecha):
        resultados = self.BD.filtroFecha(supervisor,fecha)
        return resultados
    
    def filtrotarjetaVerde(self,supervisor):
        resultados = self.BD.filtrotarjetaVerde(supervisor)
        return resultados
    
    def validarContraseña(self,rut ,contraseña):
        cont = contraseña.encode()
        ctrs = hs.md5(cont).hexdigest()
        msg = "Valida"
        if ctrs == self.BD.buscarContraseña(rut):
            msg = "Valido"
        else:
            msg = "Invalida"
        return msg

    def cambiarContraseña(self,rut,ctr, nuevaCtrl):
        verificacion = self.validarRut(rut)
        cont = nuevaCtrl.encode()
        print(cont)
        ctrn = hs.md5(cont).hexdigest()
        print(ctrn)
        veriContra = self.validarContraseña(rut, ctr)
        if verificacion == "Si":
            if veriContra == "Valido":
                self.BD.cambiarContraseña(ctrn,rut)
                msg = "La Contraseña a sido cambiada Correctamente"
            else:
                msg = "La Credencial Ingresada no es Valida "
        else:
            msg = "La Credencial Ingresada no es Valida"
        return msg

    def asignarSuper(self,nombre,id_ART):
        resultados = self.BD.asignarSuper(nombre,id_ART)
        return resultados



c = Controlador()
print(c.cambiarContraseña("187697653","holaquehace","hola"))