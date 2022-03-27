from tkinter import *
import tkxui
root = tkxui.Tk(display=tkxui.FRAMELESS)
root.geometry('914x607')

#photo
Python_weather = PhotoImage(file='Python Weather.png')
create_pkzoid = PhotoImage(file='Create By Pkzoid.png')
weather_name = PhotoImage(file='Type the name of a city to find our the weather condition.png')
city_Name = PhotoImage(file='City Name.png')
serach_label = PhotoImage(file='Rectangle 1.png')
submit_text = PhotoImage(file='Submit.png')
submit_button = PhotoImage(file='Rectangle 2.png')
penguin_photo = PhotoImage(file='taxi-autopilot 1.png')

def click_serach():
    serach_label_entry.place(x=325,y=490)
def submit_serach():
    pass

#label
penguin_label = Label(root,image=penguin_photo,border=0)
penguin_label.place(x=485,y=-22)

Python_weather_label = Label(root,image=Python_weather,border=0)
Python_weather_label.place(x=45,y=20)

create_pkzoid_label = Label(root,image=create_pkzoid,border=0)
create_pkzoid_label.place(x=45,y=287)

weather_name_label = Label(root,image=weather_name,border=0)
weather_name_label.place(x=174,y=419)

serach_label_label = Label(root,image=serach_label,border=0)
serach_label_label.place(x=324,y=479)

city_Name_label = Label(root,image=city_Name,border=0,bg='white')
city_Name_label.place(x=337,y=496)

submit_button_label = Label(root,image=submit_button,border=0)
submit_button_label.place(x=603,y=480)

submit_text_label = Label(root,image=submit_text,border=0,bg='#FFCA0F')
submit_text_label.place(x=637,y=496)

#serach label
serach_label_entry = Entry(root,width=16,font=('bold',19),border=0)

#label bind
serach_label_label.bind("<Button>",lambda e:click_serach())

root.mainloop()