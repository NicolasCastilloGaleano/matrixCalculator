from tkinter import *
from tkinter import font
import numpy as np
from matrixCalculator import MatrixCalculator


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
        
        self.test_button = Button(self.frame,command=self.calculate)
        self.test_button.grid()
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
        self.matrix = []
        self.Entries_matrix = []
        if (self.rowsEntry.get().isnumeric() and self.columnsEntry.get().isnumeric()):
            self.current_rows = int(self.rowsEntry.get())
            self.current_columns =int( self.columnsEntry.get())
            self.clean_matrix_frame()
            self.matrix = np.zeros((self.current_rows,self.current_columns),dtype=int)
            for row in range(int(self.current_rows)):
                self.Entries_matrix.append([])
                for col in range(int(self.current_columns)):
                    self.create_matrix_entry(self.matrix_frame, row, col)
        else:
            self.current_rows = 3
            self.current_columns =3
            self.matrix = np.zeros((3,3),dtype=int)
            for row in range(3):
                self.Entries_matrix.append([])
                for col in range(3):
                    self.create_matrix_entry(self.matrix_frame, row, col)
        self.matrix_calculator = MatrixCalculator(self.matrix,self.current_rows,self.current_columns)
        
        
    def calculate(self):
        # for row in range(self.current_rows):
        #     row_items = ""
        #     for col in range(self.current_columns):
        #         row_items = row_items + " "+ self.Entries_matrix[row][col].get()
        #     print(row_items)
        #     row_items =""
        
        for row in range(self.current_rows):
            for col in range(self.current_columns):
                self.matrix_calculator.matrix[row][col] = int(self.Entries_matrix[row][col].get())
        self.matrix_calculator.print_matrix()
            


    def clean_matrix_frame(self):
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

    def create_matrix_entry(self, father, row, col):
        self.entry = Entry(father, width=5,justify="center")
        self.entry.insert(0,self.matrix[row][col])
        self.entry.grid(column=col, row=row, sticky=NS, padx=1,pady=1)
        self.Entries_matrix[row].append(self.entry)
        # Press the green button in the gutter to run the script.

        # See PyCharm help at https://www.jetbrains.com/help/pycharm/
app = App()
