def busqueda(matriz, valor, X):
    posl = -1
    pos = -1
    for i in range(len(matriz)):
        if matriz[i][X] == valor:
            posl = i
            pos = X
    return posl, pos

def caracteres(nombre, X):
    sobrepasa = False
    if len(nombre) != X:
        sobrepasa = True
    return sobrepasa

def main():
    usuario_contraseña = []
    parar = False
    while parar == False:
        lista = []
        print("BIENVENIDO")
        print("1 - Registrarse")
        print("2 - Iniciar sesion")
        elegir = int(input())
        while elegir < 1 or elegir > 2:
            print("elija correctamente la opcion")
            print("1 - Registrarse")
            print("2 - Iniciar sesion")
            elegir = int(input())
        
        #REGISTRO DE USUARIO
        if elegir == 1:
            print("-----REGISTRO DE USUARIO-----")
            usuario = input("Ingrese un nombre de usuario: ")
            cantidad = caracteres(usuario, 10)
            while cantidad == True:
                print("El nombre de usuario debe tener 10 caracteres")
                usuario = input("Ingrese un nombre de usuario: ")
                cantidad = caracteres(usuario, 10)
            validar1, validar2 = busqueda(usuario_contraseña, usuario, 0)
            while validar1 != -1:
                print("Usuario ya existente")
                usuario = input("Ingrese un nombre de usuario: ")
                cantidad = caracteres(usuario, 10)
                while cantidad == True:
                    print("El nombre de usuario debe tener 10 caracteres")
                    usuario = input("Ingrese un nombre de usuario: ")
                    cantidad = caracteres(usuario, 10)
                validar1, validar2 = busqueda(usuario_contraseña, usuario, 0)
            contraseña = input("Ingrese una contraseña: ")


if __name__ == "__main__":
    main()