class Empleado:
    def __init__(self,Rut,NombreCompleto,Correo,Telefono,DireccionResidencia,Cargo, Contraseña):
        self.__Rut = Rut
        self.__NombreCompleto = NombreCompleto
        self.__Correo = Correo
        self.__Telefono = Telefono
        self.__DireccionResidencia = DireccionResidencia
        self.__Cargo = Cargo
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

    def setContraseña(self,nuevaContraseña):
        self.__Contraseña = nuevaContraseña

class ART:
    def __init__(self,Fecha,HoraInicio,HoraTermino):
        self.__realiza = []
        self.__TrabajoSimultaneo = False
        self.__PreguntaTrabajador = []
        self.__PreguntaSupervisor = []
        self.__EstadoTrabajador = False
        self.__Fecha = Fecha
        self.__HoraInicio = HoraInicio
        self.__HoraTermino = HoraTermino
    
    def getRealiza(self):
        return self.__realiza

    def getTrabajoSimultaneo(self):
        return self.__TrabajoSimultaneo
    
    def getPreguntasTrabajador(self):
        return self.__PreguntasTrabajador
    
    def getEstadoTrabajador(self):
        return self.__EstadoTrabajador
    
    def getPreguntasSupervisor(self):
        return self.__PreguntasSupervisor
    
    def getFecha(self):
        return self.__Fecha
    
    def getHoraInicio(self):
        return self.__HoraInicio
    
    def getHoraTermino(self):
        return self.__HoraTermino
    
    def setRealiza(self,nuevoRealiza):
        self.__realiza = nuevoRealiza
    
    def setTrabajoSimultaneo(self,nuevoTrabajoSimultaneo):
        self.__TrabajoSimultaneo = nuevoTrabajoSimultaneo
    
    def setPreguntaTrabajador(self,nuevaPreguntaTrabajador):
        self.__PreguntaTrabajador = nuevaPreguntaTrabajador
    
    def setPreguntaSupervisor(self,nuevaPreguntaSupervisor):
        self.__PreguntaSupervisor = nuevaPreguntaSupervisor

    def setEstadoTrabajador(self,nuevoEstado):
        self.__EstadoTrabajador = nuevoEstado
    
    def setFecha(self,nuevaFecha):
        self.__Fecha = nuevaFecha
    
    def setHoraInicio(self,nuevaHoraInicio):
        self.__HoraInicio = nuevaHoraInicio
    
    def setHoraTermino(self,nuevaHoraTermino):
        self.__HoraTermino = nuevaHoraTermino
    
class Actividad: 
    def __init__(self,Nombre,Descripcion,Riesgo,MedidaControl):
        self.__Nombre = Nombre
        self.__Descripcion = Descripcion
        self.__Riesgo = Riesgo
        self.__MedidaControl = MedidaControl

    def getNombre(self):
        return self.__Nombre
    
    def getDescripcion(self):
        return self.__Descripcion
    
    def getRiesgo(self):
        return self.__Riesgo
    
    def getMedidaControl(self):
        return self.__MedidaControl
    
    def setNombre(self,nuevoNombre):
        self.__Nombre = nuevoNombre
    
    def setDescripcion(self,nuevaDescripcion):
        self.__Descripcion = nuevaDescripcion
    
    def setRiesgo(self,nuevoRiesgo):
        self.__Riesgo = nuevoRiesgo
    
    def setMedidaControl(self,nuevaMedida):
        self.__MedidaControl = nuevaMedida

class Riego_critico:
    def __init__(self, Nombre,Pregunta,Correcta):
        self.__Nombre = Nombre
        self.__Pregunta = Pregunta
        self.__Correcta = Correcta

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