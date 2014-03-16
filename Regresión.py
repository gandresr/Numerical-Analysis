# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt

#Adquisicion de datos
def datos():
	f = open('datos.txt','r') #Se abre el archivo de texto con los datos para x,y
	x = []
	y = []

	for line in f: #Recorre para cada linea del archivo de texto 
		l = line.split() #Separa x de y
		x.append(float(l[0])) #Agrega el valor de x a la lista vacía
		y.append(float(l[1])) #Agrega el valor de y a la lista vacia

	f.close() #Se cierra el archivo

	return x,y #Retorna los vectores x y y 

#Imprime los datos de manera ordenada
def print_c(a,orden,r2):
	print '\n Regresion polinomial de orden: %d \n' % orden
	for i in range(len(a)):
		print 'a%d = %.6f' % (i,a[i])
	print '\n Coeficiente de determinacion r2 = %f' % r2

#Calcula el coeficiente de determinación
def r2(y,y_ajuste):
	y_prom = sum(y)/len(y) #y promedio

	st = sum([(y[i]-y_prom)**2 for i in range(len(y))]) #Calculo del st
	sr = sum([(y[j]-y_ajuste[j])**2 for j in range(len(y))]) #Calculo del sr

	return (st-sr)/st #Calculo de r2

#Eleva a una potencia los elementos de una lista/vector
#Retorna un vector
def power(lista,p):
	return [n**p for n in lista]

#Regresion polinomial
#Recibe como parámetro el orden de la aproximación polinomial
#Para orden 1 se tiene una regresion de la forma a0 + a1x
def polinomial(orden):
	x,y = datos()  #Se definen los datos a partir del archivo de texto

	comp_m = []  #Componenetes de la matriz para hacer la regresion por minimos cuadrados
	for i in range(2*orden+1):
		comp_m.append(sum(power(x,i))) #Agrega los elementos de la matriz a un vector. Hace la sumatoria de los (x_i) elevados a la i

	arreglo = [] #Arreglo o matriz de regresion
	for j in range(orden+1):
                #Agrega los elementos a cada fila de la matriz a partir de las componentes de la matriz
                #Se organizan de tal manera que la matriz sea simétrica
		arreglo.append([comp_m[j+i] for i in range(orden+1)]) 

	A = np.array(arreglo) #Convierte la matriz de regresion en un arreglo de numpy para facilitar operaciones de matrices

	s_y = [] #Vector de sumatoria de x_i a la k por y_i
	for k in range(orden+1):
		x_i = power(x,k)  #Calcula los x_i elevados a la potencia en la iteracion correspondiente
		s_y.append(sum([y[i]*x_i[i] for i in range(len(y))])) #Sumatoria: la sumatoria se agrega al vector s_y

	B= np.array(s_y) #Convierte s_y en un arreglo de numpy para facilitar operaciones de matrices
	ans = np.linalg.solve(A,B) #Resuelve el sistema de ecuaciones de la forma Ax = B donde x es la solución; vector de regresión

	print_c(ans,orden,r2(y,poli(ans,x))) #Imprime los resultados en pantalla: Coeficientes; orden de la regresión y Coeficiente de determinación
	return ans #Retorna el valor los coeficientes del polinomio de regresión

#Halla los valores del polinomio de la forma a0x0 + a1x1 + a2x2 + ...
#Toma como parametros los coeficientes 'a' de la regresión y los valores de x obtenidos del archivo de datos
#Retorna una lista con los valores de y
def poli(a,x):
	yn = []
	for j in range(len(x)): #Evalua cada uno de los valores de 'y' en función de x
		yn.append(sum([a[i]*x[j]**i for i in range(len(a))])) #Agrega cada valor de y evaluado en un punto x al vector de y
	return np.array(yn) #Retorna el y de la regreseión como arreglo de numpy

def test():
	x,y = datos() #Recoje los datos del archivo de texto
	a1 = polinomial(1) # Regresión de orden 1
	a6 = polinomial(6) # Regresión de orden 6
	a9 = polinomial(9) # Regresión de orden 9
	a12 = polinomial(12) # Regresión de orden 12   
	a13 = polinomial(13) # Regresión de orden 13

	p1, = plt.plot(x,y) #Grafica de los datos originales
	#Graficas de las regresiones
	p2, = plt.plot(x,poli(a1,x)) 
	p3, = plt.plot(x,poli(a6,x))
	p4, = plt.plot(x,poli(a9,x))
	p5, = plt.plot(x,poli(a12,x))
	p6, = plt.plot(x,poli(a13,x))
	plt.legend([p1, p2, p3, p4, p5, p6,],["Real","Orden 1","Orden 6","Orden 9","Orden 12","Orden 13"])  #Leyenda
	plt.show() #Se muestra la gráfica en pantalla

test() #Se corre el script de prueba

