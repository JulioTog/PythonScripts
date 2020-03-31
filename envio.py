from zipfile import ZipFile
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
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

#solicita nro de rm para generar el nombre del zip
file_name = 'RM' + input('Ingrese Nro de RedMine: ')+'.zip'

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#root = "C:\Users\jtognetti\Desktop\Defectos"
filename = askopenfilenames(title='Choose a file')
var = Tk().splitlist(filename)

#comprime todos los archivos seleccionados
print('se comprime')
with ZipFile(file_name,'w') as zip:
    for f in var:
        zip.write(f,basename(f))
