from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont
from pytube import YouTube
from moviepy.editor import *
import easygui, getpass, os, shutil

userselection = 0
sel = 0
user = getpass.getuser()

#Función para validar si el usuario ha seleccionado una opción
def selected():
    global sel
    if sel == 0:
        sel = 1
        btn.pack()
    else:
        return 0

#Función para crear el archivo de audio que pidió el usuario
def downloadAudio(link_var):
    #Tomando el directorio del usuario
    dirname = filedialog.askdirectory(initialdir='C:/Users/%s/Music' % user)
    #Llamamos el modulo de Youtube de pytube3
    yt = YouTube(str(link_var))
    #Tomamos el título del documento
    title = str(yt.title)
    #Descargamo al directorio que especificó el usuario
    t = yt.streams[0].download(dirname)
    
    #Convertimos el Video a un archivo de audio (pytube3 no lo hace)
    video = VideoFileClip(os.path.join(dirname, title + ".mp4"))
    #Creamos la variable del nombre con la extensión del audio en wav (para el soporte de todos los dispositivos)
    name = title + "(AUDIO)" + ".wav"
    #Convertirmos el archivo a audio
    video.audio.write_audiofile(str(name), fps=44100, nbytes=2, buffersize=2000, codec='pcm_s16le', bitrate='3000k',ffmpeg_params=None, write_logfile=False, verbose=True, logger='bar')
    #Borramos el video descargado desde el directorio
    #removeVideo = dirname + "/" + title + ".mp4"
    #os.remove(removeVideo)
    #Movemos el archivo de musica directo a la carpeta que el usuario seleccionó
    localFilePath = os.path.dirname(os.path.realpath(__file__))
    print(str(localFilePath))
    #shutil.move(str(localFilePath), str(dirname))

#Función para descargar video
def downloadVideo(var_link):
    #Tomando el directorio del usuario
    dirname = filedialog.askdirectory(initialdir='C:/Users/%s/Music' % user)
    #Convertimos el video directo
    yt = YouTube(str(var_link)).streams[0].download(dirname)
  
#Función para el botón de descarga
def download():
    #Hacemos global la variable link del Entry
    global link
    #Tomamos el valor que viene en el Entry
    strlink = link.get()
    #Tomamos el valor que tomó el usuario en los RadioButtons
    selection = var.get()
    #Comparamos la selección del usuario
    if selection == 0:
        #Llamamos a la función de descargar Video
        downloadVideo(str(strlink))
        #Le decimos al usuario que su conversión a sido correcta
        lblSuccess.pack()
    else:
        #Llamamos a la función de descargar Audio
        downloadAudio(str(strlink))
        #Le decimos al usuario que su conversión a sido correcta
        lblSuccess.pack()

#Ventana
root = Tk()
#Tamaño de la ventana
root.geometry('430x300')
#Tipografía
fontStyle = tkFont.Font(family="Lucida Grande", size=16)

lblTitle = Label(root, text = 'Youtube Converter', font=fontStyle, bg="red")
lblTitle.pack()

lblLink = Label(root, text = 'Link: ', font=fontStyle)  
lblLink.pack()

link = Entry(root, font=fontStyle)
link.pack(side = TOP)


var = IntVar()
var.set(0)
radio1 = Radiobutton(root, text = 'Solo Audio', variable = var, value = 1, command = selected, font=fontStyle)
radio1.pack()

radio2 = Radiobutton(root, text = 'Video y Audio', variable = var, value = 2, command = selected, font=fontStyle)
radio2.pack()

btn = Button(root, text = 'Convertir', command = download, font=fontStyle)

lblSuccess = Label(root, text = 'Convertido Correctamente', bg="green", font=fontStyle)



root.mainloop()