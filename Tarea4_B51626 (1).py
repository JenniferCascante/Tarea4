#!/usr/bin/env python
# coding: utf-8

# In[42]:


#Tarea 4 Modelos: Procesos aleatorios. 
#Jennifer Cascante Peraza/ B51626
#Apartir de los ejemplos visto en clases.

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Se extrae los bits en un vector
bits= np.array(pd.read_csv("bits10k.csv",header=None))

# Frecuencia de operación
f = 5000 # Hz

# Duración del período de cada onda
T = 1/f # 1 ms

# Número de puntos de muestreo por período, que me va dibujar la señal
p = 50

# Puntos de muestreo para cada período
tp = np.linspace(0, T, p)

# Creación de la forma de onda de la portadora
sen= np.sin(2*np.pi * f * tp)

# Visualización de la forma de onda de la portadora
plt.plot(tp, sen)
plt.title('Señal sin modular')
plt.xlabel('Tiempo / s')
plt.show()

# Frecuencia de muestreo
fs = p/T # 50 kHz

#Tamaño del vector de datos bits debería ser 10k
N=len(bits)

# Creación de la línea temporal para toda la señal Tx
t = np.linspace(0, N*T, N*p)

# Inicialización del vector de la señal modulada Tx
senal = np.zeros(t.shape)

# Creación de la señal modulado BPSK

for i,j in enumerate(bits):
    if j==1:
        senal[i*p:(i+1)*p] = sen
    else:
        senal[i*p:(i+1)*p] = -sen

            
# Visualización de los primeros bits modulados
pb = 10 # primeros bits definidos como pb
plt.plot(senal[0:pb*p])
plt.xlabel('Tiempo / S')
plt.title('Señal modulada')
plt.show()






# In[44]:


#Punto 2
from scipy import integrate

# Potencia instantánea
Pinstantanea = senal**2

# Potencia promedio a partir de la potencia instantánea
Ps = integrate.trapz(Pinstantanea, t) / (N * T)
print('La potencia promedio es',Ps)


# In[48]:


#Punto 3
# Relación señal-a-ruido deseada
#Imprime la visualizacion de cada SNR en la señal portadora:
# 1.De todo el rango de decibeles
SNR = np.arange(-2,4)
print('SNR es el vector:',SNR)
for f in SNR:
    Pn=0
    # Potencia del ruido para SNR y potencia de la señal dadas
    Pn= Pn+(Ps /(10**(f/10)))
    sigma = np.sqrt(Pn)# Desviación estándar del ruido
    ruido = np.random.normal(0, sigma, senal.shape)     # Simalación  de la señal recibida en el canal 
    Rx = senal + ruido  #Se crea ruido a partir de (Pn = sigma^2)
    plt.plot(Rx[0:5*p])


plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Canal ruidoso con SNR desde -2dB hasta 3dB')
plt.show()     
    
#2.De solo un canal como lo especifica la tarea, se elegió -2dB para la muestra.
SNR2=-2
Pn1 = Ps / (10**(SNR2 / 10))
sigma2=np.sqrt(Pn1)
ruido1 = np.random.normal(0, sigma2, senal.shape)
Rx1 = senal + ruido1

plt.plot(Rx1[0:5*p])

plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Canal ruidoso con SNR de -2dB')
plt.show()     

#print(ruido)
#print(Rx)


# In[18]:


#Punto 4:
from scipy import signal
#Señal inicial antes de pasar por el canal ruidoso de la parte 3
fw, PSD = signal.welch(senal, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad Espectral de Potencia / V**2/Hz')
plt.title('Señal antes de pasar por el canal ruidoso')
plt.show()

# # Señal cuando ya ha pasado por el canal ruidoso.
fw, PSD = signal.welch(Rx, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad Espectral de Potencia / V**2/Hz')
plt.title('Señal cuando ya ha pasado por el canal ruidoso')
plt.show()


# In[52]:


#Punto 5
# Pseudo-energía de la onda original
PE= np.sum(sen**2)

SNRf=np.arange(-2,4)#ya utilizado en el punto 3 

BER= np.zeros(SNRf.shape)

# Decodificación de la señal por detección de energía
for j in range(len(SNRf)):
    Pn2=Ps/(10**(SNRf[j]/10))
    Res2=np.sqrt(Pn2)
    gen=np.random.normal(0,Res2,senal.shape)
    Ruido2=senal+gen
    BitsR2=np.zeros(bits.shape)# bits recibidos
    
    for w, z in enumerate(bits):
        Ep2 = np.sum(Ruido2[w*p:(w+1)*p] * sen)
        if Ep2 > PE/2:
            BitsR2[w] = 1
        else:
            BitsR2[w] = 0

    error = np.sum(np.abs(bits - BitsR2))
    BER[j] = error/N
    print('-Cuando el canal tiene un ruido de SNR= {}dB entonces, la senal decodificada tiene un total de {} errores en {} bits con una tasa de error de {}.'.format(SNRf[j],error, N, BER[j]))


# In[53]:


#Punto 6
# se realiza la grafica a partir de los arreglos de SNRf y BER
plt.figure()
plt.plot(SNRf,BER2)
plt.xlabel('SNR')
plt.ylabel('BER')
plt.title('BER VS SNR')


# In[ ]:




