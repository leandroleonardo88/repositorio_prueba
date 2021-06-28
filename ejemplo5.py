#Definir una lista que almacene 5 enteros
#Sumar todos sus eleentos y mostrar dicha suma

lista = [5,3,2,7,11]
suma = 0
x = 0

while x<len(lista):
    suma += lista[x]
    x+=1

print("Los elementos de la lista son: ", lista)
print("La suma de la lista es: ",suma)

lista.sort()
lista.reverse()