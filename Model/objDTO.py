class Empleado:
    def __init__(self,Rut,NombreCompleto,Correo,Telefono,DireccionResidencia,Cargo,especialidad, Contraseña):
        self.__Rut = Rut
        self.__NombreCompleto = NombreCompleto
        self.__Correo = Correo
        self.__Telefono = Telefono
        self.__DireccionResidencia = DireccionResidencia
        self.__Cargo = Cargo
        self.__especialidad = especialidad
        self.__Contraseña = Contraseña

    def getRut(self):
        return self.__Rut
    
    def getNombreCompleto(self):
        return self.__NombreCompleto
    
    def getCorreo(self):
        return self.__Correo
    
    def getTelefono(self):
        return self.__Telefono
    
    def getDireccionResidencia(self):
        return self.__DireccionResidencia
    
    def getCargo(self):
        return self.__Cargo

    def getEspecialidad(self):
        return self.__especialidad

    def getContraseña(self):
        return self.__Contraseña
    
    
    def setRut(self,nuevoRut):
        self.__Rut = nuevoRut

    def setNombreCompleto(self,nuevoNombre):
        self.__NombreCompleto = nuevoNombre

    def setCorreo(self,nuevoCorreo):
        self.__Correo = nuevoCorreo

    def setTelefono(self,nuevoTelefono):
        self.__Telefono = nuevoTelefono

    def setDireccionResidencia(self,nuevaResidencia):
        self.__DireccionResidencia = nuevaResidencia

    def setCargo(self,nuevoCargo):
        self.__Cargo = nuevoCargo

    def setEspecialidad(self,nuevaEspecialidad):
        self.__especialidad = nuevaEspecialidad

    def setContraseña(self,nuevaContraseña):
        self.__Contraseña = nuevaContraseña

class ART:
    def __init__(self,trabajoSimultaneo,actividad,estadoTrabajador,horaTermino):
        self.__TrabajoSimultaneo = trabajoSimultaneo
        self.__Actividad = actividad
        self.__EstadoTrabajador = estadoTrabajador
        self.__HoraTermino = horaTermino
    
    def getTrabajoSimultaneo(self):
        return self.__TrabajoSimultaneo

    def getActividad(self):
        return self.__Actividad
    
    def getEstadoTrabajador(self):
        return self.__EstadoTrabajador
    
    def getHoraTermino(self):
        return self.__HoraTermino
    
    def setTrabajoSimultaneo(self,nuevoTrabajoSimultaneo):
        self.__TrabajoSimultaneo = nuevoTrabajoSimultaneo
    
    def setActvidad(self,nuevaActividad):
        self.__Actividad = nuevaActividad

    def setEstadoTrabajador(self,nuevoEstado):
        self.__EstadoTrabajador = nuevoEstado
    
    def setHoraTermino(self,nuevaHoraTermino):
        self.__HoraTermino = nuevaHoraTermino

class Actividad: 
    def __init__(self,nombre,riesgo,medidaControl):
        self.__Nombre = nombre
        self.__Riesgo = riesgo
        self.__MedidaControl = medidaControl

    def getNombre(self):
        return self.__Nombre
    
    def getRiesgo(self):
        return self.__Riesgo
    
    def getMedidaControl(self):
        return self.__MedidaControl
    
    def setNombre(self,nuevoNombre):
        self.__Nombre = nuevoNombre
    
    def setRiesgo(self,nuevoRiesgo):
        self.__Riesgo = nuevoRiesgo
    
    def setMedidaControl(self,nuevaMedida):
        self.__MedidaControl = nuevaMedida

class Riegocritico:
    def __init__(self, nombre,pregunta,respuestaCorrecta):
        self.__Nombre = nombre
        self.__Pregunta = pregunta
        self.__Correcta = respuestaCorrecta

    def getNombre(self):
        return self.__Nombre
    
    def getPregunta(self):
        return self.__Pregunta
    
    def getCorrecta(self): 
        return self.__Correcta
    
    def setNombre(self,nuevoNombre):
        self.__Nombre = nuevoNombre

    def setPregunta(self,nuevaPregunta):
        self.__Pregunta = nuevaPregunta

    def setCorrecta(self,nuevaCorrecta):
        self.__Correcta = nuevaCorrecta
