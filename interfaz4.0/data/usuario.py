import conexion as con
from model.user import empleado

class userData():
    def login(self, user:empleado):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        res = self.cursor.execute("""SELECT * FROM empleados WHERE cargo='{}' AND rut = '{}' AND contra='{}'""".format("trabajador",user._rut,user._contra))
        fila = res.fetchone()
        if fila:
            user = empleado(cargo=fila[5],rut=[6],contra=[7])
            self.cursor.close()
            self.db.close()
            return user
        else:
            self.cursor.close()
            self.db.close()
            return None
    
    def loginSuper(self, user:empleado):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        res = self.cursor.execute("""SELECT * FROM empleados WHERE cargo='{}' AND rut = '{}' AND contra='{}'""".format("supervisor",user._rut,user._contra))
        fila = res.fetchone()
        if fila:
            user = empleado(cargo=fila[5],rut=[6],contra=[7])
            self.cursor.close()
            self.db.close()
            return user
        else:
            self.cursor.close()
            self.db.close()
            return None