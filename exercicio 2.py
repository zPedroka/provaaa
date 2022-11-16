def verificarNumero(numero):
    if numero %2==0:
        return True
    
    return False

numero=int(input("qual é o seu numero"))
if verificarNumero(numero)== True:
    print("numero é par")
else:
    print("numero é impar")