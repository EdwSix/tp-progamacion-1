import random
def declarar_niveles():
    niveles = {
        1: [("L", "U", "N", "A"), ("P", "A", "N"), ("S", "O", "L")],
        2: [("C", "A", "S", "A"), ("M", "E", "S", "A"), ("G", "A", "T", "O")],
        3: [("S", "I", "L", "L", "A"), ("L", "A", "G", "O"), ("T", "I", "Z", "A")],
        4: [("P", "E", "R", "R", "O"), ("A", "V", "I", "O", "N"), ("F", "R", "U", "T", "A")],
        5: [("A", "V", "I", "O", "N", "E", "T", "A"), ("P", "A", "L", "M", "E", "R", "A"), ("S", "E", "R", "P", "I", "E", "N", "T", "E")],
        6: [("E", "L", "E", "F", "A", "N", "T", "E"), ("C", "A", "M", "I", "O", "N"), ("M", "A", "M", "N", "T", "E", "Q", "U", "I", "L", "L", "A")],
        7: [("M", "U", "R", "C", "I", "E", "L", "A", "G", "O"), ("S", "E", "M", "A", "F", "O", "R", "O"), ("C", "O", "C", "O", "D", "R", "I", "L", "O")],
        8: [("M", "A", "R", "I", "P", "O", "S", "A"), ("H", "I", "P", "O", "P", "O", "T", "A", "M", "O"), ("C", "A", "L", "E", "N", "D", "A", "R", "I", "O")],
        9: [("C", "A", "R", "R", "E", "T", "I", "L", "L", "A"), ("A", "R", "Q", "U", "I", "T", "E", "C", "T", "U", "R", "A"), ("E", "L", "E", "C", "T", "R", "I", "C", "I", "D", "A", "D")],
        10: [("M", "I", "C", "R", "O", "B", "I", "O", "L", "O", "G", "I", "A"), ("C", "I", "M", "N", "E", "M", "A", "T", "O", "G", "R", "A", "F", "I", "A"), ("D", "E", "S", "E", "M", "B", "A", "R", "C", "A", "R")]
    }
    return niveles

def mostrar_errores():
    muñeco = {
        0: """
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
         =========
         """,
        1: """
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
         =========
         """,
        2: """
          +---+
          |   |
          O   |
         /|\  |
              |
              |
         =========
         """,
        3: """
          +---+
          |   |
          O   |
         /|   |
              |
              |
         =========
         """,
        4: """
          +---+
          |   |
          O   |
          |   |
              |
              |
         =========
         """,
        5: """
          +---+
          |   |
          O   |
              |
              |
              |
         =========
         """,
        6: """
          +---+
          |   |
              |
              |
              |
              |
         =========
         """
    }
    return muñeco

def aleatorio():
    numero = random.randint(0, 2)
    return numero
def busqueda(matriz, valor, X):
    posl = -1
    for i in range(len(matriz)):
        if matriz[i][X] == valor:
            posl = i
    return posl

def busqueda2(lista1, lista2, valor):
    pos = -1
    for i in range(len(lista1)):
        if lista1[i] == valor and lista2[i] != valor:
            lista2[i] = valor
            pos = i
    if pos == -1:
        for i in range(len(lista2)):
            if lista2[i] == valor:
                pos = -2
    return pos

def caracteres(valor, X):
    while len(valor) != X:
        print("Ingrese el numero de digitos correctos")
        valor = input()
    return valor

def fuera_de_rango(valor, X):
    while valor < 1 or valor > X:
        print("Elija correctamente la opcion")
        valor = int(input())
    return valor
    
def main():
    usuario_contraseña = []
    parar = False
    while parar == False:
        lista = []
        if len(usuario_contraseña) == 0:
            print("¡BIENVENIDO!")
            print()
            print("PRESIONE 1 PARA REGISTRARSE")
            opcion = int(input())
            opcion = fuera_de_rango(opcion, 1)
        else:
            print("¡BIENVENIDO!")
            print("1 - Registrarse")
            print("2 - Iniciar sesion")
            print("3 - SALIR")
            opcion = int(input())
            opcion = fuera_de_rango(opcion, 3)
            
        #REGISTRO DE USUARIO
        if opcion == 1:
            print("-----REGISTRO DE USUARIO-----")
            usuario = input("Ingrese un nombre de usuario: ")
            #usuario = caracteres(usuario, 10)
            validar = busqueda(usuario_contraseña, usuario, 0)
            while validar != -1:
                print("Usuario ya existente")
                usuario = input("Ingrese un nombre de usuario: ")
                #usuario = caracteres(usuario, 10)
                validar = busqueda(usuario_contraseña, usuario, 0)
            contraseña = input("Ingrese una contraseña: ")
            #contraseña = caracteres(contraseña, 8)
            
            nivel = 1
            lista.append(usuario)
            lista.append(contraseña)
            lista.append(nivel)
            usuario_contraseña.append(lista)
            #[USUARIO , CONTRASEÑA, NIVEL]
            #   0           1        2 
        
        #INICIO DE SESION
        elif opcion == 2:
            print("-----INICIO SESION-----")
            usuario = input("Ingrese su nombre de usuario: ")
            validar = busqueda(usuario_contraseña, usuario, 0)
            while validar == -1:
                print("Usuario no existente")
                usuario = input("Ingrese un nombre de usuario: ")
                validar = busqueda(usuario_contraseña, usuario, 0)
            contraseña = input("Ingrese su contraseña: ")
            while contraseña != usuario_contraseña[validar][1]:
                print("Contraseña incorrecta")
                contraseña = input("Ingrese su contraseña: ")
                
            #JUEGO
            niveles = declarar_niveles()
            ahorcado = mostrar_errores()    
            jugar = True
        
            while jugar == True:
                nivel_actual = usuario_contraseña[validar][2]
                palabras = niveles[nivel_actual]
                palabra_actual = list(palabras[aleatorio()])
                guion_bajo = [" _ "] * len(palabra_actual)
                print("NIVEL:", usuario_contraseña[validar][2])
                intentos = 6
                partida = True
                ganado = False
                while partida == True:
                    print()
                    print("TE QUEDAN:", intentos," INTENTOS")
                    print(ahorcado[intentos])
                    for i in range(len(guion_bajo)):
                        print(guion_bajo[i], end="")
                    print()
                    letra = input("INGRESE POR TECLADO UNA LETRA: ")
                    existe = busqueda2(palabra_actual, guion_bajo, letra)
                    if existe == -1:
                        print("LA LETRA NO SE ENCUENTRA EN LA PALABRA")
                        intentos = intentos - 1
                    elif existe == -2:
                        print("LETRA REPETIDA")
                        intentos = intentos - 1
                    else:
                        print("¡CORRECTO!")
                    
                    if intentos == 0:
                        partida = False
                        print()
                        print("PERDISTE")
                        print("NO TE QUEDAN MAS INTENTOS")
                        print(ahorcado[intentos])
                        print("LA PALABRA ERA: ")
                        for i in range(len(palabra_actual)):
                            print(palabra_actual[i], end="")
                    
                    if palabra_actual == guion_bajo:
                        partida = False
                        ganado = True
                        
                if ganado == False:
                    print()
                    print("¿INTENTAR OTRA VEZ O SALIR?")
                    print("1 - INTENTAR OTRA VEZ")
                    print("2 - SALIR")
                    opcion = int(input())
                    opcion = fuera_de_rango(opcion, 2)
                    if opcion == 2:
                        jugar = False
                        
                if ganado == True:
                    print()
                    print("¡¡¡GANASTE!!!")
                    print("LA PALABRA ERA: ")
                    for i in range(len(palabra_actual)):
                        print(palabra_actual[i], end="")
                    usuario_contraseña[validar][2] = usuario_contraseña[validar][2] + 1
                    if usuario_contraseña[validar][2] != 11:    
                        print()
                        print("¿SIGUIENTE NIVEL O SALIR?")
                        print("1 - SIGUIENTE NIVEL")
                        print("2 - SALIR")
                        opcion = int(input())
                        opcion = fuera_de_rango(opcion, 2)
                        if opcion == 2:
                            jugar = False
                    else:
                        print("¡¡¡FELICITACIONES HAZ COMPLETADO TODOS LOS NIVELES!!!")
                        print("SE TE DEVOLVERA AL NIVEL 1 PARA QUE PUEDAS JUGAR OTRA VEZ")
                        usuario_contraseña[validar][2] = 1
                        print("1 - SEGUIR JUGANDO DESDE EL NIVEL 1")
                        print("2 - SALIR")
                        opcion = int(input())
                        opcion = fuera_de_rango(opcion, 2)
                        if opcion == 2:
                            jugar = False
        
        else:
            print("FIN DEL JUEGO")
            parar = True
            jugar = False
                        
if __name__ == "__main__":
    main()