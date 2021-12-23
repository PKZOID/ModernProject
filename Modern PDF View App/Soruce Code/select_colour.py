from tkinter import *
import tkxui
colour = tkxui.Tk(display=tkxui.FRAMELESS)
colour.center()
colour.config_border(
        {
            'border': {
                'bg': "#14E8C4"
            },
            'maximize': {
                'fg': 'black',
                'hoverfg': 'white',
                'hoverbg': '#14E8C4',
                'bg': '#14E8C4'
            },
            'minimize': {
                'fg': 'black',
                'hoverfg': 'white',
                'hoverbg': '#14E8C4',
                'bg': '#14E8C4'
            },
            'close': {
                'hoverbg': '#14E8C4',
                'hoverfg': 'white',
                'fg': 'black',
                'bg': '#14E8C4'
            }
        }
    )
colour.geometry('300x100')
def selectblack():
    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='select black.png')
def selectorange():
    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='blue.png')
    black_photo.configure(file='Black.png')
    orange_photo.configure(file='select orange.png')
def selectblue():
    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='select blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='Black.png')
def selectpink():
    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='select pink.png')
    blue_photo.configure(file='blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='Black.png')
def selectgreen():
    glassgreen_photo.configure(file='select green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='Black.png')
#black colour
black_photo = PhotoImage(file='Black.png')
black_button = Button(colour,border=0,image=black_photo,command=selectblack)
black_button.place(x=50,y=50)

#blue colour
blue_photo = PhotoImage(file='blue.png')
blue_button = Button(colour,border=0,image=blue_photo,command=selectblue)
blue_button.place(x=130,y=50)

#orange colour
orange_photo = PhotoImage(file='orange.png')
orange_button = Button(colour,border=0,image=orange_photo,command=selectorange)
orange_button.place(x=90,y=50)

#pink colour
pink_photo = PhotoImage(file='pink.png')
pink_button = Button(colour,border=0,image=pink_photo,command=selectpink)
pink_button.place(x=170,y=50)

#glassgreen colour
glassgreen_photo = PhotoImage(file='green.png')
glassgreen_button = Button(colour,border=0,image=glassgreen_photo,command=selectgreen)
glassgreen_button.place(x=210,y=50)

colour.mainloop()