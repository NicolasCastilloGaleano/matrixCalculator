import numpy as np



class MatrixCalculator:
    def __init__(self,matrix,rows,cols) -> None:
        self.rows = rows
        self.cols = cols
        self.matrix =np.array(matrix)
        
    def set_value(self,row,column,value):
        self.matrix[row][column] = value
        
    def print_matrix(self):
        if self.cols == self.rows:
            count = 0
            print('La matriz introducida es', self.matrix)
            self.tr_matrix = np.transpose(self.matrix)
            print('Y tiene matrix transpuesta ', self.tr_matrix )
            for row in range(self.rows):
                for col in range(self.cols):
                    normal_matrix_value = self.matrix[row][col]
                    tr_matrix_value = self.matrix[col][row]
                    if normal_matrix_value == tr_matrix_value:
                        count += 1
            if count == (self.rows * self.cols):
                print('Por tanto, la matriz es simétrica')
            else:
                print('Matriz adjunta no coincide con la matriz dada, por tanto se concluye que la matriz NO es simétrica')
            print('La matriz tiene determinante ', np.linalg.det(self.matrix))
            if np.linalg.det(self.matrix) != 0:
                print('los decimales que aparecen son un redondeo de las operaciones en bytes, la matriz es invertible, '
                'y tiene inversa dada por')
                print(np.linalg.inv(self.matrix))
            else:
                print('la matriz introducida tiene determinante cero y por ende no es invertible')
        else:
            print('Debido a que la matriz no es cuadrada, se concluye que No es simétrica y no se puede calcular el determinante')
        print('los valores propios de la matriz son:')
        # np.linalg usa el modulo de algebra lineal de numpy, eigenvals es para valores propios en general
        print(np.linalg.eigvals(self.matrix))
    
            
        


    
