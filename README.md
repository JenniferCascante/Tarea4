###Universidad de Costa Rica 

###Escuela de Ingeniería Eléctrica

###IE405- Modelos Probabilísticos de Señales y Sistemas 

###Tarea 4

###Jennifer Cascante Peraza  B51626

-Punto 1: Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

Primero se procedió a importar los bits, y a definir los parámetros de frecuencia, tiempo de muestra, cantidad de muestra, además de generar las señal sinusoidal a la cual llamo como señal sin modualar.
![T4](1.JPG)

Para la modulación "Binary Phase Shift Keying" BPSK, la cual consiste en variar el ángulo de la onda senusoidal ya sea a 0 o 180, dependiendo del valor del bit. A partir de la señal sin modular de la figura anterior, se logra la modulación recorriendo con un for y definiendo para el vector de la señal modulada con 10 bits, si voy tener un seno cuando el bit sea 1 o el desfase de 180 grados es decir -seno, si el el bit es 0. Obteniendo así la siguiente señal modulada.

![T4](2.JPG)


-Punto 2: Calcular la potencia promedio de la señal modulada generada.
Mediente al método descrito en lecciones se obtiene:
La potencia promedio es 0.4900009800019598 W

-Punto 3:  Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.
Para obtener la simualción del canal ruidoso AWGN en el rango de -2dB hasta 3dB, primero se establecio un vector con con este intervalo de datos, y por medio de un for se recorrió los elementos que me generan dicho canal, como lo son la potencia del ruido, la desviación estándar del ruido respecto a la señal del ruido (generada en el punto 1), en la imagen genereda se puede apreciar que la diferencia de las señales para los distintos SNR es muy pequeña, esto debido a que el esquema de modulación BPSK es muy robusto.  
![T4](3.JPG)

Además, se generó de igual manaero un solo canal con un SNR:-2
![T4](4.JPG)

-Punto 4: Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.

Densidad espectral de potencia de la señal, antes del canal ruidoso
![T4](5.JPG)

Densidad espectral de potencia de la señal, después del canal ruidoso
![T4](6.JPG)

-Punto 5: Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.
En este punto se realiza una decodificación de la onda mediante el método visto en lecciones, de ahí se obtiene la cantidad de  bits que se recibieron según el canal de ruido, gracias al "bits error date" (defibido en el código como BER), nos indica qu etan buena fue la transmisión.
Aquí los resultados obtenidos para todos los valores de SNR desde -2dB hasta -3dB:

-Cuando el canal tiene un ruido de SNR= -2dB entonces, la senal decodificada tiene un total de 12.0 errores en 10000 bits con una tasa de error de 0.0012.

-Cuando el canal tiene un ruido de SNR= -1dB entonces, la senal decodificada tiene un total de 5.0 errores en 10000 bits con una tasa de error de 0.0005.

-Cuando el canal tiene un ruido de SNR= 0dB entonces, la senal decodificada tiene un total de 1.0 errores en 10000 bits con una tasa de error de 0.0001.

-Cuando el canal tiene un ruido de SNR= 1dB entonces, la senal decodificada tiene un total de 0.0 errores en 10000 bits con una tasa de error de 0.0.

-Cuando el canal tiene un ruido de SNR= 2dB entonces, la senal decodificada tiene un total de 0.0 errores en 10000 bits con una tasa de error de 0.0.

-Cuando el canal tiene un ruido de SNR= 3dB entonces, la senal decodificada tiene un total de 0.0 errores en 10000 bits con una tasa de error de 0.0.

-Punto 6: Graficar BER versus SNR.
Se muestra una gráfica en la cual se comparten los valores de la tasa de error con los respectivos valores de SNR en el rango establecido.

![T4](7.JPG)
