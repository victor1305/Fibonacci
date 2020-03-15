print("Programa para calcular la Secuencia de Fibonacci, versión 2.0")

def fibonacci(n):
        
    if n == 0:

        print("0")

        preguntaOtroNumero()

    elif n>=1:

        a = 0
        b = 1
        c=a+b

        print (a)

        print (b)
        


        while n > c:

            c=a+b
            a=b
            b=c

            print (b)

        preguntaOtroNumero()
       
    else:

        print("El número no puede ser negativo.")

        print("Introduzca un número mayor que 0. \n")

        preguntaOtroNumero()


def ejecucionFuncion():

    n = int(input ("Introduzca el número hasta el que quiera obtener la secuencia de Fibonacci: "))

    fibonacci(n)

def ejecucionRepetida():

    n = int(input ("\nIntroduzca un nuevo número hasta el que quiere obtener la secuencia de Fibonacci: "))

    fibonacci(n)

def preguntaOtroNumero():

    q = input ("\n¿Quiere calcular la secuencia de Fibonacci de otro número?\n")

    if q == "Sí":
        
        ejecucionRepetida()

    elif q== "No":

        print ("\nEl programa ha finalizado.")

    else:

        print ("\nResponda con Sí o No. \n")

        preguntaOtroNumero()



ejecucionFuncion()