#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
lista = []
lista_impar = []


n = int(input("Ingrese la cantidad de numeros de la lista: "))

for i in range(n) :
    num=int(input("Ingrese un numero: "))
    lista.append(num)
    if num%2 != 0:
     lista_impar.append(num)  

print("La lista entera tiene los siguientes valores :",lista)
print("Los valores impares son :",lista_impar)   
#FIN