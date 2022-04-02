from tkinter import *
root = Tk()
root.geometry('627x459')
root.overrideredirect(1)
root.wm_attributes("-transparentcolor", "grey")

def exit_click():
    root.quit

def move_app(e):
	root.geometry(f'+{e.x_root}+{e.y_root}')

#photo side bar
frame_photo = PhotoImage(file='frame.png')
frame_label = Label(root,border=0,bg='grey',image=frame_photo)
frame_label.pack(fill=BOTH,expand=True)

#frame photo bind
frame_label.bind("<B1-Motion>", move_app)

#exit button photo
exit_photo = PhotoImage(file='exit.png')

#exit label 
exit_label = Label(root,image=exit_photo,border=0,bg='#332D2D')
exit_label.place(x=590,y=9)

#exit bind
exit_label.bind("<Button>",lambda e:exit_click())

root.mainloop()