from estudiantes import estudiantes
from tkinter import Tk,Label,Entry,Button,messagebox


class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestión de Estudiantes")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0,0)
        self.main()
    
    # .... Vistas o Views del Sistema ....
    def borrarPantalla(self):
      for widget in self.ventana.winfo_children():
          widget.destroy()
    
    def main(self):
       self.borrarPantalla()
       Label(self.ventana,text="::: MENU PRINCIPAL :::").pack(pady=20)
       Button(self.ventana,text="1.- Estudiantes",command=self.menu_acciones).pack(pady=10)
       Button(self.ventana,text="2.- Salir",command=self.ventana.quit).pack(pady=10)
    
    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Estudiante"
        Label(self.ventana,text=f"...::: Menu de {tipo} :::...").pack(pady=10)
        Button(self.ventana,text="1.- Agregar",command=self.insertar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="2.- Borrar",command=self.eliminar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=10)
        
    def insertar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar los datos del Estudiante...").pack(pady=10)
        
        Label(self.ventana,text="Nombre: ").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)
        
        Label(self.ventana,text="Nota: ").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)
        
        Button(self.ventana,text=":: Agregar ::",command=self.insertar_estudiante_controller).pack(pady=5)
        
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
       
    def eliminar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar el ID del estudiante a eliminar...").pack(pady=10)
        
        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)
        
        Button(self.ventana,text=":: Eliminar ::",command=self.eliminar_estudiante_controller).pack(pady=5)
        
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
        
    def consultar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="..:: Consultar Estudiantes ::..").pack(pady=10)
        filas=""
        filas=self.consultar_estudiante_controller(filas)
        Label(self.ventana,text=f"{filas}").pack(pady=5)
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
    
    def modificar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar el ID del estudiante a modificar...").pack(pady=10)
        
        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)
        
        Label(self.ventana,text="...Datos del Estudiante...").pack(pady=10)
        
        Label(self.ventana,text="Nombre: ").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.pack(pady=5)
        
        Label(self.ventana,text="Nota: ").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)
        
        Button(self.ventana,text=":: Modificar ::",command=self.modificar_estudiante_controller).pack(pady=5)
        
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)
        
        
    # .... Controlador o Controller del Sistema ....
    def respuesta_sql(self,respuesta):
            if respuesta:
                messagebox.showinfo(title=":: Exitoso ::",message="...¡Accion Realizada con Exito!...")
            else:
                messagebox.showerror(title=":: Verifique por favor ::",message="...¡Esta Accion no pudo realizarse en este momento!...")
    
    def insertar_estudiante_controller(self):
        estudiantes1=estudiantes.Estudiantes(self.nombre.get(),self.nota.get())                   
        respuesta=estudiantes1.insertar()
        self.respuesta_sql(respuesta)
        del estudiantes1    
       
    def eliminar_estudiante_controller(self):
        respuesta=estudiantes.Estudiantes.eliminar(self.id.get())
        self.respuesta_sql(respuesta)
        
    def consultar_estudiante_controller(self,filas):
        registros=estudiantes.Estudiantes.consultar()
        num_estudiante=1
        if len(registros)>0:
           for fila in registros:
             filas=filas+(f"\n\Estudiante #: {num_estudiante}\nID: {fila[0]}\tNombre: {fila[1]}\n\tNota: {fila[2]}")
             num_estudiante+=1
        else:
            filas="...¡No se encontro informacion en la BD!..."
        return filas    
      
    def modificar_estudiante_controller(self):
        id=self.id.get()
        estudiantes1=estudiantes.Estudiantes(self.nombre.get(),self.nota.get())  
        respuesta=estudiantes1.actualizar(id)
        self.respuesta_sql(respuesta)
        del estudiantes1
          
        
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
