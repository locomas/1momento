
"""1.Construir un programa que permita ingresar N (cantidad digitada por
el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3
fueron ingresados (+1)"""


numeros =[]
multiplos = []
guardian = int(input("digite el numero de numeros que quiere digitar"))
i=0
while i < guardian:
    numero = int(input("Digita el numero"))+ i 
    numeros.append(numero)
    i = i +1

    if  numero%2==0 or numero%3==0:
     multiplos.append(numero)
    else:
        ("no hay nada")
    
print(f"los multiplos de 2 y 3 son " ,multiplos)
print(multiplos)    


        



    