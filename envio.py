from zipfile import ZipFile
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from os.path import basename


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
root ='C:\Users\jtognetti\Desktop\Defectos'
filename = askopenfilenames(parent=root,title='Choose a file')
var = Tk().splitlist(filename)


#solicita nro de rm para generar el nombre del zip
print('Ingrese Nro de RedMine')
file_name = 'RM' + input()+'.zip'

#comprime todos los archivos seleccionados
print('se comprime')
with ZipFile(file_name,'w') as zip:
    for f in var:
        zip.write(f,basename(f))
