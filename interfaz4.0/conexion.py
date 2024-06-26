import sqlite3
class Conexion():
    def __init__(self):
        try:
            self.con = sqlite3.connect("wss.db")
            self.crearTablas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        sql_create_table1 = """ CREATE TABLE  empleados
        (id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_completo varchar(30) NOT NULL,
        correo varchar(30) NOT NULL,
        telefono varchar(11) NOT NULL,
        direccion_residencia varchar(35) NOT NULL,
        cargo TEXT varchar(30) NOT NULL,
        rut TEXT,
        contra TEXT)"""
        cur = self.con.cursor()
        cur.execute(sql_create_table1)
        cur.close()
        self.crearSupervisor()

    def crearSupervisor(self):
        try:
            sql_insert = """ INSERT INTO empleados values(
            null,'{}','{}','{}','{}','{}','{}','{}')""".format("pablo_Picasso","xdxd@gmail.com","56528381","La_conchetumare_123","supervisor","123123","qwerqwer")
            cur = self.con.cursor()
            cur.execute(sql_insert)
            self.con.commit()
        except Exception as ex:
            print(ex)

    def conectar(self):
        return self.con