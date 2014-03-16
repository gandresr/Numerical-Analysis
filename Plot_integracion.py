#-*- coding: utf-8 -*-
#Importa las librerias
import Integracion as arias
import pylab as plt

#Define el vector de tiempo y el vector de intensidad obtenidos por el metodo del trapecio
timet, intensidadt = arias.intensidad_trapecio() 
#Define el vector de tiempo y el vector de intensidad obtenidos por el metodo de simpson 1/3
timestercio, intensidadtercio = arias.intensidad_stercio()
#Define el vector de tiempo y el vector de intensidad obtenidos por el metodo del simpson 3/8
timestresoctavos, intensidadtresoctavos = arias.intensidad_stresoctavos()
#Se imprimen los valores de intensidad máxima
print 'Maxima intensidad: \n Trapecio: %f\n Simpson 1/3: %f \n Simpson 3/8: %f' % (intensidadt[len(intensidadt)-1],intensidadtercio[len(intensidadtercio)-1],intensidadtresoctavos[len(intensidadtresoctavos)-1])
p1, = plt.plot(timet, intensidadt) #Gráfica 1, trapecio
p2, = plt.plot(timestercio, intensidadtercio) #Gráfica 2, simpson 1/3
p3, = plt.plot(timestresoctavos, intensidadtresoctavos) #Gráfica 3, simpson 3/8
plt.legend([p1,p2,p3],["Trapecio","Simpson 1/3","Simpson 3/8"]) #Leyenda de la gráfica
plt.show() #Muestra la gráfica
