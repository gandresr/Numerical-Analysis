# -*- coding: utf-8 -*-

#Metodo para evaluar la funcion en un punto x 
#Recibe como parametros W0, L, E, I (Si no se ingresan se toman valores predeterminados)
def f(x,W0=5400., L=700., E=20000., I = 1500.):
    
    return W0/(120*E*I*L)*(-(x**5)+2*(L**2)*(x**3)-(L**4)*x)

#Metodo para evaluar la primera derivada de la funcion en un punto x 
#Recibe como parametros W0, L, E, I (Si no se ingresan se toman valores predeterminados)
def d1f(x,W0=5400., L=700., E=20000., I = 1500.):

	return W0/(120*E*I*L)*(-5*(x**4)+6*(L**2)*(x**2)-(L**4))

#Metodo para evaluar la segunda derivada de la funcion en un punto x 
#Recibe como parametros W0, L, E, I (Si no se ingresan se toman valores predeterminados)
def d2f(x,W0=5400., L=700., E=20000., I = 1500.):

	return W0/(120*E*I*L)*(-20*(x**3)+12*(L**2)*x)

#Metodo de busqueda dorada
def dorada(xl,xu,tol):
   
	#Se definen los parametros iniciales
	i = 1  #Numero de iteracion
	e = None  #Error
	R = 0.6180339  #Razón dorada
	ans = 'I   xl        xu        xopt      error     f(xopt)\n\n'  #Tabla para archivo de texto

	#Ciclo principal
	#Se lleva a cabo hasta obtener un error menor a la tolerancia ingresada por el usuario
	while e>tol or e is None:

		#Se calculan variables para hallar el optimo
		d = R*(xu-xl)  
		x1 = xl + d  #Posible optimo entre intervalo [xl,xu]
		x2 = xu - d  #Posible optimo entre intervalo [xl,xu]
		num = (1-R)*abs(xu-xl) #Numerador de la ecuacion del error absoluto

		#Se agrega información a la tabla
		ans += (str(i)+(4-len(str(i)))*' '+('%.4f' % xu)+(10-len(('%.4f' % xu)))*' '+('%.4f' % xl)+(10-len(('%.4f' % xl)))*' ')

		#Se escoge el mejor optimo entre x1 y x2
		if f(x1) < f(x2):
			xopt = x1
			xl = x2
			x2 = x1
		else:
			xopt = x2
			xu = x1
			x1 = x2

		e = num/xopt
		i += 1 #Se registra la iteración
		#Se agrega información a la tabla
		ans +=(('%.4f' % xopt)+(10-len(('%.4f' % xopt)))*' '+('%.4f' % e)+(10-len(('%.4f' % e)))*' '+('%.4f' % f(xopt))+'\n')

	print 'Busqueda dorada\n','Optimo: ',xopt,'\n','Error', e, '\n' #Se imprime el resultado

	#Se crea un archivo donde de texto donde se guardan los datos de la tabla
	archivo = open('dorada.txt','w')
	archivo.write(ans)
	archivo.close()

#Metodo Interpolación cuadrática
def icuadratica(x0,x1,x2,tol):

	i = 0
	e = None
	ans = 'I   x1        x2        x3        xopt      error     f(xopt)\n\n'

	while e > tol or e == None:

		x3 = ((f(x0)*((x1**2)-(x2**2))+f(x1)*((x2**2)-(x0**2))+f(x2)*((x0**2)-(x1**2)))/
		(2*f(x0)*(x1-x2)+2*f(x1)*(x2-x0)+2*f(x2)*(x0-x1)))
		
		x1a = x1

		ans += (str(i)+(4-len(str(i)))*' '+('%.4f' % x0)+(10-len(('%.4f' % x0)))*' '+('%.4f' % x1)+(10-len(('%.4f' % x1)))*' '
			+('%.4f' % x2)+(10-len(('%.4f' % x2)))*' '+('%.4f' % x3)+(10-len(('%.4f' % x3)))*' ')

		if x3>x1:
			if abs(f(x3)) > abs(f(x1)):
				x0 = x1
				x1 = x3
			else:
				x2 = x3
		else:
			if abs(f(x3)) > abs(f(x1)):
				x2 = x1
				x1 = x3
			else:
				x0 = x3

		e = abs((x1-x1a)/x1)
		i += 1

		ans += ('%.4f' % e)+(10-len(('%.4f' % e)))*' '+('%.4f' % f(x1))+'\n'

	print 'Interpolacion Cuadratica\n','Optimo: ',x1,'\n','Error', e, '\n' #Se imprime el resultado

	archivo = open('cuadratica.txt','w')
	archivo.write(ans)
	archivo.close()	

#Metodo de Newton
def newton(tol,L=700.):

	#Se definen los parametros iniciales
	i = 1  #Numero de la iteración
	x0 = 0.14*L #Distancia inicial
	e = None #Error
	ans = 'I   x0        x         error     f(x)\n\n' #Tabla para archivo de texto

	#Ciclo principal
	#Se lleva a cabo hasta obtener un error menor a la tolerancia ingresada por el usuario
	while e > tol or e == None: 
	    
		x = (x0 - d1f(x0) / d2f(x0))  #Se calcula la aproximacion al optimo 
		e = abs((x - x0) / x)  #Se calcula el error de la iteración
		
		ans += (str(i)+(4-len(str(i)))*' '+('%.4f' % x0)+(10-len(('%.4f' % x0)))*' '+('%.4f' % x)+(10-len(('%.4f' % x)))*' '
			+('%.4f' % e)+(10-len(('%.4f' % e)))*' '+('%.4f' % f(x))+'\n') #Se agregan datos a la tabla

		i += 1 #Se registra la iteración
		x0=x  #Se cambia el valor inicial por el mejor optimo para continuar el calculo de la siguiente iteracion

	#Se imprime el resultado de l optimo y el error en pantalla
	print 'Metodo de Newton\n','Optimo: ',x,'\n','Error', e, '\n' #Se imprime el resultado

	#Se crea un archivo donde de texto donde se guardan los datos de la tabla
	archivo = open('newton.txt','w')
	archivo.write(ans)
	archivo.close()	


#Se corren los metodos
dorada(0,700,0.00001)
newton(0.00001)
icuadratica(0.,420.,700.,0.00001)
raw_input('Presionar enter para finalizar')
