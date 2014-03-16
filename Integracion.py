#-*- coding: utf-8 -*-
import numpy as np

#Variables globales
h = 0.01 #Tamaño de paso
g = 9.81 #Gravedad

#Método para elevar los componentes del vector a al cuadrado
def power(lista, p):
	return [l**p for l in lista]

#Aceleraciones
def funcion():
	a = np.loadtxt('datos.txt') #Extrae los valores de aceleracion del archivo datos.txt
	y = power(a,2) #Evalua la aceleración al cuadrado
	x = [round(i*0.01,2) for i in range(len(y))] #Define el vector de tiempo
	return x,y #Retorna el vector de tiempo y aceleración al cuadrado

x,y = funcion() #Define como variables globales los vectores de tiempo y aceleración

#Calcula la intensidad de Arias 
#utilizando el método del trapecio
def intensidad_trapecio(): 
	tiempo = x #Vector de tiempo
	intensidad = [0] #Vector de intensidad
	for i in range(len(y)-1):
		intensidad.append(intensidad[i]+ (np.pi/(2*g)) * (y[i]+y[i+1]) * h/2) #Agrega los valores de la intensidad asociados al tiempo (i*0,01)
	return tiempo,intensidad #Retorna tiempo e intensidad

#Calcula la intensidad de Arias 
#utilizando el método de Simpson 1/3
def intensidad_stercio():
	intensidad = [0] #Vector de intensidad
	tiempo = [0] #Vector de tiempo
	i = 0 #Índice para el tiempo y la aceleración
	j = 0 #Índice para tomar el valor de la intensidad anterior (Permite usar el valor anterior de intensidad como 'contador')
	#Se calcula el valor de la integral acumulada - equivalente a la intensidad de Arias
	while i <len(y)-2:
		tiempo.append(i*0.01+0.01) #Vector de tiempo asociado a cada intensidad
		intensidad.append(intensidad[j]+ (np.pi/(2*g)) * (y[i]+4*y[i+1]+y[i+2]) * h/3) #Agrega los valores de la intensidad asociados al tiempo (i*0,01+0,01)
		i += 2 #Muevo el índice para calcular la integral en el siguiente subintervalo
		j += 1 #Muevo el índice para usar el valor anterior de intensidad como contador
	return tiempo,intensidad #Retorna tiempo e intensidad

#Calcula la intensidad de Arias 
#utilizando el método de Simpson 3/8
def intensidad_stresoctavos():
	intensidad = [0] #Vector de intensidad
	tiempo = [0] #Vector de tiempo
	i = 0 #Índice para el tiempo y la aceleración
	j = 0 #Índice para tomar el valor de la intensidad anterior (Permite usar el valor anterior de intensidad como 'contador')
	#Se calcula el valor de la integral acumulada - equivalente a la intensidad de Arias
	while i < len(y)-3:
		tiempo.append(i*0.01+0.01) #Vector de tiempo asociado a cada intensidad
		intensidad.append(intensidad[j]+ (np.pi/(2*g)) * (3*h/8) *  (y[i]+3*y[i+1]+3*y[i+2]+y[i+3])) #Agrega los valores de la intensidad asociados al tiempo (i*0,01+0,01)
		i += 3 #Muevo el índice para calcular la integral en el siguiente subintervalo
		j += 1 #Muevo el índice para usar el valor anterior de intensidad como contador
	return tiempo,intensidad #Retorna tiempo e intensidad
