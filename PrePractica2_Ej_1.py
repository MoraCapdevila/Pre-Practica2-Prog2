#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
lista = []
a = int(input("Ingresar el valor de a: "))
b = int(input("Ingresar el valor de b: "))
lista.append(a)
lista.append(b)
max_valor = max(lista)
print("El maximo valor es: ", max_valor)

if lista[0] > lista[1] :
    max_valor = lista[0]
else:
    max_valor = lista[1]

print("El maximo valor es: " , max_valor)


#FIN