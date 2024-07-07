from pymysql import * 
from objDTO import * 
class BD_WSS:
    def __init__(self):
        self.conector = connect(
            host='localhost',
            user='root',
            password='',
            db='wss_db4')
        self.cursor = self.conector.cursor()

    def login(self, objDTO: empleado):
        sql = """SELECT * FROM empleado WHERE cargo=%s AND rut=%s AND contraseña=%s"""
        self.cursor.execute(sql, ("Trabajador", objDTO.getRut2(), objDTO.getContrasena2()))
        fila = self.cursor.fetchone()
        if fila:
            user = empleado(Cargo=fila[0], Rut=fila[1], Contrasena=fila[2])
            return user
        return None

    def loginSuper(self, objDTO: empleado):
        sql = """SELECT * FROM empleado WHERE cargo=%s AND rut=%s AND contraseña=%s"""
        self.cursor.execute(sql, ("Supervisor", objDTO.getRut2(), objDTO.getContrasena2()))
        fila = self.cursor.fetchone()
        if fila:
            user = empleado(Cargo=fila[0], Rut=fila[1], Contrasena=fila[2])
            return user
        return None

    def buscarRut(self,rut):
        sql = "SELECT rut From empleado WHERE rut = '"+rut+"'"
        try:
            self.cursor.execute(sql)
            Empleado = self.cursor.fetchone()
            if Empleado != None: 
                msg = "Si"
            else: 
                msg = 'No'
        except Exception as ex:
            msg = "Error: " +str(ex.args)
        return msg

    def buscarFecha(self,fecha):
        sql = "SELECT fecha From ver_arts WHERE fecha = '"+fecha+"'"
        try:
            self.cursor.execute(sql)
            fechas = self.cursor.fetchall()
            if len(fechas) != 0:
                msg = "Si"
            else: 
                msg = 'No'
        except Exception as ex:
            msg = "Error: " +str(ex.args)
        return msg
    
    def sacarIdActividad(self,actividad):
        sql = "select id_actividad from actividad where '"+ actividad + "' = nombre;"
        try: 
            self.cursor.execute(sql)
            IdActividad = self.cursor.fetchone()
            if IdActividad != None:
                return IdActividad[0]
            else: 
                print("No hay ninguna actividad con ese nombre")
        except Exception as ex:
            print("Error: " + str(ex.args))

    def idUltimaART(self):
        sql = "SELECT * FROM  art ORDER BY id_art DESC LIMIT 1;"
        try:
            self.cursor.execute(sql)
            ART = self.cursor.fetchone()
            if ART != None:
                return ART[0]
            else: 
                return "No hay ninguna ART ingresada"
        except Exception as ex:
            print("Error: " + str(ex.args))
    
    def realiza(self,rut):
        idART = self.idUltimaART()
        sql = "INSERT INTO realiza(rut, id_ART, fecha) VALUES ('"+rut+"','"+str(idART)+"', CURDATE());"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
        except Exception as ex:
            msg = "Error en realiza: " +str(ex.args)
        return msg

    def crearArt(self,nueva,rut):
        msg = "ART Creada Correctamente"
        sql = "INSERT INTO art(trabajo_simultaneo, id_actividad, estado_trabajador, hora_inicio, hora_termino) VALUES ('"+str(nueva.getTrabajoSimultaneo())+"', '"+str(nueva.getActividad())+"','"+str(nueva.getEstadoTrabajador())+"', DATE_FORMAT(NOW(), '%H:%i:%S') ,'"+str(nueva.getHoraTermino())+"');"
        try: 
            self.cursor.execute(sql)
            self.conector.commit()
            self.realiza(rut)
        except Exception as ex:
            msg = "Error : " + str(ex.args)
        return msg

    def crearEmpleado(self,nuevo):
        sql = "INSERT INTO empleado(rut,nombre_completo,correo,telefono,direccion_residencia,cargo,contraseña) VALUES ('"+nuevo.getRut()+"', '"+nuevo.getNombreCompleto()+"','"+nuevo.getCorreo()+"','"+str(nuevo.getTelefono())+"', '"+nuevo.getDireccionResidencia()+"','"+nuevo.getCargo()+"','"+nuevo.getContraseña()+"');"
        msg = "El empleado a sido creado Correctamente"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
        except Exception as ex:
            msg = "Error: " + str(ex.args)
        return msg
    
    def crearActividad(self,nombre,riesgo,medidaControl):
        sql = "INSERT INTO actividad (nombre,riesgo,medida_control) VALUES ('"+nombre+"','"+riesgo+"','"+medidaControl+"');"
        msg = "Actividad Agregada Correctamente"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
        except Exception as ex:
            msg = "Error: " + str(ex.args)
        return msg
    
    def visualizarEmpleados(self):
        sql = "SELECT * FROM empleado"
        try:
            self.cursor.execute(sql)
            Empleados = self.cursor.fetchall()
            if len(Empleados) != 0:
                for Empleado in Empleados:
                    print("Rut                 : " + Empleado[0])
                    print("Nombre              : " + Empleado[1])
                    print("Correo              : " + Empleado[2])
                    print("Telefono            : " + str(Empleado[3]))
                    print("Direccion Residencia: " + Empleado[4])
                    print("Cargo               : " + Empleado[5])
                    print("\n")
            else: 
                print("Credenciales incorrectas")
        except Exception as ex:
            print("Error: " + str(ex.args))


    def visualizarARTS(self):
        sql = "SELECT * FROM ver_arts;"
        try:
            self.cursor.execute(sql)
            ARTS = self.cursor.fetchall()
            if len(ARTS) != 0:
                for ART in ARTS:
                    print("Rut             : " + ART[0])
                    print("Nombre Completo : " + ART[1])
                    print("Fecha           : " + str(ART[2]))
                    print("Hora Inicio     : " + str(ART[3]))
                    print("Hora Termino    : " + str(ART[4]))
                    if ART[5] == 1: 
                        TrabajoSimultaeno = "Si contiene Trabajo Simultaneo "
                    else:
                        TrabajoSimultaeno = "No contiene trabajo Simultaneo "
                    print(TrabajoSimultaeno)
                    print("Nombre Actividad: " + ART[6])
                    if ART[7] == 1: 
                        estado = "esta en buen estado"
                    else:
                        estado = "NO esta en buen estado "
                    print("El trabajador   : " + estado)
                    print("Cargo           : "+ ART[8])
                    print("\n")
            else:
                print("No hay ninguna ART en el sistema")
        except Exception as ex:
            print("Error: " + str(ex.args))

    def visualizarPorRut(self,rut):
        sql = "select * from ver_arts va where '"+rut+"' = rut ;"
        try:
            self.cursor.execute(sql)
            ARTS = self.cursor.fetchall()
            if len(ARTS) != 0:
                for ART in ARTS:
                    print("Rut             : " + ART[0])
                    print("Nombre Completo : " + ART[1])
                    print("Fecha           : " + str(ART[2]))
                    print("Hora Inicio     : " + str(ART[3]))
                    print("Hora Termino    : " + str(ART[4]))
                    if ART[5] == 1: 
                        TrabajoSimultaeno = "Si contiene Trabajo Simultaneo "
                    else:
                        TrabajoSimultaeno = "No contiene trabajo Simultaneo "
                    print(TrabajoSimultaeno)
                    print("Nombre Actividad: " + ART[6])
                    if ART[7] == 1: 
                        estado = "esta en buen estado"
                    else:
                        estado = "NO esta en buen estado "
                    print("El trabajador   : " + estado)
                    print("Cargo           : "+ ART[8])
                    print("\n")
            else:
                print("No hay ninguna ART con ese RUT")
        except Exception as ex:
            print("Error: " + str(ex.args))

    def visualizarPorFecha(self,Fecha):
        sql = "select * from ver_arts va where '"+Fecha+"' = fecha ;"
        try:
            self.cursor.execute(sql)
            ARTS = self.cursor.fetchall()
            if len(ARTS) != 0:
                for ART in ARTS:
                    print("Rut             : " + ART[0])
                    print("Nombre Completo : " + ART[1])
                    print("Fecha           : " + str(ART[2]))
                    print("Hora Inicio     : " + str(ART[3]))
                    print("Hora Termino    : " + str(ART[4]))
                    if ART[5] == 1: 
                        TrabajoSimultaeno = "Si contiene Trabajo Simultaneo "
                    else:
                        TrabajoSimultaeno = "No contiene trabajo Simultaneo "
                    print(TrabajoSimultaeno)
                    print("Nombre Actividad: " + ART[6])
                    if ART[7] == 1: 
                        estado = "esta en buen estado"
                    else:
                        estado = "NO esta en buen estado "
                    print("El trabajador   : " + estado)
                    print("Cargo           : "+ ART[8])
                    print("\n")
            else:
                print("No hay ninguna ART con ese RUT")
        except Exception as ex:
            print("Error: " + str(ex.args))
    
    def actualizarDatos(self,rut,campo,dato):
        msg = "Dato Actualizado"
        sql = "UPDATE empleado SET "+campo+" = '"+dato+"' WHERE rut = "+rut+""
        try:
            self.cursor.execute(sql)
            self.conector.commit()
        except Exception as ex:
            msg =  "Error: " + str(ex.args)
        return msg 