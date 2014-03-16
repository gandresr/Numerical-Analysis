# -*- coding: utf-8 -*-
import numpy as np
import pylab as plt

#Función del ejercicio
def f(x):
	return np.sqrt(64-x**2) + 10/(2+x**2)

#Coeficientes del polinomio de interpolacion en la forma de Lagrange
#El metodo recibe como parámetros el valor de "n" (orden de la aproximación)
#el valor del índice de la iteración, el vector "xi" (valores de x donde se conoce cuanto vale f(x))
#y el valor de "x" (punto donde se quiere interpolar la función)
def Li(i,n,xi,x):

	mul = 1

	for j in range(n+1): #Multiplicatoria 
		if j!=i:
			mul*=(x-xi[j])/(xi[i]-xi[j])
	return mul #Coeficiente i-ésimo del polinomio de Lagrange

#Polinomio de Lagrange
#Recibe el valor de "x" (punto donde se quiere interpolar la función)
#el valor de "n" (orden de la interpolación)
#el valor de "xl" (limite inferior del intervalo donde se va a interpolar) -> por defecto es -5
#el valor de "xu" (limite superior del intervalo donde se va a interpolar) -> por defecto es +5
def lagrange(x,n,xl=-5,xu=5):

	h=abs(float(xu-xl)/n) #Tamaño de paso
	xi=np.arange(xl,xu+h,h) #Arreglo con puntos donde se conoce la función (son n+1 puntos)
	return sum([Li(i,n,xi,x)*f(xi[i]) for i in range(n+1)]) #Sumatoria para evaluar el polinomio de interpolación

#Interpola la función entre -5 y 5 para el orden n
def interpolar(n):
	x = np.arange(-5.,5.+0.01,0.01) #Vector de puntos en el intervalo [-5,5] con pasos de 0.01
	y = [lagrange(x[i],n) for i in range(len(x))] #Valor aproximado con Lagrange de la función para cada x
	return y #Retorna "x" y "y"

#Calcula el máximo error absoluto de la interpolacion
def error(n,y,y_aprox):
	#Retorna el orden de aproximación y el máximo error absoluto (con 4 cifras decimales)
	return "Aproximacion de orden: %d \n Error maximo: %.4f" % (n,max([abs((y[i]-y_aprox[i])/y[i]) for i in range(len(y))]))
