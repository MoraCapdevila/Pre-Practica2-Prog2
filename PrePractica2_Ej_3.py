#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
try:
    num1 = int(input("Ingresar el primer numero: "))
    num2 = int(input("Ingresar el segundo numero: "))
    resultado = num1/num2
    print(f'El resultado de la division es -> {resultado}')
except ZeroDivisionError:
    print("¡ERROR!.El divisor es cero")
#FIN