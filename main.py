import envio
import os


while True:
    os.system('cls')
    print('\n')
    print(' ▄▄▄██▀▀▀▄▄▄█████▓     ██████  ▄████▄   ██▀███   ██▓ ██▓███  ▄▄▄█████▓  ██████')
    print('   ▒██   ▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▓██▒▓██░  ██▒▓  ██▒ ▓▒▒██    ▒ ')
    print('   ░██   ▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒ ▓██░ ▒░░ ▓██▄   ')
    print('▓██▄██▓  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░ ▓██▓ ░   ▒   ██▒')
    print(' ▓███▒     ▒██▒ ░    ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒░██░▒██▒ ░  ░  ▒██▒ ░ ▒██████▒▒')
    print(' ▒▓▒▒░     ▒ ░░      ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░  ▒ ░░   ▒ ▒▓▒ ▒ ░')
    print(' ▒ ░▒░       ░       ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░ ▒ ░░▒ ░         ░    ░ ░▒  ░ ░')
    print(' ░ ░ ░     ░         ░  ░  ░  ░          ░░   ░  ▒ ░░░         ░      ░  ░  ░  ')
    print(' ░   ░                     ░  ░ ░         ░      ░                          ░  ')
    print('                              ░                                                ')
    print('                                                                           V1.4')
    print('\n')
    print('\n')


    print('1.- Realizar envio a formosa')
    print('\n')
    print('\n')

    opcion = int(input('seleccione una opcion... \n'))

    if opcion == 1:
        envio.envio()
    elif opcion == 5:
        break
    else:
        print('Esa opcion no es valida')
