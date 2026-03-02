numeros =[]


for i in range(10):
    number = int(input(f'digite o {i+1}° numero:'))
    numeros.append(number)


media= sum(numeros)/len(numeros)
print(f'a media dos numeros foi {media:.0f}')
