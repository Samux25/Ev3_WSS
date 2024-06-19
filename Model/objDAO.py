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
                for dt in Empleados:
                    print("Id                  : " + str(dt[0]))
                    print("Nombre              : " + dt[1])
                    print("Correo              : " + dt[2])
                    print("Telefono            : " +str(dt[3]))
                    print("Direccion_Residencia: " +dt[4])
                    print("Cargo               : " +dt[5])
            else: 
                print("No hay ningun trabajador")
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

u = UsuarioBD()
u.verUsuarios()
u.verARTS()
u.verActividades()
u.verRiesgosCriticos()