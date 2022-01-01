from tkinter import *
import tkxui

root = tkxui.Tk(display=tkxui.FRAMELESS)
root.config_border(
        {
            'border': {
                'bg': "#25262A"
            },
            'maximize': {
                'fg': 'white',
                'hoverfg': 'white',
                'hoverbg': '#14E8C4',
                'bg': '#25262A'
            },
            'minimize': {
                'fg': 'white',
                'hoverfg': 'white',
                'hoverbg': '#14E8C4',
                'bg': '#25262A'
            },
            'close': {
                'hoverbg': '#14E8C4',
                'hoverfg': 'white',
                'fg': 'white',
                'bg': '#25262A'
            }
        }
    )
root.geometry('750x550')
root.resizable(False,False)
root.center()

#background
background_label = Label(root,bg='#1C1919',border=0,width=750,height=550)
background_label.pack()

#title label
title_label = Label(root,text="Popcorn Time",foreground='white',bg='#25262A',font=('bold',15))
title_label.place(x=500,y=5)

#Menu Label Activebackground
activelines_image = PhotoImage(file='activelines.png')
bluelines = Label(root,image=activelines_image,border=0,bg='#1C1919')

def Anime():
    #Add Your Function
    bluelines.place(x=170,y=80)

def tvactive():
    #Add Your Function
    bluelines.place(x=95,y=80)

def moveactive():
    #Add Your Function
    bluelines.place(x=15,y=80)

#menu icon
find_icon = PhotoImage(file='find.png')
find_label = Button(root,image=find_icon,border=0,bg='#1C1919',activebackground='#1C1919')
find_label.place(x=1000,y=50)

mail_icon = PhotoImage(file='mail.png')
mail_label = Button(root,image=mail_icon,border=0,bg='#1C1919',activebackground='#1C1919')
mail_label.place(x=1030,y=50)

heart_icon = PhotoImage(file='heart.png')
heart_label = Button(root,image=heart_icon,border=0,bg='#1C1919',activebackground='#1C1919')
heart_label.place(x=1060,y=50)

setting_icon = PhotoImage(file='setting.png')
setting_label = Button(root,image=setting_icon,border=0,bg='#1C1919',activebackground='#1C1919')
setting_label.place(x=1087,y=50)

information_icon = PhotoImage(file='information.png')
information_label = Button(root,image=information_icon,border=0,bg='#1C1919',activebackground='#1C1919')
information_label.place(x=1109,y=50)

netflix_icon = PhotoImage(file='netflix.png')
netflix_label = Button(root,image=netflix_icon,border=0,bg='#1C1919',activebackground='#1C1919')
netflix_label.place(x=1127,y=50)

#Menu Label
Movies = Button(root,text="Movies",foreground='#b5b5b5',font=('bold',12),border=0,bg='#1C1919',activebackground='#1C1919',activeforeground='#b5b5b5',command=moveactive)
Movies.place(x=10,y=50)

Tvseries = Button(root,text="Tv Series",foreground='#b5b5b5',font=('bold',12),border=0,bg='#1C1919',activebackground='#1C1919',activeforeground='#b5b5b5',command=tvactive)
Tvseries.place(x=80,y=50)

Anime = Button(root,text="Anime",foreground='#b5b5b5',font=('bold',12),border=0,bg='#1C1919',activebackground='#1C1919',activeforeground='#b5b5b5',command=Anime)
Anime.place(x=165,y=50)

moveactive()
root.mainloop()