import os
os.system('cls||clear')


def  verificar_par_impar(numero):

    if numero% 2 == 0 :
        print("o  numero é par ")
    else:
        print("o numero é impar")

numero =int(input("digite um numero: "))
verificar_par_impar(numero)