import random #Libreria para selección computadora de (1) Piedra, (2) Papel, (3) Tijera

def resultado(A,B): # creamos la subrutina que determina el resultado
    #Creamos la estructura condicional, junto con una opción si alguien mete mal el dedo
    if A == B:
        print("Resultado: EMPATE")

    elif A == 1 and B == 2:
        print("Resultado: GANA COMPUTADORA")

    elif A == 2 and B == 3:
        print("Resultado: GANA COMPUTADORA")

    elif A == 3 and B == 1:
        print("Resultado: GANA COMPUTADORA")

    elif A == 1 and B == 3:
        print("Resultado: GANA USUARIO")

    elif A == 2 and B == 1:
        print("Resultado: GANA USUARIO")

    elif A == 3 and B == 2:
        print("Resultado: GANA USUARIO")

    else:
        print("Opción inválida")

def main():

    while True: # bucle para repetir el juego
    
        print("PIEDRA, PAPEL O TIJERA") #Mostramos mensaje para que usuario sepa que hacer
        print("Seleccione una opción:")
        print("1 = Piedra")
        print("2 = Papel")
        print("3 = Tijera")
    
    
        while True:
            try:
                A = int(input("Ingrese su opción (1-3): ")) #Solicito ingresar la selección de usuario
                if A in [1, 2, 3]: #Uso de lista
                    break # selección correcta
                else:
                    print ("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Debe ingresar un número válido.")
                
        B = random.randint(1, 3) #Proceso interno de computador de selección de opción
        print("\nComputadora eligió:", B)    
        resultado(A, B)
        
        #Introducimos la opción de preguntar si quiere volver a jugar
        
        repetir = input("¿Desea volver a jugar? (s/n): ").lower() #registramos las opciones de s o n y si las escribe en mayusculas el usuario, las vuelve minusculas
    
        if repetir != "s":
            print("Gracias por jugar.")
            break  # Sale del bucle principal
        
                
if __name__ == "__main__": # cuando el archivo se ejecuta directamente. Si se importa desde otro archivo, no ejecuta main().
    main()