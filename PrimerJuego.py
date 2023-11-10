import random
numero = random.randint(0, 100)
contador = 0
print('Intenta adivinar un numero del 0-99.') 
intento = -1
while intento != numero:
    intento = int(input())
    if intento < 0 or intento > 99:
        print("Error, el numero debe estar comprendido entre 0-99")
    else: 
        if intento < numero:
            print("Demasiado pequeño")
        elif intento > numero:
            print("Demasiado grande")
        contador += 1
else: 
    print("¡Ha ganado!")
    print("Has realizado", contador, "intentos")