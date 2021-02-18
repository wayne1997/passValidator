import re 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class Ventana():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(0,0)
        self.ventana.title('Validador de contraseñas')
        
        self.marco = ttk.Frame(self.ventana, borderwidth=7, relief="raised", padding=(10, 10))

        self.lblPassword = ttk.Label(self.marco, text="Password: ", padding=(5,5))
        self.txtPassword = ttk.Entry(self.marco, width=50)
        self.separador = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.btnVerificar = ttk.Button(self.marco, text="Verificar", padding=(5, 5), command=self.verificar)

        self.marco.grid(column=0, row=0)
        self.lblPassword.grid(column=0, row=0)
        self.txtPassword.grid(column=1, row=0)
        self.separador.grid(column=0, row=1, columnspan=3)
        self.btnVerificar.grid(column=2, row=2)
        self.ventana.mainloop()
    
    def verificar(self):
        if re.match('^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,21}$', self.txtPassword.get()):
            messagebox.showinfo('Resultado', 'Su password es fuerte')
        else:
            messagebox.showinfo('Resultado', 'Su clave es debil')
            

def main():
    mi_ventana = Ventana()
    return 0

if __name__ == '__main__':
    main()

