"""
Obtener números primos, en un rango específico, 
el usuario ingresa el valor mínimo y el máximo 
(con input), el programa busca y guarda en una 
lista los números primos que se encuentran en el 
rango de valores dado. Al final hacen un plot de 
la lista.
"""
import matplotlib.pyplot as graf 

#Obtiene los límites del intervalo
print("Límite inferior cerrado:",end=" ")
Linf=int(input())
print("Límite superior abierto:",end=" ")
Lsup=int(input())

#Eratóstenes
Primos=[]#Arreglo para guardar los primos en [0,Lsup)
Ploti=[]#Arreglo para guardar los primos del itervalo [Linf,Lsup)
Flags = [1 for i in range(Lsup)]#Arreglo para marcar y descartar 
Flags[0] = Flags[1] = 0 #Descarta de entrada al 0 y al 1, puesto que el algoritmo es válido para empezar a iterar con múltiplos de 2 

for i in range(Lsup):
    if Flags[i]:
        Primos.append(i)#Marca el primer primo no marcado
        h = 2
        while i*h < Lsup:
            Flags[i*h] = 0#Quita los multiplos de i en el intervalo
            h += 1   
#Una vez que obtiene los primos de [0,Lsup) guarda los pertienente aL intervalo [Linf,Lsup) en el arreglo Ploti
print("---------------")
for i in Primos:
    if i>=Linf  and i <Lsup:
        Ploti.append(i)
print(Ploti) 

#Gráfica         
print("---------------")
print("\nPrimos encontrados:",len(Ploti))
graf.plot(Ploti)

