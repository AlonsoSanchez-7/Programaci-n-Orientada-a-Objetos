from estudiantes import estudiantes, estudiantesBD

class App:
    def __init__(self):
        self.main()
        
    def borrarPantalla(self):
        print("\033c")
    
    def espereTecla(self):
        input("... ¡Oprima cualquier Tecla para continuar! ...")
        
    def terminar(self):
        input("... ::: ¡GRACIAS POR UTILIZAR NUESTRO SISTEMA! ::: ...")
    
    def opcionInvalida(self):
        input("Opcion invalida oprima cualquier Tecla para continuar")
        
    def respuesta_sql(self, respuesta):
        if respuesta:
            input("\n\t...¡Accion Realizada con Exito!...")
        else:
            input("\n\t...¡Esta Accion no pudo realizarse en este momento!...")
        
    def menu_acciones(self):
        print(f"\n\t\t... :::MENU DE ESTUDIANTES::: ... \n")
        opc = input("\n\t1.- Agregar \n\t2.- Borrar \n\t3.- Modificar \n\t4.- Mostrar \n\t5.- Salir\n \t\tElige una opcion: ").strip()
        return opc
    
    def datos_estudiantes(self):
        alumno={}
        self.borrarPantalla()
        print(f"\n\t... Ingresar los datos del Estudiante ...")
        alumno['nombre'] = input("Nombre: ").upper().strip()
        alumno['nota'] = input("Nota (Calificación):").strip()
        return alumno
    
    
    def menu_estudiantes(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones()
            match opcion:
                case '1':
                    # Crear objeto
                    alumno = self.datos_estudiantes()                    
                    # Crear objetos de CochesBD y luego insertar BD
                    estudiante1 = estudiantesBD.EstudiantesBD(alumno ['nombre'], alumno ['nota'])
                    respuesta = estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1
                    
                case '2':
                    self.borrarPantalla()
                    id = input("Ingrese el ID del Estudiante a eliminar: ").strip()
                    respuesta = estudiantesBD.EstudiantesBD.eliminar(id)
                    self.respuesta_sql(respuesta)
                    
                case '3':
                    self.borrarPantalla()
                    id = input("Ingrese el ID del Estudiante a actualizar: ").strip()
                    alumno = self.datos_estudiantes()
                    estudiante1 = estudiantesBD.EstudiantesBD(alumno ['nombre'], alumno ['nota'])
                    respuesta = estudiante1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del estudiante1
                    
                case '4':
                    self.borrarPantalla()
                    registros = estudiantesBD.EstudiantesBD.consultar()
                    num_estudiante = 1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"\n\tEstudiante #: {num_estudiante}\n\t\tID: {fila[0]}\n\t\tNombre: {fila[1]}\n\t\tNota: {fila[2]}")
                            num_estudiante+=1
                            self.espereTecla()
                    else:
                        print("... ¡Por el momento no se encontro informacion en la BD! ...")
                        self.espereTecla()
                    
                case '5':
                    pass
                
                case _:
                    self.opcionInvalida()
    
    def main(self):
        opc = True
        while opc:
            self.borrarPantalla()
            opc = input("\n\t\t ::: MENU PRINCIPAL :::\n\t1.- Estudiantes\n\t2.- Salir\n\t Elige una opcion: ").lower().strip()
            match opc:
                case '1':
                    self.borrarPantalla()
                    self.menu_estudiantes()
                    self.espereTecla()
                case '2':
                    self.borrarPantalla()
                    self.terminar()
                    opc = False
                case _:
                    self.opcionInvalida()
            
    
if __name__ == "__main__":
    app = App()
    
    
    # Hacer que el metodo get y set se utilizen para (decoradores en los metodos get y set).
    # @ set.
    # Metodos estaticos, definir en una clase y utilizarlo sin haber creado un objeto (tiene que ver con los decoradores).