#Definindo Listas necessarias

numeros = list()
pares = list()
impares = list()

#Laço para pedir os valores

for c in range(6):
    numeros.append(int(input(f'Digite o {c + 1} valor: ')))
    if numeros[c] % 2 == 0:
        pares.append(numeros[c])
    else:
        impares.append(numeros[c])
print('=' * 40)

if pares:
    print('Os numeros pares digitados foram: ',end = '')
    for item in pares:
        print(f'{item}, ',end='')
        
else:
    print('\nNão foram digitados numeros pares')

if impares:
    print('\nOs numeros impares digitados foram: ', end='')
    for item in impares:
        print(f'{item}, ',end='')
        
else:
    print('\nNão foram digitados numeros impares')
    
print(f'\nA soma dos numeros pares resulta em {sum(pares)}')
print(f'Foram digitados {len(impares)} numeros impares')
print('=' * 40)
