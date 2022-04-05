from tkinter import *
root = Tk()
root.geometry('942x671')
root.overrideredirect(1)
root.wm_attributes("-transparentcolor", "grey")

def move_app(e):
	root.geometry(f'+{e.x_root}+{e.y_root}')

#create account click 
def register_user():
    pass

def login_click():
    pass

#photo side bar
frame_photo = PhotoImage(file='frame.png')
frame_label = Label(root,border=0,bg='grey',image=frame_photo)
frame_label.pack(fill=BOTH,expand=True)

#frame photo bind
frame_label.bind("<B1-Motion>", move_app)

#create account image
create_image = PhotoImage(file='Create an account.png')
button_bg_image = PhotoImage(file='buttonbg.png')

#create account place
create_button = Button(root,image=button_bg_image,border=0,bg='white',activebackground='white',command=register_user)
create_button.place(x=530.99,y=496.28)

create_text = Label(root,image=create_image,border=0,bg='#367CFF')
create_text.place(x=578,y=515)

#login text image
login_text = PhotoImage(file='Log in.png')

#login place
login_label = Label(root,image=login_text,border=0,bg='white')
login_label.place(x=809,y=189)

#entry email $ password
entry_email = Entry(root,font=('bold',28),width=14,bg='white',border=0)
entry_email.place(x=540,y=299)

entry_password = Entry(root,font=('bold',28),width=14,bg='white',border=0)
entry_password.place(x=540,y=417)

root.mainloop()