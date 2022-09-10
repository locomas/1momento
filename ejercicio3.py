"""3.Construir un programa para ir de compras en un supermercado
que permita la construcción del siguiente MENU:
1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
2. Digitar 2 para mostrar todos los productos registrados (+0.4)
3. Digitar 3 para permitir buscar por código un producto y editar el precio
de este (+0.4)
4. Digitar 4 para permitir buscar por código un producto y eliminar el
producto (+0.4)
5. Digitar 0 para SALIR"""

guardian = 200
# Ciclo While
print("Menu")
print("1. Agregar Producto")
print("2. Mostrar Productos")
print("3. Editar producto")
print("0. Salir")
productos = []
while guardian!=0:

    guardian = int(input("Digita una opcion"))
    if guardian ==1:
 
       producto={}

       producto['codigo']= input("digite el codigo del producto")
       producto['nombre'] =input("digite el nombre del producto")
       producto['precio']=input("digite el precio del producto") 
       productos.append(producto)
        
    elif guardian ==2:
         print(productos)

    elif guardian ==3:
        busca = int(input("digite el codigo del producto"))
        for producto in productos:
             if(busca == productos['codigo']):
                print("lo encontre")
            
                
    elif guardian ==0:
        break
    else:
        print("no valido")

else:
    print("Terminé")