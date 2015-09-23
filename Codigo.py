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
c = 0
imp = 0
par = 0
delta = (b-a)/(len(Flujo)-1)

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
print (delta*(Flujo[0]+ 4*imp + 2*par + Flujo[len(Flujo)-1]))/3
