#importo el archivo funciones
import funciones

#realizamos el llamado de la funcion
#print(funciones.resta(30, 10))
while True:

    print("Bienvenido!, Que desea hacer?")

    #Digite una de las opciones
    opcion = int (input("1- Restar, 2- Sumar , 3- Multiplicar "))
    if opcion == 1 or opcion == 2 or opcion == 3 :
        #Solicito numeros para realizar la operacion
        num1 = int(input("Ingresa el primer numero "))
        num2 = int(input("Ingresa el segundo numero "))

        #Valida la opcion y llama la funcion correspondiente
        if opcion == 1:

            print(funciones.resta(num1, num2))

        elif opcion == 2:

            print(funciones.suma(num1, num2))
            
        else:

            print(funciones.multiplicar(num1, num2))

        break

    else:

        print("Digite una opcion valida")
    

