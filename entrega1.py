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
                
                
                
if __name__ == "__main__":
    main()