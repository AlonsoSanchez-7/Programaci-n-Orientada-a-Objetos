from coches import coches, cochesBD

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
            print("\n\t...¡Accion Realizada con Exito!...")
        else:
            print("\n\t...¡Esta Accion no pudo realizarse en este momento!...")
        
    def menu_acciones(self, tipo):
        print(f"\n\t\t... :::MENU DE {tipo}::: ... \n")
        opc = input("\n\t1.- Agregar \n\t2.- Borrar \n\t3.- Modificar \n\t4.- Mostrar \n\t5.- Salir\n \t\tElige una opcion: ").strip()
        return opc
    
    def datos_coche(self, tipo):
        cochesito={}
        self.borrarPantalla()
        print(f"\n\t... Ingresar los datos del {tipo} ...")
        cochesito['marca'] = input("Marca: ").upper().strip()
        cochesito['color'] = input("Color: ").upper().strip()
        cochesito['modelo'] = input("Modelo: ").upper().strip()
        cochesito['velocidad'] = input("Velocidad: Km/h").strip()
        cochesito['potencia'] = input("Potencia: (Hp)").strip()
        cochesito['asientos'] = input("# de Asientos: ").strip()
        return cochesito
    
    
    def menu_coches(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones("Coches")
            match opcion:
                case '1':
                    # Crear objeto
                    cochesito = self.datos_coche("Coche")
                    coches1 = coches.Coches(cochesito ['marca'],cochesito ['color'],cochesito ['modelo'],cochesito ['velocidad'],cochesito ['potencia'],cochesito ['asientos'])
                    
                    # Crear objetos de CochesBD y luego insertar BD
                    coches1 = coches.Coches(cochesito ['marca'],cochesito ['color'],cochesito ['modelo'],cochesito ['velocidad'],cochesito ['potencia'],cochesito ['asientos'])
                    respuesta = coches1.insertar()
                    self.respuesta_sql(respuesta)
                    del coches1
                    
                case '2':
                    self.borrarPantalla()
                    id = input("Ingrese el ID del coche a eliminar: ").strip()
                    respuesta = coches.Coches.eliminar(id)
                    self.respuesta_sql(respuesta)
                    
                case '3':
                    self.borrarPantalla()
                    id = input("Ingrese el ID del coche a actualizar ").strip()
                    cochesito = self.datos_coche("Coche")
                    coches1 = coches.Coches(cochesito ['marca'],cochesito ['color'],cochesito ['modelo'],cochesito ['velocidad'],cochesito ['potencia'],cochesito ['asientos'])
                    respuesta = coches1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del coches1
                    
                case '4':
                    self.borrarPantalla()
                    registro = coches.Coches.consultar()
                    num_coche = 1
                    if len(registro)>0:
                        for fila in registro:
                            print(f"\n\tCoche #: {num_coche}\n\t\tID: {fila[0]}\n\t\tMarca: {fila[1]}\n\t\tColor: {fila[2]}\n\t\tModelo: {fila[3]}\n\t\tVelocidad: {fila[4]}\n\t\tPotencia: {fila[5]}\n\t\tAsientos: {fila[6]}")
                            num_coche+=1
                            self.espereTecla()
                    else:
                        print("... ¡Por el momento no se encontro informacion en la BD! ...")
                        self.espereTecla()
                    
                case '5':
                    opcion = False
                
                case _:
                    self.opcionInvalida()
    
    def main(self):
        opc = True
        while opc:
            self.borrarPantalla()
            opc = input("\n\t\t ::: MENU PRINCIPAL :::\n\t1.- Coches\n\t2.- Salir\n\t Elige una opcion: ").lower().strip()
            match opc:
                case '1':
                    self.borrarPantalla()
                    self.menu_coches()
                    self.espereTecla()
                case '2':
                    self.borrarPantalla()
                    self.terminar()
                    opc = False
                case _:
                    self.opcionInvalida()
            
    
if __name__ == "__main__":
    app = App()