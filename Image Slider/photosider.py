from tkinter import *
root = Tk()
root.title("Photo Slider")
root.geometry('630x400')
root.resizable(False,False)

#def on_next
def on_next():
    image_show_box_photo.configure(file='wallpaper2.png')
    back_button_label.bind("<Button>",lambda e:onclick_back())
def onclick_back():
    image_show_box_photo.configure(file='wallpaper show.png')
    back_button_label.bind("<Button>",lambda e:on_next())

#back image button
back_button_photo = PhotoImage(file='Back.png')
back_button_label = Label(root,image=back_button_photo,border=0)
back_button_label.place(x=50,y=100)

#next image button
next_button_photo = PhotoImage(file='next.png')
next_button_label = Label(root,image=next_button_photo,border=0)
next_button_label.place(x=50*10,y=100)

#image show box
image_show_box_photo = PhotoImage(file='wallpaper show.png')
image_show_box_label = Label(root,image=image_show_box_photo,border=0)
image_show_box_label.place(x=150,y=50)

#label bind
back_button_label.bind("<Button>",lambda e:on_next())
next_button_label.bind("<Button>",lambda e:onclick_back())

root.mainloop()