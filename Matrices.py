# -*- encoding: utf-8 -*-
#Autor: Gerardo Andrés Riaño Briceño
#Código: 201112388

#Funcion para definir los valores de la matriz original
def matrix(n,m):
     
    #Inicialización de lista vacía
    matriz=[]
    
    #Ciclo de inicialización:
    #El usuario ingresa los valores de la matriz y estos se guardan en la lista
    for i in range(0,n):
        a = raw_input('Ingrese los %d valores de la fila %d (separados por 1 espacio): \n ' % (m,i)).split(' ')
        matriz.append(map(float,a))
                     
    return matriz

#Funcion para simplificar la diagonal de la matriz
def simplificar(matrix):

    #Recorre la matriz y divide los elementos de cada fila por el número den la diagonal
	for i in range(0, len(matrix)):
		factor = matrix[i][i]
		for j in range(0, len(matrix[0])):
			matrix[i][j] = matrix[i][j]/factor

	return matrix
	
#Muestra en pantalla la matriz
#Recibe como parámetros la matriz que va a mostrarse, la pocisión x (fila en la interfaz) y la posición y (columna en la interfaz)
def mostrar_m(matrix):

	l = '\n'

    #Recorre la matriz y toma los valores para ponerlos en la interfaz de forma organizada
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[0])):
			l+=' '*(9-len('%.4f' % matrix[i][j]))+('%.4f' % matrix[i][j])
		print l+'\n'
		l = ''

#Método de Gauss simple
#Recibe como parámetros las dimensiones de la matriz que quiere reducirse
def gauss_s(n, m):

    #Se inicializa la matriz
    matriz = matrix(n,m)

    #Se definen los índices para recorrer la matriz hacer la eliminación por filas
    y = 0
    k = 1

    #Ciclo principal
    #Recorre la matriz y modifica sus valores haciendo poniendo en cero los valores
        #de la matriz debajo de la diagonal
    #Se obtiene una matriz triangular superior como resultado
    while y<n-1:

        #Recorrido interno
        while k<n:
            #Se define el factor por el cual va a multiplicarse la fila con la que se va a reducir
            factor = matriz[k][y]/matriz[y][y]
            for i in range(0,m):
                #Se reducen las filas desde la 1 hasta la n de la matriz
            	matriz[k][i] = matriz[k][i]-(factor*matriz[y][i])
            k += 1

        #Incremento de los índices para el recorrido
        y += 1
        k = y+1

    #Retorna la matriz simplificada
    return simplificar(matriz)


#Método de Gauss Jordan

def gauss_jordan(n, m):

    #Inicializa la matriz como una matriz diagonal superior 
    #Se reduce la matriz original por Gauss simple para hacer la eliminación hacía adelante
    matriz = gauss_s(n, m)


    y = 1
    k = 0

    #Ciclo interno
    #Se lleva a cabo la eliminación hacía adelante
    while y<n:
        while k<y:
            #Se define el factor por el cual va a multiplicarse la fila con la que se va a reducir
            factor = matriz[k][y]/matriz[y][y]
            for i in range(0,m):
                #Se reducen las filas
                matriz[k][i] = matriz[k][i]-(factor*matriz[y][i])
            k += 1
        #Incremento de los índices para el recorrido
        y += 1
        k = 0

    #Retorna una matriz diagonal simplificada
    #Con la matriz reducida como diagonal es facil distinguir las soluciones del sistema
    return simplificar(matriz)

#Método de Gauss Seidel
def gauss_seidel(n, m):

    #El usuario ingresa los valores iniciales de x
    x=[]
    for i in range(n):
        x.append(float(raw_input('Ingrese el valor de x%d: ' % i)))
    tol = float(raw_input('Ingrese tolerancia: '))

    #Se inicializa el sistema de ecuaciones
    matriz = matrix(n, m)
    
    #Se inicializan las variables del sistema
    numerador = 0
    e=range(n)
    emax = None

    #Ciclo principal
    while emax>tol or emax == None:

        #Primer ciclo interno
        #Se calculan los valores de x de forma recursiva
        #Se despeja el valor de x de cada fila y se utilizan las condiones iniciales para resolver la ecuación
        for j in range(0,n):
            for i in range(0,n):
                numerador -= x[i]*matriz[j][i]
            numerador+=x[j]*matriz[j][j]
            #Se guarda el valor calculado de x_j en el vector x
            x[j]=round((matriz[j][m-1]+numerador)/matriz[j][j],4)
            numerador = 0
        
        #Segundo ciclo interno
        #Se calcula el error de cada ecuación
        #Se toma como error dominante de la iteración del ciclo principal el máximo de los errores
        for k in range(n):
            sum=0
            for b in range(n):
                #Se calcula el valor de la solución a partir de los valores de x calculados en la iteración
                sum += matriz[k][b]*x[b]
            #Se calcula el error correspondiente a cada fila y se almacena en un vector de errores
            e[k] = abs((matriz[k][m-1]-sum)/(matriz[k][m-1]))
        
        #Se toma el máximo de los errores del sistema como el dominante de la iteración
        emax = max(e)

    #Después de finalizar el ciclo se satisface el error y las soluciones se muestran en pantalla
    print '\nEl resultado para x por Gauss Seidel es: '
    return x

#Se prueban los métodos para la matriz del ejercicio 3x4
#El usuario debe ingresar los valores del sistema de ecuaciones como se específica en el proceso
#NO DEBE DEJAR ESPACIOS AL FINAL O AL PRINCIPIO, SOLO UN ESPACIO ENTRE NUMEROS
#Sin embargo, los métodos funcionan para resolver un sistema de nxn ecuaciones; están en su forma general
def test():
    print '\nMetodo de Gauss Seidel \n'
    print gauss_seidel(3,4)
    print '\n\nMetodo de Gauss Simple \n'
    mostrar_m(gauss_s(3,4))
    print '\n Metodo de Gauss Jordan \n'
    mostrar_m(gauss_jordan(3,4))
    print'\n Los resultados de x para el sistema de ecuaciones se encuentran en la ultima columna de la matriz'
    

#Corremos el Test
test()