def declarar_niveles():
    nivel_1 = [["L", "U", "N", "A"], ["P", "A", "N"], ["S", "O", "L"]]
    nivel_2 = [["C", "A", "S", "A"], ["M", "E", "S", "A"], ["G", "A", "T", "O"]]
    nivel_3 = [["S", "I", "L", "L", "A"], ["L", "A", "G", "O"], ["T", "I", "Z", "A"]]
    nivel_4 = [["P", "E", "R", "R", "O"], ["A", "V", "I", "O", "N"], ["F", "R", "U", "T", "A"]]
    nivel_5 = [["A", "V", "I", "O", "N", "E", "T", "A"], ["P", "A", "L", "M", "E", "R", "A"], ["S", "E", "R", "P", "I", "E", "N", "T", "E"]]
    nivel_6 = [["E", "L", "E", "F", "A", "N", "T", "E"], ["C", "A", "M", "I", "O", "N"], ["M", "A", "M", "N", "T", "E", "Q", "U", "I", "L", "L", "A"]]
    nivel_7 = [["M", "U", "R", "C", "I", "E", "L", "G", "O"], ["S", "E", "M", "A", "F", "O", "R", "O"], ["C", "O", "C", "O", "D", "R", "I", "L", "O"]]
    nivel_8 = [["M", "A", "R", "I", "P", "O", "S", "A"], ["H", "I", "P", "O", "P", "O", "T", "A", "M", "O"], ["C", "A", "L", "E", "N", "D", "A", "R", "I", "O"]]
    nivel_9 = [["C", "A", "R", "R", "E", "T", "I", "L", "L", "A"], ["A", "R", "Q", "U", "I", "T", "E", "C", "T", "U", "R", "A"], ["E", "L", "E", "C", "T", "R", "I", "C", "I", "D", "A", "D"]]
    nivel_10 = [["M", "I", "C", "R", "O", "B", "I", "O", "L", "O", "G", "I", "A"], ["C", "I", "M", "N", "E", "M", "A", "T", "O", "G", "R", "A", "F", "I", "A"], ["D", "E", "S", "E", "M", "B", "A", "R", "C", "A", "R"]]
    niveles = [nivel_1, nivel_2, nivel_3, nivel_4, nivel_5, nivel_6, nivel_7, nivel_8, nivel_9, nivel_10]
    return niveles

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
            cantidad = caracteres(contraseña, 8)
            while cantidad == True:
                print("La contraseña debe tener 8 caracteres")
                contraseña = input("Ingrese una contraseña: ")
                cantidad = caracteres(contraseña, 8)
            monedas = 100
            nivel = 1
            lista.append(usuario)
            lista.append(contraseña)
            lista.append(monedas)
            lista.append(nivel)
            usuario_contraseña.append(lista)
            #[USUARIO , CONTRASEÑA, MONEDAS, NIVEL]
            #   0           1           2       3
        
        #INICIO DE SESION
        else:
            print("-----INICIO SESION-----")
            usuario = input("Ingrese su nombre de usuario: ")
            validar1, validar2 = busqueda(usuario_contraseña, usuario, 0)
            while validar1 == -1:
                print("Usuario no existente")
                usuario = input("Ingrese un nombre de usuario: ")
                validar1, validar2 = busqueda(usuario_contraseña, usuario, 0)
            contraseña = input("Ingrese su contraseña: ")
            while contraseña != usuario_contraseña[validar1][validar2 + 1]:
                print("Contraseña incorrecta")
                contraseña = input("Ingrese su contraseña: ")
            
            #JUEGO
            niveles = declarar_niveles()
            
if __name__ == "__main__":
    main()