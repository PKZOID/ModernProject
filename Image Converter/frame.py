from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

root = Tk()
root.wm_attributes('-transparentcolor', 'grey')
root.overrideredirect(1)
root.geometry('559x407')
def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')

frame_photo = PhotoImage(file='frame.png')
frame_label = Label(root,border=0,bg='grey',image=frame_photo)
frame_label.pack()
frame_label.bind('<B1-Motion>',move_app)

def upload_image():
    global upload_photo
    filename = filedialog.askopenfilename()
    upload_photo = tk.PhotoImage(file=filename)
    upload_label.configure(image=upload_photo)
    upload_text_photo.configure(file='save.png')
    upload_label.configure(command=DISABLED)

def save_image():
    files = [ ('Jpg', '*.Jpg')]
    file = asksaveasfile(filetypes = files, defaultextension = files)

upload_photo = PhotoImage(file='upload.png')
upload_label = Button(root,image=upload_photo,border=0,bg='#FFFFFF',activebackground='#FFFFFF',command=upload_image)
upload_label.place(x=168,y=71)

upload_text_photo = PhotoImage(file='uploadtext.png')
upload_photo_text = Button(root,image=upload_text_photo,border=0,bg='#FFFFFF',activebackground='#FFFFFF',command=save_image)
upload_photo_text.place(x=157,y=297)

root.mainloop()
