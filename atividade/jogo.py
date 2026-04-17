import os, random

sorteado =  random.randint(1,100)
tentativas = 0

while True:
    numero = int(input('digite o numero magico'))
    tentativas = tentativas+1
    os.system('cls || clear')
    if(numero == sorteado):
        print(f'parabens voce acertou o numero magico em {tentativas} tentativas')
        break
    elif(numero>sorteado):
        print(f'o numero magico  é menor --  {tentativas} tentativas')
    else:
        print(f'o numero magico é maior -- {tentativas} tentativas')
