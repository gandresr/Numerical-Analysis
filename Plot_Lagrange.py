# -*- coding: utf-8 -*-
import Lagrange as inter
import pylab as plt
import numpy as np


x = np.arange(-5.,5.+0.01,0.01) #Vector x
y = [inter.f(x[i]) for i in range(len(x))] #Valores reales de la función

print inter.error(2,y,inter.interpolar(2))
print inter.error(4,y,inter.interpolar(4))
print inter.error(6,y,inter.interpolar(6))

#Graficas
plot0, = plt.plot(x,y)
plot1, = plt.plot(x,inter.interpolar(2))
plot2, = plt.plot(x,inter.interpolar(4))
plot3, = plt.plot(x,inter.interpolar(6))
plt.legend([plot0,plot1,plot2,plot3],["f(x)","Orden 2","Orden 4","Orden 6"])
plt.show()
