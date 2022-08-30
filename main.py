#adivina que numero es, generado por la computadora
import random     #random es aleatoria en español                      #con esta sentencia importamos imporatmos un modulo, modulo es un archivo de python que contiene funcones y elementos utiles que usamos en el programo


def adivina_el_número(x): # siempre despues de definir una funcion colocar los dos puntos al final

    print("==========================")
    print("¡¡Bienvenido/a al juego!! ")
    print("==========================")
    print("Tu objetivo, es adivinar el número que nos de la computadora.")

    número_aleatorio = random.randint(1, x)  #randint viene de random(aleatorio) e int que viene de entero, numero aleatorio entre 1 y x inclusive

    intuición = 0

    while intuición != número_aleatorio: 
        intuición = int(input(f"Adivina el número entre 1 y {x}: "))  #f-string, nos permite remplezar el valor de una variable o de una exprecion de forma mas concisa

        if intuición < número_aleatorio:
            print("vuelve a intentar, número chico.")
        elif intuición > número_aleatorio:
            print("Vuelve a intentar, número grande.")

    print(f"felicitaciones! número correcto. {número_aleatorio} Te ganaste otra vuelta.")



adivina_el_número(30)
