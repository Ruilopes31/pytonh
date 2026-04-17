import os

os.system('cls||clear')

def verificar(x):
    n =  x.replace('','')
    qletras = len(n)
    print(f'o seu nome {x} tem  {qletras} letras')




nome = input('digite seu nome')
verificar(nome)

