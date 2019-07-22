import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dado = [1,2,3,4,5,6]                                                            #Lista con los numeros de un dado

#Actividad 1
###############################Pregunta 1######################################
probexp= []                                                                     #Lista vacia para guardar las probabilidades
error=[]                                                                        #Lista vacia para guardar los errores                                              
rep = [1,2,3,4,5,6,7]                                                           #Lista Con los ordenes de magnitud para efectuar la simulacion

for n in rep:                                                                   #Iteracion Para cada orden de magnitud
    contador=0                                                                  #Contador que registra los pares de 6
    for i in range(10**n):                                                      #Iteracion por lanzamiento de dados
        aux=np.random.choice(dado,2)                                            #Escojer un numero al azar de la lista dados, 2 veces
        if list(aux) == [6,6]:                                                  #Si es par de 6, sumar 1 al contador
            contador+=1
    print(float(contador)/10**n)                                                
    probexp.append(float(contador)/10**n)                                       #Agregar resultado de la frecuencia
    error.append(abs(float(contador)/10**n - 1/36))                             #Agregar resultado de el error
 
plt.plot(rep,probexp,'bo')                                                      #Graficar las frecuencias
plt.show()
plt.plot(rep,error,'bo')                                                        #Graficar los errores
plt.show()

###############################Pregunta 3######################################
#Parte 1
cont = 0                                                                        #Contador para las iteraciones que cumplen las condiciones
for j in range(10**6):                                                          #iterar un millon de veces, para asegurar un buen resultado
    aux=np.random.choice(dado,5)                                                #Escojer un numero al azar de la lista dados, 5 veces
    caux1 = 0                                                                   #Variable para guardar cantidad de pares 
    caux2 = 0                                                                   #Variable para ver si hay escala
    for i in list(np.bincount(aux)):                                            #Se aplica bincount a la lista, y se itera en el resultado
        if i == 2:                                                              #si hay un par se suma uno al contador de pares
            caux1+=1
        elif i == 3:                                                            #si hay un trio se marca la variable de trios
            caux2+=1
        elif i == 4:                                                            #Si hay 4 iguales, se suma 2 al contador de pares
            caux=2
        elif i == 5:                                                            #Si hay 5 iguales, se marca el trio y se suma un par
            caux1=1
            caux2=1
        
    if (caux1 == caux2 == 1) or (caux1 == 2) or (caux1 == caux2 == 0):              #Luego se evaluan las condiciones, par y trio, 2 pares, y escala donde ambos son 0(Se concidera escala que da vuelta)
       cont+=1
       
print (cont/10**6)

#Parte 2 y 3
primos = [11,13,17,19,23,29,31,37,41,43,47,53,59]                               #Lista con los primos entre 10 y 60
perfect = [16,25,36,49]                                                         #Lista con los cuadrados perfectos entre 10 y 60
cont1 = 0                                                                       #Contador para primos
cont2 = 0                                                                       #Contador para cuadrados perfectos
for i in range(10**6):
    aux=np.random.choice(dado,10)                                               #Escojer un numero al azar de la lista dados, 10 veces
    if sum(aux) in primos:                                                      #aumentar cont1 si la suma de los dados escojidos se encuntra en la lista primos 
        cont1+=1    
    if sum(aux) in perfect:                                                     #aumentar cont2 si la suma de los dados escojidos se encuntra en la lista de cuadrados perfectos
        cont2+=1
print (cont1/10**6)
print (cont2/10**6)
        