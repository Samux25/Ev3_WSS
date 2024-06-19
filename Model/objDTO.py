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
    

class realiza:
    def __init__(self):
        self.__RutEmpleado = []
        self.__IdArt = []

class ART:
    def __init__(self,Fecha,HoraInicio,HoraTermino):
        self.__TrabajoSimultaneo = False
        self.__PreguntasTrabajador = {}
        self.__EstadoTrabajador = False
        self.__PreguntasSupervisor = {}
        self.__Fecha = Fecha
        self.__HoraInicio = HoraInicio
        self.__HoraTermino = HoraTermino

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


class Riego_critico:
    def __init__(self, Nombre):
        self.__Nombre = Nombre
        self.__Pregunta = {}

    def getNombre(self):
        return self.__Nombre
    
    def getPregunta(self):
        return self.__Pregunta

class pregunta_rc:
    def __init__(self, Pregunta):
        self.__Pregunta = Pregunta
        self.__Respuesta = {}

    def getPregunta(self):
        return self.__Pregunta

    def getRespuesta(self):
        return self.__Respuesta