import os 
import time

#lista de peliculas
peliculas = {
    1:'Spider-man: Lejos de casa',
}
    
precio_entrada = 2500

asientos = [[0] * 10 for _ in range(20)]

def mostrar_peliculas ():
    print('peliculas disponibles: ')
    for clave, pelicula in peliculas.items():
        print(f'{clave}. {pelicula}')
        opcion = input('seleccione una opcion: ')
        print('se ha seleccionad de manera exitosa👍')
        print('espere unos segundos...')
        time.sleep(3)
        os.system('cls')

def mostrar_asientos ():
    print('peliculas disponibles: ')
    for fila, asientos_fila in enumerate (asientos, start=1):
        for col, estado in enumerate(asientos_fila, start=1):
            if estado ==0:
                print(f'fila {fila}, asiento {col}: Disponible')

            else:
                print(f'fila {fila}, asiento {col}: Ocupado')
    time.sleep(5)
    os.system('cls')

def reservar_asiento (fila, columna):
    if asientos[fila-1][columna-1] == 0:
        asientos[fila-1][columna-1] = 1
        return True
    else:
        return False

def registro():
    print('Bienvenido')
    nombre = input('ingresa tu nombre: ')
    print('Es alumno de Duoc?')
    print('[1]')
    print('[2]')
    opcion_alumno = input('ingrese su respuesta: ')
    if opcion_alumno == 1:
        print('Bienvenido alumno')
    elif opcion_alumno == 2:
        print('Bienvenido Cliente')

def calcular_total_ingresos ():
    total = 0
    for fila in asientos:
        total += fila.count(1) * precio_entrada
        return total

while True:
    print('-----------Bienvenido al Cine----------')
    print('----[1] Mostrar lista de peliculas-----')
    print('----[2] Mostrar estado de los asientos-')
    print('----[3] Reservar un asiento------------')
    print('----[4] Calcular total de ingresos-----')
    print('----[5] Registro-----------------------')
    print('----[0] Salir--------------------------')
    opcion = input('Seleccione una opcion: ')
    if opcion == '1':
        mostrar_peliculas()
    elif opcion == '2':
        mostrar_asientos()
    elif opcion == '3':
        fila = int(input('Ingrese el numero de la fila: '))
        columna = int(input('Ingrese el numero de la columna: '))
        if reservar_asiento(fila, columna):
            print('Asiento reservado con exito!')
        else:
            print('El asiento ya esta ocupado')
    elif opcion == '4':
        total_ingresos = calcular_total_ingresos()
        print(f'total de ingresos: ${total_ingresos}')
    elif opcion == '5':
        registro()
    elif opcion == '0':
        break
    else:
        print('Opcion invalida, por favor seleccione nuevamente')

