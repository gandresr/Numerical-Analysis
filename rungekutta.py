#-*- coding: utf-8 -*-

#Ecuacion diferencial que describe el comporatmiento de la variación de concentracion del reactivo C_a
#Depende de la concentración de los reactivos C_a y C_c
def dca_dt(ca,cc):
	return -0.1*ca*cc+0.3*ca

#Ecuacion diferencial que describe el comporatmiento de la variación de concentracion del reactivo C_b
#Depende de la concentración de los reactivos C_a, C_b y C_c
def dcb_dt(ca,cb,cc):
	return -0.01*ca*cc+0.2*cb

#Ecuacion diferencial que describe el comporatmiento de la variación de concentracion del reactivo C_c
#Depende de la concentración de los reactivos C_a, C_b y C_c
def dcc_dt(ca,cb,cc):
	return -0.1*ca*cc-0.3*cb+0.3*cc

#Método de Runge Kutta de orden 4
#Permite calcular de manera aproximada la variación de la concentración de los reactivos 
#en un intervalo de tiempo determinado.
#Dado que es un método aproximado describe la función paso por paso por ende el usuario debe definir el tamaño del paso de tiempo 'h'
def rk4(ca0,cb0,cc0,h,tf):

	ca = [ca0] #Vector de conectración del reactivo C_a
	cb = [cb0] #Vector de conectración del reactivo C_b
	cc = [cc0] #Vector de conectración del reactivo C_c
	tiempo = [0] #Vector de tiempo

	t = 0

	while t < tf/h:
		
		#Calculo de las constantes K1, K2, K3 Y K4 para la ecuación del reactivo C_a
		k1a = dca_dt(ca[t],cc[t])
		k2a = dca_dt((ca[t]+k1a*h/2),cc[t])
		k3a = dca_dt((ca[t]+k2a*h/2),cc[t])
		k4a = dca_dt((ca[t]+k3a*h),cc[t])
		ca.append(ca[t]+(k1a+2*k2a+2*k3a+k4a)*h/6) #Aproximación del valor de la función con el RK4

		#Calculo de las constantes K1, K2, K3 Y K4 para la ecuación del reactivo C_b
		k1b = dcb_dt(ca[t],cb[t],cc[t])
		k2b = dcb_dt(ca[t],(cb[t]+k1b*h/2),cc[t])
		k3b = dcb_dt(ca[t],(cb[t]+k2b*h/2),cc[t])
		k4b = dcb_dt(ca[t],(cb[t]+k3b*h),cc[t])
		cb.append(cb[t]+(k1b+2*k2b+2*k3b+k4b)*h/6) #Aproximación del valor de la función con el RK4

		#Calculo de las constantes K1, K2, K3 Y K4 para la ecuación del reactivo C_c
		k1c = dcc_dt(ca[t],cb[t],cc[t])
		k2c = dcc_dt(ca[t],cb[t],(cc[t]+k1c*h/2))
		k3c = dcc_dt(ca[t],cb[t],(cc[t]+k2c*h/2))
		k4c = dcc_dt(ca[t],cb[t],(cc[t]+k3c*h))
		cc.append(cc[t]+(k1c+2*k2c+2*k3c+k4c)*h/6) #Aproximación del valor de la función con el RK4

		t += 1 
		tiempo.append(round(t*h,1)) #Incremento del vector de tiempo

	return tiempo,ca,cb,cc