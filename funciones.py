#funcion sin parametros y sin retorno
def espacio():
    print("\n"*2)
    print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
    
def menu():
    espacio()
    print(".-.-.- M E N U -.--.-.-.-.-.-")
    print("")
    print("1-. Sumar")
    print("2.- Restar")
    print("3.- Dividir")
    print("4.- Multiplicar")
    print("")

# funcion sin parametro y con retorno
def suma1():
    total=4+5
    return total
# funcion con parámetro y sin retorno
def sumar(a,b):
    tot=a+b
    print("El total es : ",tot)
    
# funcion con parámetro y CON retorno
def restar(a,b):
    tot=a-b
    print("El total es : ",tot)
    return tot

#####################################################
while(True):
    menu()
    op = int(input("Ingrese una opción : "))
    if op==1:
        numerito1=int(input("Ingrese numero 1 : "))
        numeroto2=int(input("Ingrese numero 2 : "))
        sumar(numerito1,numeroto2)
    elif op==2:
        numerito1=int(input("Ingrese numero 1 : "))
        numeroto2=int(input("Ingrese numero 2 : "))
        total=restar(numerito1,numeroto2)
        print("el total es : ",total)










        
