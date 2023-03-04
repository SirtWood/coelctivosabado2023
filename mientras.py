

controladora=100

print("***Empanadas el machetico***")
print("****************")
print("1.Agregar sabor empanada")
print("2.Mostrar sabor empanada")
print("3.Cambiar sabor empanada")
print("0.SALIR")

while(controladora!=0):
    empanada=None
    controladora=int(input("Digita una opcion: "))
    if controladora == 1:
        empanada=input("¿Cuál es el sabor?: ")
    elif controladora == 2:
        print(f"El sabor es: {empanada}")
    elif controladora == 3:
        empanada=input("¿Cuál es el sabor?: ")
    elif controladora == 0:
        print("Vuelve pronto")
    else:
        print("Opción inválida")