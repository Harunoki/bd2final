import mysql.connector, os, sys
from getpass import getpass

if __name__ == '__main__':
    run=1
    titulo='Conectar a una base de datos MySQL'
    print(titulo)
    hst = str(input('Ingrese el host (Por defecto:localhost): ') or 'localhost')
    usr = str(input('Ingrese el usuario: '))
    pwd = str(getpass('Ingrese la contraseña: '))
    try:
        db = mysql.connector.connect(host=hst, user=usr, password=pwd)
    except:
        sys.exit('No se pudo conectar a la base de datos. Cerrando...')
    sqlsh = db.cursor()


    def sqlcmd(cmd):
        sqlsh.execute(cmd)


    def printsql(com):
        sqlcmd(com)
        for lines in sqlsh:
            print(lines)


    sdbc = 'SHOW DATABASES;'
    stc = 'SHOW TABLES;'

    while run == 1:
        udbc = 'USE '
        sel = None
        os.system('cls')
        print(titulo)
        print('''
        -MENU-
        1) Ver base de datos
        2) Usar base de datos
        3) Ver tablas
        9) Usar sentencias SQL personalizadas
        0) Salir
        ''')
        sel = int(input('Seleccione: '))
        os.system('cls')
        print(titulo)
        if sel == None:
            input('Seleccione una opcion, presione una tecla para continuar...')
        elif sel == 0:
            print('Cerrando...')
            run = 0
        elif sel == 1:
            printsql(sdbc)
            input('Presione una tecla para continuar...')
        elif sel == 2:
            print('-Usar base de datos-')
            printsql(sdbc)
            dbn = input('Ingrese el nombre de la base de datos: ')
            udbc = udbc + dbn + ";"
            print('Comando: ' + udbc)
            try:
                sqlcmd(sdbc)
                db = mysql.connector.connect(host=hst, user=usr, password=pwd,database=dbn)
                sqlsh = db.cursor()
            except:
                print('No se pudo seleccionar la base de datos')
                seldb = 0
            else:
                seldb = 1
            input('Presione una tecla para continuar...')
        elif sel == 3:
            print('-Ver tablas-')
            if seldb == 1:
                print('Comando: ' + stc + '\nSalida:')
                try:
                    printsql(stc)
                except:
                    print('No se pudo realizar la consulta')
            else:
                print('No se ha seleccionado la base de datos')
            input('Presione una tecla para continuar...')
        elif sel == 9:
            print('-Usar sentencias SQL personalizadas-')
            sqlc = input('Ingrese el comando que desea realizar: ')
            print('-Ver tablas-\nComando: ' + sqlc + '\nSalida:')
            try:
                printsql(sqlc)
            except:
                print('No se pudo realizar el comando')
            input('Presione una tecla para continuar...')
    db.close()
    sys.exit()