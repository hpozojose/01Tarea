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
