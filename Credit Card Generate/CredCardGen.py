from tkinter import *

import tkxui
import random
root = tkxui.Tk(display=tkxui.FRAMELESS)
root.config_border(
        {
            'border': {
                'bg': "white"
            },
            'maximize': {
                'fg': 'black',
                'hoverfg': 'white',
                'hoverbg': '#14E8C4',
                'bg': 'white'
            },
            'minimize': {
                'fg': 'black',
                'hoverfg': 'white',
                'hoverbg': '#14E8C4',
                'bg': 'white'
            },
            'close': {
                'hoverbg': '#14E8C4',
                'hoverfg': 'white',
                'fg': 'black',
                'bg': 'white'
            }
        }
    )
root.geometry('750x550')
root.resizable(False,False)

def generate_number():
    list = ["3","7","7","3","7","7","5","5","5","8","9","7","5","9","0","4","4"]
    number = ""
    for i in range(16):
        number = number + random.choice(list)
    creditcard_number.configure(text=number)
    namelist = ["T","I","F","S","I","D","D","I","Q","U","E","P","K","G","A","M","A"]
    name = ""
    for i in range(8):
        name = name + random.choice(namelist)
    name_text.configure(text=name)

title = Label(root,text="CreditCard Generate",font=('bold',12),border=0,bg='white')
title.place(x=10,y=10)

creditcard_photo = PhotoImage(file='creditcard.png')

creditcard_Label = Label(root,image=creditcard_photo,border=0)
creditcard_Label.place(x=70,y=100)

generate_photo = PhotoImage(file='Generate.png')
generate_button = Label(root,image=generate_photo,border=0)
generate_button.place(x=310,y=450)
generate_button.bind("<Button-1>", lambda e:generate_number())

creditcard_number = Label(root,font=('bold',38),border=0,bg='#1A1A1A',foreground='white')
creditcard_number.place(x=150,y=260)

name_text = Label(root,font=('bold',17),text="PKGAMER",border=0,bg='#1A1A1A',foreground='white')
name_text.place(x=290,y=333)

date = Label(root,font=('bold',17),text="Date:",border=0,bg='#1A1A1A',foreground='white')
date.place(x=530,y=333)

date_text = Label(root,font=('bold',16),text="1/1/2021",border=0,bg='#1A1A1A',foreground='white')
date_text.place(x=590,y=333)

root.mainloop()
