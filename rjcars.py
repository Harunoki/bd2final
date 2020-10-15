from getpass import getpass

import mysql.connector
import os
import random
import sys


class Auto:
    def __init__(self, mar, mod, tip, ye, prec):
        self.marca = mar
        self.modelo = mod
        self.tipo = tip
        self.year = ye
        self.precio = prec


class Cliente:
    def __init__(self, ced, nom, ape, dirc, tel):
        self.cedula = ced
        self.nombre = nom
        self.apellido = ape
        self.direccion = dirc
        self.telefono = tel


class Empleado:
    def __init__(self, ced, nom, ape, car, dire, sal):
        self.cedula = ced
        self.nombre = nom
        self.apellido = ape
        self.cargo = car
        self.direccion = dire
        self.salario = sal


if __name__ == '__main__':
    run = 1
    titulo = '-Programa para administrar base de datos de RJ CARS-'
    print(titulo)
    hst = str(input('Ingrese el host (Por defecto:localhost): ') or 'localhost')
    usr = str(input('Ingrese el usuario (Por defecto:RJadmin): ') or 'RJadmin')
    pwd = str(getpass('Ingrese la contraseña: '))
    dbn = 'RJCARS'
    try:
        db = mysql.connector.connect(host=hst, user=usr, password=pwd, database=dbn)
    except NameError:
        sys.exit('No se pudo conectar a la base de datos. Cerrando...')
    sqlsh = db.cursor()


    def sqlcmd(cmd):
        sqlsh.execute(cmd)


    def printsql(com):
        res = sqlsh.execute(com, multi=True)
        for line in res:
            print(line)
            if line.with_rows:
                print(line.fetchall())


    autos = [Auto('Hyundai', 'Tucson', 'SUV', '2018', '51963.12'),
             Auto('Lada', 'Samara', 'Convertible', '1995', '20265.93'),
             Auto('Honda', 'Civic', 'Coupe', '2001', '33610.71'),
             Auto('Kia', 'Rio', 'Hatchback', '2017', '25488.66'),
             Auto('Toyota', 'Corolla', 'Sedan', '2007', '31137.54')]

    clientes = []
    empleados = []

    stc = 'SHOW TABLES;'

    while run == 1:
        vdtc = 'SELECT * FROM '
        ia = 'INSERT INTO AUTOS (MARCA, MODELO, TIPO, AÑO, PRECIO) VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');'
        ic = 'INSERT INTO CLIENTES (CEDULA, NOMBRE, APELLIDO, DIRECCION, TELEFONO) VALUES (\'{}\',\'{}\',\'{}\',' \
             '\'{}\',\'{}\'); '
        ie = 'INSERT INTO EMPLEADOS (CEDULA, NOMBRE, APELLIDO, CARGO, DIRECCION, SALARIO) VALUES (\'{}\',\'{}\',' \
             '\'{}\',\'{}\',\'{}\',\'{}\'); '
        it = 'INSERT INTO TRANSACCIONES (NoEMP, CedCLIENTE, VIN, VALOR) VALUES (\'{}\',\'{}\',\'{}\',\'{}\');'
        os.system('cls')
        print(titulo)
        try:
            if NoEMP:
                print(f'Numero de Empleado: {NoEMP}')
        except NameError:
            pass
        try:
            if CedCLIENTE:
                print(f'Cedula Cliente: {CedCLIENTE}')
        except NameError:
            pass
        print('''
        -MENU-
        1) Ver tablas
        2) Ver datos de tablas
        3) Agregar datos a la tabla
        4) Ingresar como Empleado
        5) Ingresar como Cliente
        6) Cerrar Sesion
        9) Usar sentencias SQL personalizadas
        0) Salir
            ''')
        sel = input('Seleccione: ')
        try:
            sel = int(sel)
        except NameError:
            input('Seleccione una opcion, presione una tecla para continuar...')
        os.system('cls')
        print(titulo)
        if sel is None or sel == '':
            input('Seleccione una opcion, presione una tecla para continuar...')
        elif sel == 0:
            print('Cerrando...')
            run = 0
        elif sel == 1:
            print('-Ver tablas-')
            print('Comando: ' + stc + '\nSalida:')
            try:
                printsql(stc)
            except NameError:
                print('No se pudo realizar la consulta')
            input('Presione una tecla para continuar...')
        elif sel == 2:
            print('-Ver datos de tablas-')
            print('''
        -MENU-
        1) Tabla AUTOS
        2) Tabla CLIENTES
        3) Tabla EMPLEADOS
        4) Tabla TRANSACCIONES
        5) Manual
                                    ''')
            sel = input('Seleccione: ')
            try:
                sel = int(sel)
            except NameError:
                input('Seleccione una opcion, presione una tecla para continuar...')
            os.system('cls')
            print(titulo)
            if sel == 1:
                print('Comando: ' + vdtc + 'AUTOS;' + '\nSalida:')
                try:
                    printsql(vdtc + 'AUTOS;')
                except NameError:
                    print('No se pudo mostrar la tabla')
            if sel == 2:
                print('Comando: ' + vdtc + 'CLIENTES;' + '\nSalida:')
                try:
                    printsql(vdtc + 'CLIENTES;')
                except NameError:
                    print('No se pudo mostrar la tabla')
            if sel == 3:
                print('Comando: ' + vdtc + 'EMPLEADOS;' + '\nSalida:')
                try:
                    printsql(vdtc + 'EMPLEADOS;')
                except NameError:
                    print('No se pudo mostrar la tabla')
            if sel == 4:
                print('Comando: ' + vdtc + 'TRANSACCIONES;' + '\nSalida:')
                try:
                    printsql(vdtc + 'TRANSACCIONES;')
                except NameError:
                    print('No se pudo mostrar la tabla')
            if sel == 5:
                try:
                    printsql(stc)
                except NameError:
                    print('No se pudo realizar la consulta')
                tn = input('Ingrese el nombre de la tabla: ')
                print('Comando: ' + vdtc + tn + ";" + '\nSalida:')
                try:
                    printsql(vdtc + tn + ";")
                except NameError:
                    print('No se pudo mostrar la tabla')
            input('Presione una tecla para continuar...')
        elif sel == 3:
            print('-Agregar datos a la tabla-')
            print('''
        -MENU-
        1) Agregar datos a la tabla AUTOS
        2) Agregar datos a la tabla CLIENTES
        3) Agregar datos a la tabla EMPLEADOS
        4) Crear una transaccion
                        ''')
            sel = input('Seleccione: ')
            try:
                sel = int(sel)
            except NameError:
                input('Seleccione una opcion, presione una tecla para continuar...')
            os.system('cls')
            print(titulo)
            if sel == 1:
                print('-Agregar datos a la tabla AUTOS-')
                print('''
        -MENU-
        1) Automatizado
        2) Manual
                                        ''')
                sel = input('Seleccione: ')
                try:
                    sel = int(sel)
                except NameError:
                    input('Seleccione una opcion, presione una tecla para continuar...')
                os.system('cls')
                print(titulo)
                if sel == 1:
                    print('-Agregar datos a la tabla AUTOS-')
                    rn = random.randint(0, 4)
                    marca = autos[rn].marca
                    modelo = autos[rn].modelo
                    tipo = autos[rn].tipo
                    year = autos[rn].year
                    precio = autos[rn].precio
                    ia = ia.format(marca, modelo, tipo, year, precio)
                    print('Comando: ' + ia)
                    try:
                        sqlcmd(ia)
                        db.commit()
                    except NameError:
                        print('No se pudo agregar los datos a la tabla AUTOS')
                    else:
                        print('Se agrego los datos a la tabla AUTOS correctamente')
                if sel == 2:
                    print('-Agregar datos a la tabla AUTOS-')
                    print('A continuacion ingrese la informacion del auto:')
                    marca = input('Ingrese la marca: ')
                    modelo = input('Ingrese el modelo: ')
                    tipo = input('Ingrese el tipo: ')
                    year = input('Ingrese el año: ')
                    precio = input('Ingrese el precio: ')
                    ia = ia.format(marca, modelo, tipo, year, precio)
                    print('Comando: ' + ia)
                    try:
                        sqlcmd(ia)
                        db.commit()
                    except NameError:
                        print('No se pudo agregar los datos a la tabla AUTOS')
                    else:
                        print('Se agrego los datos a la tabla AUTOS correctamente')
            if sel == 2:
                print('-Agregar datos a la tabla CLIENTES-')
                print('''
        -MENU-
        1) Automatizado
        2) Manual
                                            ''')
                sel = input('Seleccione: ')
                try:
                    sel = int(sel)
                except NameError:
                    input('Seleccione una opcion, presione una tecla para continuar...')
                os.system('cls')
                print(titulo)
                if sel == 1:
                    print('-Agregar datos a la tabla CLIENTES-')
                    rn = random.randint(0, 4)
                    cedula = clientes[rn].cedula
                    nombre = clientes[rn].nombre
                    apellido = clientes[rn].apellido
                    direccion = clientes[rn].direccion
                    telefono = clientes[rn].telefono
                    ic = ic.format(cedula, nombre, apellido, direccion, telefono)
                    print('Comando: ' + ic)
                    try:
                        sqlcmd(ic)
                        db.commit()
                    except NameError:
                        print('No se pudo agregar los datos a la tabla CLIENTES')
                    else:
                        print('Se agrego los datos a la tabla CLIENTES correctamente')
                if sel == 2:
                    print('-Agregar datos a la tabla CLIENTES-')
                    print('A continuacion ingrese la informacion del cliente:')
                    cedula = input('Ingrese la cedula: ')
                    nombre = input('Ingrese el nombre: ')
                    apellido = input('Ingrese el apellido: ')
                    direccion = input('Ingrese la direccion: ')
                    telefono = input('Ingrese el telefono: ')
                    ic = ic.format(cedula, nombre, apellido, direccion, telefono)
                    print('Comando: ' + ic)
                    try:
                        sqlcmd(ic)
                        db.commit()
                    except NameError:
                        print('No se pudo agregar los datos a la tabla CLIENTES')
                    else:
                        print('Se agrego los datos a la tabla CLIENTES correctamente')
            if sel == 3:
                print('-Agregar datos a la tabla EMPLEADOS-')
                print('''
        -MENU-
        1) Automatizado
        2) Manual
                                                            ''')
                sel = input('Seleccione: ')
                try:
                    sel = int(sel)
                except NameError:
                    input('Seleccione una opcion, presione una tecla para continuar...')
                os.system('cls')
                print(titulo)
                if sel == 1:
                    print('-Agregar datos a la tabla EMPLEADOS-')
                    rn = random.randint(0, 4)
                    cedula = empleados[rn].cedula
                    nombre = empleados[rn].nombre
                    apellido = empleados[rn].apellido
                    cargo = empleados[rn].cargo
                    direccion = empleados[rn].direccion
                    salario = empleados[rn].salario
                    ie = ie.format(cedula, nombre, apellido, cargo, direccion, salario)
                    print('Comando: ' + ie)
                    try:
                        sqlcmd(ie)
                        db.commit()
                    except NameError:
                        print('No se pudo agregar los datos a la tabla EMPLEADOS')
                    else:
                        print('Se agrego los datos a la tabla EMPLEADOS correctamente')
                if sel == 2:
                    print('-Agregar datos a la tabla EMPLEADOS-')
                    print('A continuacion ingrese la informacion del empleado:')
                    cedula = input('Ingrese la cedula: ')
                    nombre = input('Ingrese el nombre: ')
                    apellido = input('Ingrese el apellido: ')
                    cargo = input('Ingrese el cargo: ')
                    direccion = input('Ingrese la direccion: ')
                    salario = input('Ingrese el salario: ')
                    ie = ie.format(cedula, nombre, apellido, cargo, direccion, salario)
                    print('Comando: ' + ie)
                    try:
                        sqlcmd(ie)
                        db.commit()
                    except NameError:
                        print('No se pudo agregar los datos a la tabla EMPLEADOS')
                    else:
                        print('Se agrego los datos a la tabla EMPLEADOS correctamente')
            if sel == 4:
                print('-Crear una transaccion-')
                print('A continuacion ingrese la informacion de la transaccion:')
                try:
                    if NoEMP:
                        pass
                except NameError:
                    try:
                        printsql(vdtc + 'EMPLEADOS' + ";")
                    except NameError:
                        print('No se pudo mostrar la tabla EMPLEADOS')
                    NoEMP = input('Ingrese el No. de Empleado: ')
                else:
                    if NoEMP is None or NoEMP == '':
                        try:
                            printsql(vdtc + 'EMPLEADOS' + ";")
                        except NameError:
                            print('No se pudo mostrar la tabla EMPLEADOS')
                        NoEMP = input('Ingrese el No. de Empleado: ')
                try:
                    if CedCLIENTE:
                        pass
                except NameError:
                    try:
                        printsql(vdtc + 'CLIENTES' + ";")
                    except NameError:
                        print('No se pudo mostrar la tabla CLIENTES')
                    CedCLIENTE = input('Ingrese la cedula del cliente: ')
                else:
                    if CedCLIENTE is None or CedCLIENTE == '':
                        try:
                            printsql(vdtc + 'CLIENTES' + ";")
                        except NameError:
                            print('No se pudo mostrar la tabla CLIENTES')
                        CedCLIENTE = input('Ingrese la cedula del cliente: ')
                try:
                    printsql(vdtc + 'AUTOS' + ";")
                except NameError:
                    print('No se pudo mostrar la tabla AUTOS')
                VIN = input('Ingrese el numero VIN del auto: ')
                try:
                    precmd = f'SELECT PRECIO FROM AUTOS WHERE VIN=\'{VIN}\';'
                    sqlsh.execute(precmd)
                    for (pre) in sqlsh:
                        VALOR = ('{}'.format(pre[0]))
                        VALOR = float(VALOR) * 1.07
                except NameError:
                    print("No se pudo recuperar el precio del auto")
                it = it.format(NoEMP, CedCLIENTE, VIN, VALOR)
                print('Comando: ' + it)
                try:
                    sqlcmd(it)
                    db.commit()
                except NameError:
                    print('No se pudo realizar la transaccion')
                else:
                    print('Transaccion realizada correctamente')
            input('Presione una tecla para continuar...')
        elif sel == 4:
            try:
                if NoEMP and NoEMP != '':
                    print("Ya inicio sesion")
            except NameError:
                try:
                    printsql(vdtc + 'EMPLEADOS' + ";")
                except NameError:
                    print('No se pudo mostrar la tabla EMPLEADOS')
                NoEMP = input('Ingrese el No. de Empleado: ')
            else:
                if NoEMP is None or NoEMP == '':
                    try:
                        printsql(vdtc + 'EMPLEADOS' + ";")
                    except NameError:
                        print('No se pudo mostrar la tabla EMPLEADOS')
                    NoEMP = input('Ingrese el No. de Empleado: ')
            input('Presione una tecla para continuar...')
        elif sel == 5:
            try:
                if CedCLIENTE and NoEMP != '':
                    print("Ya inicio sesion")
            except NameError:
                try:
                    printsql(vdtc + 'CLIENTES' + ";")
                except NameError:
                    print('No se pudo mostrar la tabla CLIENTES')
                CedCLIENTE = input('Ingrese la cedula del cliente: ')
            else:
                if CedCLIENTE is None or CedCLIENTE == '':
                    try:
                        printsql(vdtc + 'CLIENTES' + ";")
                    except NameError:
                        print('No se pudo mostrar la tabla CLIENTES')
                    CedCLIENTE = input('Ingrese la cedula del cliente: ')
            input('Presione una tecla para continuar...')
        elif sel == 6:
            NoEMP = None
            CedCLIENTE = None
            input('Sesion Cerrada, presione una tecla para continuar...')
        elif sel == 9:
            print('-Usar sentencias SQL personalizadas-')
            sqlc = input('Ingrese el comando que desea realizar: ')
            print('-Ver tablas-\nComando: ' + sqlc + '\nSalida:')
            try:
                printsql(sqlc)
                db.commit()
            except NameError:
                print('No se pudo realizar el comando')
            input('Presione una tecla para continuar...')
    sqlsh.close()
    db.close()
    sys.exit()
