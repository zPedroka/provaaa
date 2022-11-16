matriz=[
    [0,0,0,0,],
    [0,0,0,0,],
    [0,0,0,0,],
    [0,0,0,0,]
]
  
for linha in range (4):
    for coluna in range (4):
        matriz [linha][coluna]= int(input("qual é o numero escolhido?"))

for indice in range(4):
    print(matriz[indice])

contador=0
for line in matriz:
    for numero in line:
        if numero >10:
            contador= contador + 1
            print(f'a matriz possui {contador} valores maior que 10')