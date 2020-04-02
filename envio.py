from zipfile import ZipFile
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory,askopenfilenames
from os import remove
from os.path import basename
from datetime import date

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
print('                                                                           V1.3')
print('\n')
print('\n')
#solicita nro de rm para generar el nombre del zip
file_name2 = 'RM' + input('Ingrese Nro de RedMine: ')
file_name = file_name2 +'.zip'

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

filename = askopenfilenames(title='Archivos a zipear')
destino = askdirectory(title='Directorio destino del zip')
var = Tk().splitlist(filename)
#Selecciona destino del zipfile


#concatena path destino con el nombre del archivo a zipear
file_name = destino + '/' + file_name
file_name2 = destino + '/' + file_name2
#comprime todos los archivos seleccionados
print('se comprime')
with ZipFile(file_name,'w') as zip:
    lista = ''
    for f in var:
        zip.write(f,basename(f))
        lista += basename(f) +'\n' #Carga lista de objetos
    zip.close()
#genera path para txt
readme = destino + '/Release.txt'
descripcion = input('Ingrese descripcion del envio: ')
data = 'Fecha: '+ str(date.today())+'\n'+'Descripcion: ' +descripcion+'\n''Objetos:\n'
#abre archivo y escribe
with open(readme,'w') as txt:
    txt.write(data+lista)
    txt.close()

with ZipFile(file_name2+'-Env.zip','w') as Env:
    Env.write(file_name,basename(file_name))
    Env.write(readme,basename(readme))
    Env.close()

remove(readme)
remove(file_name)
