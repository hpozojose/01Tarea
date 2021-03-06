'''
Este codigo contiene los algoritmos que grafican
los datos de sun_AM0.dat
'''
import matplotlib.pyplot as plt
import numpy as np
import astropy.constants as const
import astropy.units as u
import math
plt.figure(1)
plt.clf()

Longitud = np.loadtxt('sun_AM0.dat', usecols=[0])
Flujo = np.loadtxt('sun_AM0.dat', usecols=[1])
#Rescato los datos por columnas del archivo sun_AM0
Longitud *= 10
Flujo *= 100
#amplifico los datos para que queden en las unidades indicadas en el grafico
plt.xscale("log")
#escala logaritmica
plt.plot(Longitud, Flujo)
plt.xlabel('$Longitud\,de\,onda\,[\AA] $')
plt.ylabel('$Flujo\, [ergs \cdot s^{-1} \cdot cm^{2} \cdot \AA]$')
plt.title('$Espectro\,del\,Sol$')
plt.show()

'''
Lo que sigue es el codigo que usaremos para integrar los datos y obtener
el espectro del Sol
'''
a = Longitud[0]
b = Longitud[len(Flujo)-1]
c = 1
imp = 0
par = 0
delta = (b-a)/670000

def Flujo_x(x):
    '''
    A un valor de Longitud con posicion i le asigna un valor de la
    Flujo con la misma posicion
    '''
    return Flujo[x]
while c < (len(Flujo)-1):
    if c % 2 == 0:
        par += Flujo_x(c)

    elif c % 2 == 1:
        imp += Flujo_x(c)
    c += 1
a02 = (1.49597870*(10**13))**2
inte = (delta*(Flujo[0]+ 4*imp + 2*par + Flujo[len(Flujo)-1]))/3

'''
algoritmo para separar las posiciones pares e impares, ademas de identificarlas
va sumando las funciones dependiendo de la posicion, lo hace por hasta la
cantidad total de datos, luego imprimo el resultado de la integracion,
cuyo algoritmo escrito abajo corresponde al algoritmo de simpson.
'''
print "Luminosidad Parte 2: ", 4*np.pi*a02*inte

'''
Parte 3 de la tarea, donde nos piden integrar pero ahora usando la formula
de planc y un arreglo de x
'''

cp = 1
impp = 0
parp = 0
eps = 0.00001
K = 9718787927.976933

def Planc_x(x):
# A un valor de x le asigna un valor usando la formula de Planc
    return (((np.tan(x))**3)*(1+(np.tan(x)**2)))/(np.exp(np.tan(x))-1)
Puntos = 200
ap = 0.01
bp = (np.pi/2)-0.01
xplanc = np.linspace(ap, bp, Puntos)
Rint = 0
deltap = (bp-ap)/(len(xplanc)-1)
while np.fabs(Rint - (np.pi**4)/15) >= eps :
#Compara el valor de la integral con el resultado que debiese dar, si el error
#es muy grande, aumenta el numer de puntos en el intervalo en x
    while cp < (len(xplanc)-2) :
        if cp % 2 == 0:
            parp += Planc_x(xplanc[cp])
        elif cp % 2 == 1:
            impp += Planc_x(xplanc[cp])
        cp += 1
#separa los valores de la funcion en par e impares para luego integrar mediante simpson
    Rint = (deltap*(Planc_x(ap)+ 4*impp + 2*parp + Planc_x(bp)))/3
    Puntos = Puntos + 100
    #aumenta la cantidad de puntos, disminnuyento el delta
    xplanc = np.linspace(ap, bp, Puntos)
    deltap = (bp-ap)/(len(xplanc)-1)
rsol = 6.960*(10**10)
print "Luminosidad Parte 3: ", Rint*K*4*np.pi*(rsol**2)



'''
El siguiente codigo reevalua los datos obtenidos en la segunda parte,
esta vez usando librerias a fin de comparar los valores obtenidos
en la parte 2
'''
i = 0
yplanc = []
while i < len(xplanc):
    yplanc.append(K*Planc_x(xplanc[i]))
    i += 1
#Crea un lista donde va guardando los valores de Planc_x(x)
import scipy.integrate
I2S = scipy.integrate.simps(Flujo, Longitud)
I2T = scipy.integrate.trapz(Flujo, Longitud)
#Integra con simps y tranz desde las librerias los datos analiticos
I3S = scipy.integrate.simps(yplanc, xplanc)
I3T = scipy.integrate.trapz(yplanc, xplanc)
#Integra con simps y tranz desde las librerias el arreglo y sus valores dada la integral de planc
print "Luminosidad Simps 2: ", 4*np.pi*a02*I2T
print "Luminosidad Tranpz 2: ", 4*np.pi*a02*I2S
print "Luminosidad Simps 3: ", I3T*4*np.pi*(rsol**2)
print "Luminosidad Tranpz 3: ", I3S*4*np.pi*(rsol**2)

''''
Para estimar el radio del sol igualamos los datos obtenidos en la parte 2 y 3,
donde en la parte dos obtemos la constante solar y en la 3, sigma por la
temperatura efectiva del sol a la cuarta, por ende agregamos las constantes para
compararlas como luminosidad y despejando el radio de la tierra
'''
radio_est = math.sqrt((inte*a02)/(K*Rint))
print "Radio Estimado del Sol: ", radio_est
