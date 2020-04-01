from zipfile import ZipFile
from tkinter import *
from tkinter import ttk
from os.path import basename

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
print('                                                                           V1.2')
print('\n')
print('\n')
#solicita nro de rm para generar el nombre del zip
file_name = 'RM' + input('Ingrese Nro de RedMine: ')+'.zip'

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

filename = filedialog.askopenfilenames(title='Archivos a zipear')
var = Tk().splitlist(filename)
#Selecciona destino del zipfile
destino = filedialog.askdirectory(title='Directorio destino del zip')
#concatena path destino con el nombre del archivo a zipear
destino = destino + '/' + file_name
#comprime todos los archivos seleccionados
print('se comprime')
with ZipFile(destino,'w') as zip:
    for f in var:
        zip.write(f,basename(f))
