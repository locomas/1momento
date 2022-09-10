"""2.Leer el nombre de 10 frutas {nombre, color, precio} para preparar un
salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al
mismo tiempo en sentido inverso al ingresado+(1)
"""

# Ciclo for con python

guardian = 10
# Ciclo While
print("Menu")
print("1. Agregar Fruta")
print("2.Mostrar frutas")
print("0. Salir")
frutas = []

while guardian!=0:
    guardian = int(input("Digita una opcion"))
    fruta = {}
    if guardian ==1:
        
       fruta['nombre']= input("digite el nombre de la fruta: ")
       fruta['color'] =input("digite el color: ")
       fruta['precio']=input("digite el precio: ")       
       frutas.append(fruta)     
    elif guardian ==2:
      frutas.reverse()
      print(frutas)
         
    elif guardian ==0:
        break
    else:
        print("no valido")

else:
    print("Terminé")