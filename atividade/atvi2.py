numeros =[]


for i in range(5):
     temp = int(input(f'digite sua temperatura :'))
     numeros.append(temp)
maior = max(numeros)
menor = min(numeros)

media= sum(numeros)/len(numeros)
print(f'a maior temperatura: {maior}º celsius')
print(f'a menor temperatura foi: {menor}º celcius')
print(f'a media da temperatura  foi: {media:.2f}')

compras= []
while True:
    valor= float(input("digite um numero seu miseralvel: "))
    if(valor!=0):
        compras.append(valor)
    else:
        break

somatorio = sum(compras)
print(f'o valor total da compra é R$ {somatorio}')