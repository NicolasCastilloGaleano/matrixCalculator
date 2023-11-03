from tkinter import *
from tkinter import font


class App:
    def __init__(self):
        self.create_window()

    def create_window(self):
        # se crea la ventana de la app
        self.window = Tk()
        self.window.iconbitmap("icon.ico")
        self.window.geometry("1340x680+0+0")
        self.window.resizable(0, 0)
        self.window.title("ITENUA Matrix Calculator")
        self.set_parameters()
        self.frame = Frame(self.window,bg="white")
        self.frame.pack(fill="both",expand=True)
        self.frame.grid_rowconfigure(0,weight=1)
        self.frame.grid_rowconfigure(1,weight=15)
        self.frame.grid_columnconfigure(0, weight=1)

        # se crea el Frame donde se especifican las dimensiones de la matriz 
        self.matrix_size_frame = Frame(self.frame, bg="black", borderwidth=11)
        self.matrix_size_frame.grid(column=0,row=0,sticky=NSEW)

        # Texto
        self.matrix_size_text = "Tamaño de la matriz: "
        self.matrix_size_label_text = Label(self.matrix_size_frame, text=self.matrix_size_text)
        self.matrix_size_label_text.grid(row=0,column=0)
        

        # entrada del valor de las filas de la matriz
        self.rowsEntry = Entry(self.matrix_size_frame, width=5,justify="center")
        self.rowsEntry.grid(row=0,column=1, sticky=NS)

        # Texto
        self.matrix_size_label_text2 = Label(self.matrix_size_frame, text="X")
        self.matrix_size_label_text2.grid(row=0,column=2)

        # entrada del valor de las columnas de la matriz
        self.columnsEntry = Entry(
            self.matrix_size_frame, width=5,justify="center")
        self.columnsEntry.grid(row=0,column=3, sticky=NS)

        # boton que crea la matriz con las dimensiones dadas
        self.create_matrix_button = Button(self.matrix_size_frame, text= "crear",command=self.resize_matrix)
        self.create_matrix_button.grid(row=0,column=4, padx=(5,0))

        # Frame que muestra la matriz sobre la uqe se va a trabajar
        self.matrix_frame = Frame(self.frame, bg="black")
        self.matrix_frame.grid(row=1,column=0, sticky=NSEW)
        self.resize_matrix()
        self.window.mainloop()

    def set_parameters(self):
        # se establece parametros por defecto
        custom_font = font.Font(size=12, family="Arial", weight="bold")
        self.window.option_add("*Font", custom_font)  # Aplica la fuente personalizada a todos los elementos de tkinter
        self.window.option_add("*Button*Foreground", "black")  # Establece el color de fuente para botones
        self.window.option_add("*Label*Background", "black") 
        self.window.option_add("*Label*Foreground", "white") 
        self.window.option_add("*Entry*Foreground", "black") 

    def resize_matrix(self, *args):
        if (self.rowsEntry.get().isnumeric() and self.columnsEntry.get().isnumeric()):
            self.current_rows = self.rowsEntry.get()
            self.current_columns = self.columnsEntry.get()
            self.clean_matrix()
            for row in range(int(self.current_rows)):
                for col in range(int(self.current_columns)):
                    self.create_matrix_entry(self.matrix_frame, row, col)
        else:
            for row in range(3):
                for col in range(3):
                    self.create_matrix_entry(self.matrix_frame, row, col)

    def clean_matrix(self):
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

    def create_matrix_entry(self, father, row, col):
        self.entry = Entry(father, width=5,justify="center")
        self.entry.grid(column=col, row=row, sticky=NS, padx=1,pady=1)
        return
        # Press the green button in the gutter to run the script.

        # See PyCharm help at https://www.jetbrains.com/help/pycharm/
app = App()
