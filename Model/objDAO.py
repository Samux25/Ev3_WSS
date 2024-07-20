from pymysql import * 
from objDTO import * 
class BD_WSS:
    def __init__(self):
        self.conector = connect(
            host='localhost',
            user='root',
            password='',
            db='wss')
        self.cursor = self.conector.cursor()
    
    def buscarContraseña(self,rut):
        sql = "SELECT contraseña FROM empleado WHERE rut = '"+rut+"'"
        try: 
            self.cursor.execute(sql)
            Contraseña = self.cursor.fetchone()
            if Contraseña != None:
                msg = Contraseña[0]
            else:
                msg = "Las credenciales son incorrectas"
        except Exception as ex:
            msg = "Error: " +str(ex.args)
        return msg

    def buscarCargo(self,rut):
        sql = "SELECT cargo FROM empleado WHERE rut = '"+rut+"'"
        try: 
            self.cursor.execute(sql)
            Cargo = self.cursor.fetchone()
            if Cargo != None:
                msg = Cargo[0]
            else:
                msg = "Las credenciales son incorrectas"
        except Exception as ex:
            msg = "Error: " +str(ex.args)
        return msg

    def buscarRut(self,rut):
        sql = "SELECT rut FROM empleado WHERE rut = '"+rut+"'"
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
    
    def buscarCorreo(self,correo):
        sql = "SELECT correo FROM empleado WHERE correo = '"+correo+"'"
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
        sql = "SELECT fecha FROM ver_arts WHERE fecha = '"+fecha+"'"
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
        sql = "INSERT INTO empleado(rut,nombre_completo,correo,telefono,direccion_residencia,cargo, especialidad, contraseña) VALUES ('"+nuevo.getRut()+"', '"+nuevo.getNombreCompleto()+"','"+nuevo.getCorreo()+"','"+str(nuevo.getTelefono())+"', '"+nuevo.getDireccionResidencia()+"','"+nuevo.getCargo()+"','"+nuevo.getEspecialidad()+"','"+nuevo.getContraseña()+"')"
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
    
    def visualizarEmpleadoRut(self,rut):
        datos = []
        sql = "SELECT nombre_completo, direccion_residencia, telefono, correo, especialidad FROM empleado WHERE rut = '"+rut+"'"
        try : 
            self.cursor.execute(sql)
            Empleado = self.cursor.fetchone()
            if Empleado != None:
                datos.append(Empleado[0])
                datos.append(Empleado[1])
                datos.append(Empleado[2])
                datos.append(Empleado[3])
                datos.append(Empleado[4])
        except Exception as ex:
            msg  = "Error: " + str(ex.args)
            datos.append(msg)
        return datos
    
    def visualizarRiesgoActividad(self, nombre):
        datoRiesgo = []
        sql = "SELECT actividad.nombre, GROUP_CONCAT(posee.id_riesgoCritico ORDER BY posee.id_riesgoCritico), GROUP_CONCAT(riesgocritico.nombre ORDER BY posee.id_riesgoCritico) FROM posee INNER JOIN actividad ON posee.id_actividad = actividad.id_actividad INNER JOIN riesgocritico ON posee.id_riesgoCritico = riesgocritico.id_riesgoCritico WHERE actividad.nombre = '"+nombre+"'"
        try:
            self.cursor.execute(sql)
            riesgoCritico = self.cursor.fetchone()
            if riesgoCritico is not None:
                datoRiesgo.append(riesgoCritico[0])
                idRiesgosCriticos = riesgoCritico[1]
                nombresRiesgosCriticos = riesgoCritico[2]
                if idRiesgosCriticos:
                    ids = idRiesgosCriticos.split(',')
                    nombres = nombresRiesgosCriticos.split(',')
                    for idRiesgo, nombreRiesgo in zip(ids, nombres):
                        datoRiesgo.extend([idRiesgo, nombreRiesgo])
                    while len(datoRiesgo) < 4:
                        datoRiesgo.extend(['', ''])
        except Exception as ex:
            msg = "Error: " + str(ex.args)
            datoRiesgo.append(msg)
        return datoRiesgo
    
    def visualizarControlRiesgo(self, nombre):
        controlRiesgo = []
        sql= "SELECT riesgo, medida_control FROM actividad WHERE  nombre= '"+nombre+"'"
        try : 
            self.cursor.execute(sql)
            riesgoControl= self.cursor.fetchone()
            if riesgoControl != None:
                controlRiesgo.append(riesgoControl[0])
                controlRiesgo.append(riesgoControl[1])
        except Exception as ex:
            msg  = "Error: " + str(ex.args)
            controlRiesgo.append(msg)
        return controlRiesgo
    
    def sacarNumeroPreguntas(self,Nombre):
        sql= "SELECT pregunta FROM riesgocritico WHERE nombre= '"+Nombre+"'"
        try:
            self.cursor.execute(sql)
            pregunta = self.cursor.fetchone()
            if pregunta != None:
                msg = str(pregunta[0])
        except Exception as ex:
            msg = "Error: " + str(ex.args)
        return msg
    
    def mostrarTrabajadores(self):
        listaTrabajadores = []
        sql = "SELECT nombre_completo, rut, correo, especialidad FROM empleado WHERE cargo = 'Trabajador'"
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            if resultados:
                for registro in resultados:
                    listaTrabajadores.append((registro[0], registro[1], registro[2], registro[3]))
                return listaTrabajadores
            else:
                return []
        except Exception as ex:
            print("Error: " + str(ex.args))
            return []

    def mostrarARTCreadas(self,supervisor):
        listaART = []
        sql = "SELECT empleado.nombre_completo, empleado.rut, actividad.nombre, realiza.fecha, art.hora_inicio, art.hora_termino, realiza.estado_ART FROM realiza JOIN empleado ON realiza.rut = empleado.rut JOIN art ON realiza.id_ART = art.id_ART JOIN actividad ON art.id_actividad = actividad.id_actividad WHERE realiza.supervisor_asignado = '"+supervisor+"';"
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            if resultados:
                for registro in resultados:
                    listaART.append((registro[0], registro[1], registro[2], str(registro[3]), str(registro[4]), str(registro[5]), str(registro[6])))
                return listaART
            else:
                return []
        except Exception as ex:
            print("Error: " + str(ex.args))
            return []
        
    def mostrarARTporActividad(self,actividad,supervisor):
        listaporActividad = []
        sql = "SELECT empleado.rut, empleado.nombre_completo, art.id_ART, actividad.nombre, art.trabajo_simultaneo, realiza.estado_ART FROM art JOIN realiza ON art.id_ART = realiza.id_ART JOIN empleado ON realiza.rut = empleado.rut JOIN actividad ON art.id_actividad = actividad.id_actividad WHERE actividad.nombre = '"+actividad+"' AND realiza.estado_ART = 'pendiente' AND realiza.supervisor_asignado = '"+supervisor+"'"
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            if resultados:
                for registro in resultados:
                    listaporActividad.append((registro[0], registro[1], str(registro[2]), str(registro[3]),str(registro[4]),registro[5]))
                return listaporActividad
            else:
                return []
        except Exception as ex:
            print("Error: " + str(ex.args))
            return []
        
    def mostrarSuper(self):
        sql = "SELECT nombre_completo FROM empleado WHERE cargo ='Supervisor'"
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            nombres_supervisores = [fila[0] for fila in resultados]
            return nombres_supervisores  
        except Exception as ex:
            msg = "Error: " + str(ex.args)
        return msg
    
    def mostrarRcRespuestas(self, nombre, nombre2):
        respuestaRiesgo = []
        sql = "SELECT respuesta_correcta FROM riesgocritico WHERE nombre ='"+nombre+"' OR nombre = '"+nombre2+"'"
        try:
            self.cursor.execute(sql)
            riesgorespuesta = self.cursor.fetchall()
            if riesgorespuesta:
                respuestaRiesgo = [fila[0] if fila[0] != 1 else 'SI' for fila in riesgorespuesta]
                if len(respuestaRiesgo) == 1:
                    respuestaRiesgo.append("")
        except Exception as ex:
            msg = "Error: " + str(ex)
            respuestaRiesgo.append(msg)
        return respuestaRiesgo

    def mostrarResPreguntas(self):
        respuestasPreguntas = []
        sql = "SELECT respuesta_correcta FROM pregunta WHERE cargo= 'Trabajador'"
        try:
            self.cursor.execute(sql)
            preguntasRespuestas = self.cursor.fetchall()
            if preguntasRespuestas:
                respuestasPreguntas = [fila[0] if fila[0] != 1 else 'SI' for fila in preguntasRespuestas]
                if len(respuestasPreguntas) == 1:
                    respuestasPreguntas.append("")
        except Exception as ex:
            msg = "Error: " + str(ex)
            respuestasPreguntas.append(msg)
        return respuestasPreguntas
    
    def idUltimaARTRut(self,rut):
        sql = "SELECT id_ART FROM realiza WHERE rut='"+rut+"' ORDER BY id_art DESC LIMIT 1"
        try:
            self.cursor.execute(sql)
            realiza= self.cursor.fetchone()
            if realiza != None:
                return realiza[0]
            else: 
                return "No hay ninguna ART ingresada"
        except Exception as ex:
            print("Error: " + str(ex.args))
    
    def incorpora(self, id_art, id_pregunta, respuesta):
        sql = "INSERT INTO incorpora(id_art, id_pregunta, respuesta) VALUES ('"+str(id_art)+"','"+str(id_pregunta)+"', '"+str(respuesta)+"');"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
            msg = "Incorporación realizada correctamente"
        except Exception as ex:
            msg = "Error en incorpora: " + str(ex.args)
        return msg
    
    def actualizarEstadoArt1(self, id_ART):
        sql = "UPDATE realiza SET estado_ART = 'pendiente' WHERE id_ART = '"+id_ART+"'"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
            msg = "Estado de ART actualizado a 'pendiente'."
        except Exception as ex:
            msg = "Error al actualizar estado de ART: " + str(ex.args)
        return msg
    
    def actualizarEstadoArt2(self, id_ART):
        sql = "UPDATE realiza SET estado_ART = 'concluido' WHERE id_ART = '"+id_ART+"'"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
            msg = "Estado de ART actualizado a 'concluido'."
        except Exception as ex:
            msg = "Error al actualizar estado de ART: " + str(ex.args)
        return msg
    
    def actualizarEstadoArt3(self, id_ART):
        sql = "UPDATE realiza SET estado_ART = 'tarjeta verde' WHERE id_ART = '"+id_ART+"'"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
            msg = "Estado de ART actualizado a 'tarjeta verde'."
        except Exception as ex:
            msg = "Error al actualizar estado de ART: " + str(ex.args)
        return msg
    
    def actualizarEstadoArt4(self, id_ART):
        sql = "UPDATE realiza SET estado_ART = 'Revisado' WHERE id_ART = '"+id_ART+"'"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
            msg = "Estado de ART actualizado a 'Revisado'."
        except Exception as ex:
            msg = "Error al actualizar estado de ART: " + str(ex.args)
        return msg
    
    def asignarSuper(self,nombre,id_ART):
        sql = "UPDATE realiza SET supervisor_asignado = '"+nombre+"' WHERE id_ART = '"+id_ART+"'"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
            msg = "Supervisor asignado a la ART creada."
        except Exception as ex:
            msg = "Error de asignar supervisor: " + str(ex.args)
        return msg
    
    def ingresartrabSimut(self,contexto, coordinacion, verif_control, comuni_tab, id_ART):
        contextoStr = ",".join(contexto)
        sql = "UPDATE art SET Contexto_trab_simultaneo = '"+contextoStr+"', coordinacion_lider = '"+coordinacion+"', verificacion_controles_criticos = '"+verif_control+"', comunicacion_trabajadores_control = '"+comuni_tab+"' WHERE id_ART = '"+id_ART+"'"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
            msg = "Trabajo simultaneo puesto"
        except Exception as ex:
            msg = "Error al actualizar estado de ART: " + str(ex.args)
        return msg
    
    def filtroRut(self,supervisor,rut):
        sql = "SELECT empleado.nombre_completo, empleado.rut, actividad.nombre, realiza.fecha, art.hora_inicio, art.hora_termino, realiza.estado_ART FROM realiza JOIN empleado ON realiza.rut = empleado.rut JOIN art ON realiza.id_ART = art.id_ART JOIN actividad ON art.id_actividad = actividad.id_actividad WHERE realiza.supervisor_asignado = '"+supervisor+"' AND empleado.rut = '"+rut+"';"
        listaART = []
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            if resultados:
                for registro in resultados:
                    listaART.append((registro[0], registro[1], registro[2], str(registro[3]), str(registro[4]), str(registro[5]), str(registro[6])))
                return listaART
            else:
                return []
        except Exception as ex:
            print("Error: " + str(ex.args))
            return []
        
    def filtroFecha(self,supervisor,fecha):
        sql = "SELECT empleado.nombre_completo, empleado.rut, actividad.nombre, realiza.fecha, art.hora_inicio, art.hora_termino, realiza.estado_ART FROM realiza JOIN empleado ON realiza.rut = empleado.rut JOIN art ON realiza.id_ART = art.id_ART JOIN actividad ON art.id_actividad = actividad.id_actividad WHERE realiza.supervisor_asignado = '"+supervisor+"' AND realiza.fecha = '"+fecha+"';"
        listaART = []
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            if resultados:
                for registro in resultados:
                    listaART.append((registro[0], registro[1], registro[2], str(registro[3]), str(registro[4]), str(registro[5]), str(registro[6])))
                return listaART
            else:
                return []
        except Exception as ex:
            print("Error: " + str(ex.args))
            return []
        
    def filtrotarjetaVerde(self,supervisor):
        sql = "SELECT realiza.id_ART, empleado.nombre_completo, empleado.rut, actividad.nombre, realiza.fecha, art.hora_inicio, art.hora_termino, realiza.estado_ART FROM realiza JOIN empleado ON realiza.rut = empleado.rut JOIN art ON realiza.id_ART = art.id_ART JOIN actividad ON art.id_actividad = actividad.id_actividad WHERE realiza.supervisor_asignado = '"+supervisor+"' AND realiza.estado_ART = 'tarjeta verde';"
        listaART = []
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            if resultados:
                for registro in resultados:
                    listaART.append((str(registro[0]), registro[1], registro[2], str(registro[3]), str(registro[4]), str(registro[5]), str(registro[6]), registro[7]))
                return listaART
            else:
                return []
        except Exception as ex:
            print("Error: " + str(ex.args))
            return []
        
    def cambiarContraseña(self,contraseña,rut):
        sql = "UPDATE empleado SET contraseña = '"+contraseña+"' WHERE rut = '"+rut+"'"
        try:
            self.cursor.execute(sql)
            self.conector.commit()
        except Exception as ex:
            msg =  "Error: " + str(ex.args)
            return msg