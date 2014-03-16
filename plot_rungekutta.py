#-*- coding: utf-8 -*-
#Se importan librerias
import matplotlib.pyplot as plt
from rungekutta import *

#Gráfica de las concentraciones utilizando el método de RK4 con paso de 0.1 s
t,ca,cb,cc = rk4(50,10,20,0.1,3) #Variables para las gráficas
#Se imprimen concentraciones de cada reactivo para t={0.2, 1.2, 3}s
print (' -------------h = 0.1s-----------------')
print 'Concentracion reactivo Ca en t=0.2s: %f ' % ca[t.index(0.2)]
print 'Concentracion reactivo Cb en t=0.2s: %f ' % cb[t.index(0.2)]
print 'Concentracion reactivo Cc en t=0.2s: %f ' % cc[t.index(0.2)]

print 'Concentracion reactivo Ca en t=1.2s: %f ' % ca[t.index(1.2)]
print 'Concentracion reactivo Cb en t=1.2s: %f ' % cb[t.index(1.2)]
print 'Concentracion reactivo Cc en t=1.2s: %f ' % cc[t.index(1.2)]

print 'Concentracion reactivo Ca en t=3s: %f ' % ca[t.index(3)]
print 'Concentracion reactivo Cb en t=3s: %f ' % cb[t.index(3)]
print 'Concentracion reactivo Cc en t=3s: %f ' % cc[t.index(3)]

p1, = plt.plot(t,ca)
p2, = plt.plot(t,cb)
p3, = plt.plot(t,cc)         
plt.title('Concentraciones con paso de 0.1s')
plt.xlabel('Tiempo (s)')         
plt.legend([p1,p2,p3],['A','B','C'])
plt.show()

#Gráfica de las concentraciones utilizando el método de RK4 con paso de 0.2 s
t,ca,cb,cc = rk4(50,10,20,0.2,3) #Variables para las gráficas
#Se imprimen concentraciones de cada reactivo para t={0.2, 1.2, 3}s
print (' -------------h = 0.2s-----------------')
print 'Concentracion reactivo Ca en t=0.2s: %f ' % ca[t.index(0.2)]
print 'Concentracion reactivo Cb en t=0.2s: %f ' % cb[t.index(0.2)]
print 'Concentracion reactivo Cc en t=0.2s: %f ' % cc[t.index(0.2)]

print 'Concentracion reactivo Ca en t=1.2s: %f ' % ca[t.index(1.2)]
print 'Concentracion reactivo Cb en t=1.2s: %f ' % cb[t.index(1.2)]
print 'Concentracion reactivo Cc en t=1.2s: %f ' % cc[t.index(1.2)]

print 'Concentracion reactivo Ca en t=3s: %f ' % ca[t.index(3)]
print 'Concentracion reactivo Cb en t=3s: %f ' % cb[t.index(3)]
print 'Concentracion reactivo Cc en t=3s: %f ' % cc[t.index(3)]
p3, = plt.plot(t,ca)
p4, = plt.plot(t,cb)
p5, = plt.plot(t,cc)
plt.title('Concentraciones con paso de 0.2s')
plt.xlabel('Tiempo (s)')       
plt.legend([p3,p4,p5],['A','B','C'])
plt.show()