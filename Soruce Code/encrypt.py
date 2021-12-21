from tkinter import *
import tkxui

__author__ = 'PKZOID/PKGAMER/ATIFSIDDIQUE'
__copyright__ = 'Copyright (C) 2020, PKZOID'
__credits__ = ['PKZOID']
__license__ = 'The MIT License (MIT)'
__version__ = '1.0'
__maintainer__ = 'PKZOID'
__email__ = 'Snipergamerpk@gmail.com'
__status__ = 'Beta'

_AppName_ = 'Text Encrypt'

root = tkxui.Tk(display=tkxui.FRAMELESS)
root.geometry('450x350')
root.center()
root.config_border(
        {
            'border': {
                'bg': "black"
            },
            'maximize': {
                'fg': 'white',
                'hoverfg': 'white',
                'hoverbg': '#14E8C4',
                'bg': 'black'
            },
            'minimize': {
                'fg': 'white',
                'hoverfg': 'white',
                'hoverbg': '#14E8C4',
                'bg': 'black'
            },
            'close': {
                'hoverbg': '#14E8C4',
                'hoverfg': 'white',
                'fg': 'white',
                'bg': 'black'
            }
        }
    )
def ecnrypt():
    name = name_entry.get()
    name_entry.delete(0,END)
    name_entry.insert(INSERT,name[::-1])
def Decrypt():
    name = name_entry.get()
    name_entry.delete(0,END)
    name_entry.insert(INSERT,name[::-1])    

def selectblack():
    #colour change
    background.configure(bg='black',activebackgroun='black')
    encrypt_button.configure(bg='black',activebackgroun='black')
    decrypt_button.configure(bg='black',activebackgroun='black')
    entry_image.configure(bg='black',activebackgroun='black')
    blue_button.configure(bg='black',activebackgroun='black')
    black_button.configure(bg='black',activebackgroun='black')
    orange_button.configure(bg='black',activebackgroun='black')
    pink_button.configure(bg='black',activebackgroun='black')
    glassgreen_button.configure(bg='black',activebackgroun='black')

    #select colour
    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='select black.png')
def selectorange():
    #colour change
    background.configure(bg='#FFA500',activebackgroun='#FFA500')
    encrypt_button.configure(bg='#FFA500',activebackgroun='#FFA500')
    decrypt_button.configure(bg='#FFA500',activebackgroun='#FFA500')
    entry_image.configure(bg='#FFA500',activebackgroun='#FFA500')
    blue_button.configure(bg='#FFA500',activebackgroun='#FFA500')
    black_button.configure(bg='#FFA500',activebackgroun='#FFA500')
    orange_button.configure(bg='#FFA500',activebackgroun='#FFA500')
    pink_button.configure(bg='#FFA500',activebackgroun='#FFA500')
    glassgreen_button.configure(bg='#FFA500',activebackgroun='#FFA500')

    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='blue.png')
    black_photo.configure(file='Black.png')
    orange_photo.configure(file='select orange.png')
def selectblue():
    #colour change
    background.configure(bg='#0096FF',activebackgroun='#0096FF')
    encrypt_button.configure(bg='#0096FF',activebackgroun='#0096FF')
    decrypt_button.configure(bg='#0096FF',activebackgroun='#0096FF')
    entry_image.configure(bg='#0096FF',activebackgroun='#0096FF')
    blue_button.configure(bg='#0096FF',activebackgroun='#0096FF')
    black_button.configure(bg='#0096FF',activebackgroun='#0096FF')
    orange_button.configure(bg='#0096FF',activebackgroun='#0096FF')
    pink_button.configure(bg='#0096FF',activebackgroun='#0096FF')
    glassgreen_button.configure(bg='#0096FF',activebackgroun='#0096FF')

    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='select blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='Black.png')
    
def selectpink():
    #colour change
    background.configure(bg='pink',activebackgroun='pink')
    encrypt_button.configure(bg='pink',activebackgroun='pink')
    decrypt_button.configure(bg='pink',activebackgroun='pink')
    entry_image.configure(bg='pink',activebackgroun='pink')
    blue_button.configure(bg='pink',activebackgroun='pink')
    black_button.configure(bg='pink',activebackgroun='pink')
    orange_button.configure(bg='pink',activebackgroun='pink')
    pink_button.configure(bg='pink',activebackgroun='pink')
    glassgreen_button.configure(bg='pink',activebackgroun='pink')

    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='select pink.png')
    blue_photo.configure(file='blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='Black.png')
def selectgreen():
    #colour change
    background.configure(bg='#36c9bb',activebackgroun='#36c9bb')
    encrypt_button.configure(bg='#36c9bb',activebackgroun='#36c9bb')
    decrypt_button.configure(bg='#36c9bb',activebackgroun='#36c9bb')
    entry_image.configure(bg='#36c9bb',activebackgroun='#36c9bb')
    blue_button.configure(bg='#36c9bb',activebackgroun='#36c9bb')
    black_button.configure(bg='#36c9bb',activebackgroun='#36c9bb')
    orange_button.configure(bg='#36c9bb',activebackgroun='#36c9bb')
    pink_button.configure(bg='#36c9bb',activebackgroun='#36c9bb')
    glassgreen_button.configure(bg='#36c9bb',activebackgroun='#36c9bb')

    glassgreen_photo.configure(file='select green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='Black.png')
#background
background = Label(root,border=0,width=80,height=50)
background.place(x=0,y=35)
#title 
title = Label(root,text="Text Encrypt",bg='black',border=0,font=('bold',14),foreground='white')
title.place(x=5,y=8)

#Encryptt Button
encrypt_photo = PhotoImage(file='Encrypt button.png')
encrypt_button = Button(root,border=0,image=encrypt_photo,command=ecnrypt)
encrypt_button.place(x=170,y=90)

#Decrypt Button
decrypt_photo = PhotoImage(file='Decrypt.png')
decrypt_button = Button(root,border=0,image=decrypt_photo,command=Decrypt)
decrypt_button.place(x=170,y=210)

#entry
entry_name = PhotoImage(file='Rectangle 1.png')
entry_image = Label(root,image=entry_name,border=0)
entry_image.place(x=110,y=160)

name_entry = Entry(root,width=27,border=0,font=('bold',11))
name_entry.place(x=120,y=163)

black_photo = PhotoImage(file='Black.png')
black_button = Button(root,border=0,image=black_photo,command=selectblack)
black_button.place(x=135,y=280)

#blue colour
blue_photo = PhotoImage(file='blue.png')
blue_button = Button(root,border=0,image=blue_photo,command=selectblue)
blue_button.place(x=180,y=280)

#orange colour
orange_photo = PhotoImage(file='orange.png')
orange_button = Button(root,border=0,image=orange_photo,command=selectorange)
orange_button.place(x=220,y=280)

#pink colour
pink_photo = PhotoImage(file='pink.png')
pink_button = Button(root,border=0,image=pink_photo,command=selectpink)
pink_button.place(x=260,y=280)

#glassgreen colour
glassgreen_photo = PhotoImage(file='green.png')
glassgreen_button = Button(root,border=0,image=glassgreen_photo,command=selectgreen)
glassgreen_button.place(x=300,y=280)

root.mainloop()