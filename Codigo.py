'''
Este codigo contiene los algoritmos que grafican
los datos de sun_AM0.dat
'''
import matplotlib.pyplot as plt
import numpy as np

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
plt.savefig('grafico.png')
#guardo el grafico

'''
Lo que sigue es el codigo que usaremos para integrar los datos y obtener
el espectro del Sol
'''
a = Longitud[0]
b = Longitud[len(Flujo)-1]
c = 1
imp = 0
par = 0
delta = (b-a)/500000000
print len(Flujo)-1
def Flujo_x(x):
    '''
    A un valor de Longitud con posicion i le asigna un valor de la
    Flujo con la misma posicion
    '''
    return Flujo[x]
while c < (len(Flujo)-2):
    if c % 2 == 0:
        par += Flujo_x(c)

    elif c % 2 == 1:
        imp += Flujo_x(c)
    c += 1
'''
algoritmo para separar las posiciones pares e impares, ademas de identificarlas
va sumando las funciones dependiendo de la posicion, lo hace por hasta la
cantidad total de datos, luego imprimo el resultado de la integracion,
cuyo algoritmo escrito abajo corresponde al algoritmo de simpson.
'''
print (delta*(Flujo[0]+ 4*imp + 2*par + Flujo[len(Flujo)-1]))/3

'''
Parte 3 de la tarea, donde nos piden integrar pero ahora usando la formula
de planc y un arregla de x
'''
import astropy.constants as const
import astropy.units as u

cp = 1
impp = 0
parp = 0
eps = 0.00001
K = 9718787927.976933

def Planc_x(x):
# A un valor de x le asiga un valor usando la formula de Planc
    return (((np.tan(x))**3)*(1+(np.tan(x)**2)))/(np.exp(np.tan(x))-1)
Puntos = 200
ap = 0.01
bp = (np.pi/2)-0.01
xplanc = np.linspace(ap, bp, Puntos)
Rint = 0
deltap = (bp-ap)/(len(xplanc)-1)
while np.fabs(Rint - (np.pi**4)/15) >= eps :
    while cp < (len(xplanc)-2) :
        if cp % 2 == 0:
            parp += Planc_x(xplanc[cp])
        elif cp % 2 == 1:
            impp += Planc_x(xplanc[cp])
        cp += 1
    Rint = (deltap*(Planc_x(ap)+ 4*impp + 2*parp + Planc_x(bp)))/3
    Puntos = Puntos + 100
    xplanc = np.linspace(ap, bp, Puntos)
    deltap = (bp-ap)/(len(xplanc)-1)
print Rint*K
