from pymysql import * 
class UsuarioBD:
    def __init__(self):
        self.conector = connect(
            host='localhost',
            user='root',
            password='',
            db='wss')
        self.cursor = self.conector.cursor()
         
    def verUsuarios(self):
        sql = "SELECT * FROM Empleado"
        try: 
            self.cursor.execute(sql)
            Empleados = self.cursor.fetchall()
            if len(Empleados) != 0:
                for empleado in Empleados:
                    print("Id                  : " + str(empleado[0]))
                    print("Nombre              : " + empleado[1])
                    print("Correo              : " + empleado[2])
                    print("Telefono            : " +str(empleado[3]))
                    print("Direccion_Residencia: " +empleado[4])
                    print("Cargo               : " +empleado[5])
            else: 
                print("No hay ningun trabajador")
        except Exception as ex:
            print("Error: " + str(ex.args))
        
    def verUsuario(self,rut):
        sql = "SELECT * FROM empleado WHERE empleado.rut = '"+rut+"'"
        try:
            self.cursor.execute(sql)
            Usuario = self.cursor.fetchone()
            if Usuario != None:
                    print("Id                  : " + str(Usuario[0]))
                    print("Nombre              : " + Usuario[1])
                    print("Correo              : " + Usuario[2])
                    print("Telefono            : " + str(Usuario[3]))
                    print("Direccion_Residencia: " + Usuario[4])
                    print("Cargo               : " + Usuario[5])
            else: 
                print("No hay ningun empleado con ese Rut")
        except Exception as ex:
            print("Error: " + str(ex.args))
    def verARTS(self):
        sql = "SELECT * FROM art"
        try: 
            self.cursor.execute(sql)
            ARTS = self.cursor.fetchall()
            if len(ARTS) != 0:
                for art in ARTS: 
                    print ("id                 : " +str(art[0]))
                    if art[1] == 1:
                        resultado = "apto"
                    print("Trabajo Simultaneo  : " +resultado)
                    print("id Actividad        : " +str(art[2]))
                    print("Preguntas Trabajador: " +art[3])
                    if art[4] == 1:
                        resultado = "apto"
                    print("Estado Trabajador   : " + resultado)
                    print("Preguntas Supervisor: "+ art[5])
                    print("Fecha               : " +str(art[6]))
                    print("Hora Inicio         : " +str(art[7]))
                    print("Hora Termino        : "+ str(art[8]))
            else: 
                print("No hay ninguna ART")
        except Exception as ex:
            print("Error: " + str(ex.args))
    
    def verActividades(self):
        sql = "SELECT * FROM actividad"
        try: 
            self.cursor.execute(sql)
            Actividades = self.cursor.fetchall()
            if len(Actividades) != 0:
                for actividad in Actividades:
                    print("Actividad        : " +str(actividad[0]))
                    print("Nombre           : "+actividad[1])
                    print("Riesgo           : "+actividad[2])
                    print("Medida de Control: "+actividad[3])
            else: 
                print("No Hay ninguna actividad")
        except Exception as ex:
            print("Error: " + str(ex.args))
    
    def verRiesgosCriticos(self):
        sql = "SELECT * FROM riesgocritico"
        try: 
            self.cursor.execute(sql)
            Riesgos = self.cursor.fetchall()
            if len(Riesgos) != 0: 
                for riesgo in Riesgos:
                    print("Id           : " +str(riesgo[0]))
                    print("Nombre       : " + riesgo[1])
                    print("Pregunta     : "+ riesgo[2])
                    if riesgo[3] == 1:
                        rp = "Apto"
                    print("Respuesta Correcta: "+ rp)
            else: 
                print("No hay ningun Riesgo Critico")
        except Exception as ex:
            print("Error: " +str(ex.args))
    
    def sacarIdActividad(self,actividad):
        sql = "select id_actividad from actividad where '"+ actividad + "' = nombre"
        try: 
            self.cursor.execute(sql)
            IdActividad = self.cursor.fetchone()
            if IdActividad != None:
                return IdActividad
            else: 
                print("No hay ninguna actividad con ese nombre")
        except Exception as ex:
            print("Error: " + str(ex.args))