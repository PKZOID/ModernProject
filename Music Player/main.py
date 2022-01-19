from tkinter import *
import tkxui
root = tkxui.Tk(display=tkxui.FRAMELESS)
root.config_border(
        {
            'border': {
                'bg': "#343434"
            },
            'maximize': {
                'fg': 'white',
                'hoverfg': 'white',
                'hoverbg': '#14E8C4',
                'bg': '#343434'
            },
            'minimize': {
                'fg': 'white',
                'hoverfg': 'white',
                'hoverbg': '#14E8C4',
                'bg': '#343434'
            },
            'close': {
                'hoverbg': '#14E8C4',
                'hoverfg': 'white',
                'fg': 'white',
                'bg': '#343434'
            }
        }
    )
root.geometry('700x600')
root.resizable(False,False)
root.center()

#title $ backgrond
title = Label(root,bg='#343434',text="Music",foreground='white',font=('60')).place(x=5,y=5)
background = Label(root,bg='white',width=500,height=500,border=0).pack()

#$ function
def play():
    print("play")

#text
release = Label(root,text="New Release Song For You",font=('bold',18),border=0,bg='white').place(x=10,y=50)
hot_right_now = Label(root,text="Hot Right Now",font=('bold',18),border=0,bg='white').place(x=10,y=240)
playlist = Label(root,text="PlayList",font=('bold',18),border=0,bg='white').place(x=10,y=420)

#image
music_photo = PhotoImage(file='music.png')
music_thumbial = PhotoImage(file='Music Thumbial.png')

#playlist
pop_music = PhotoImage(file='Pop Music.png')

#label image
music_label = Label(root,image=music_photo,border=0,bg='white').place(x=310,y=50)
music_label1 = Label(root,image=music_photo,border=0,bg='white').place(x=170,y=240)

#new release song for you
music_thumbial1 = Label(root,image=music_thumbial,border=0,bg='white')
music_thumbial1.place(x=0,y=90)
music_thumbial2 = Label(root,image=music_thumbial,border=0,bg='white').place(x=120,y=90)
music_thumbial3 = Label(root,image=music_thumbial,border=0,bg='white').place(x=240,y=90)
music_thumbial4 = Label(root,image=music_thumbial,border=0,bg='white').place(x=360,y=90)
music_thumbial5 = Label(root,image=music_thumbial,border=0,bg='white').place(x=480,y=90)

#hot right now 
music_thumbial6 = Label(root,image=music_thumbial,border=0,bg='white').place(x=0,y=280)
music_thumbial7 = Label(root,image=music_thumbial,border=0,bg='white').place(x=120,y=280)
music_thumbial8 = Label(root,image=music_thumbial,border=0,bg='white').place(x=240,y=280)
music_thumbial9 = Label(root,image=music_thumbial,border=0,bg='white').place(x=360,y=280)
music_thumbial10 = Label(root,image=music_thumbial,border=0,bg='white').place(x=480,y=280)

#playlist
music_thumbial11 = Label(root,image=pop_music,border=0,bg='white').place(x=0,y=450)

#bind Label
music_thumbial1.bind("<Button>",lambda e:play())


root.mainloop()