from tkinter import *
import PyPDF2
from tkinter import filedialog
import tkxui
root = tkxui.Tk(display=tkxui.FRAMELESS)
root.geometry('550x500')
root.center()
root.config_border(
        {
            'border': {
                'bg': "black"
            },
            'maximize': {
                'fg': 'white',
                'hoverfg': 'white',
                'hoverbg': 'black',
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

background = Label(root,width=237,height=134,border=0)
background.place(x=0,y=35)

setting_new_image = PhotoImage(file='settings-5666.png')
setting_new = Button(root,border=0,image=setting_new_image)

def selectcolour():
  setting_button.destroy()
  setting_new.place(x=510,y=450)
  def selectblack():
    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='select black.png')

    glassgreen_button.configure(bg='black',activebackground='black')
    pink_button.configure(bg='black',activebackground='black')
    blue_button.configure(bg='black',activebackground='black')
    setting_new.configure(bg='black',activebackground='black')
    orange_button.configure(bg='black',activebackground='black')
    black_button.configure(bg='black',activebackground='black')

    pdf_button.configure(bg='black',activebackground='black')
    text_pdf.configure(bg='black',foreground='white')
    pdf_button.configure(bg='black',activebackground='black')
    background.configure(bg='black',activebackground='black')
  def selectorange():
    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='blue.png')
    black_photo.configure(file='Black.png')
    orange_photo.configure(file='select orange.png')

    glassgreen_button.configure(bg='orange',activebackground='orange')
    pink_button.configure(bg='orange',activebackground='orange')
    blue_button.configure(bg='orange',activebackground='orange')
    orange_button.configure(bg='orange',activebackground='orange')
    setting_new.configure(bg='orange',activebackground='orange')
    black_button.configure(bg='orange',activebackground='orange')

    pdf_button.configure(bg='orange',activebackground='orange')
    text_pdf.configure(bg='orange',foreground='white')
    pdf_button.configure(bg='orange',activebackground='orange')
    background.configure(bg='orange')
  def selectblue():
    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='select blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='Black.png')

    glassgreen_button.configure(bg='#0096FF',activebackground='#0096FF')
    pink_button.configure(bg='#0096FF',activebackground='#0096FF')
    blue_button.configure(bg='#0096FF',activebackground='#0096FF')
    orange_button.configure(bg='#0096FF',activebackground='#0096FF')
    setting_new.configure(bg='#0096FF',activebackground='#0096FF')
    black_button.configure(bg='#0096FF',activebackground='#0096FF')

    pdf_button.configure(bg='#0096FF',activebackground='#0096FF')
    text_pdf.configure(bg='#0096FF',foreground='white')
    pdf_button.configure(bg='#0096FF',activebackground='#0096FF')
    background.configure(bg='#0096FF')
  def selectpink():
    glassgreen_photo.configure(file='green.png')
    pink_photo.configure(file='select pink.png')
    blue_photo.configure(file='blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='Black.png')

    glassgreen_button.configure(bg='hotpink',activebackground='hotpink')
    pink_button.configure(bg='hotpink',activebackground='hotpink')
    blue_button.configure(bg='hotpink',activebackground='hotpink')
    orange_button.configure(bg='hotpink',activebackground='hotpink')
    setting_new.configure(bg='hotpink',activebackground='hotpink')
    black_button.configure(bg='hotpink',activebackground='hotpink')

    pdf_button.configure(bg='hotpink',activebackground='hotpink')
    text_pdf.configure(bg='hotpink',foreground='white')
    pdf_button.configure(bg='hotpink',activebackground='hotpink')
    background.configure(bg='hotpink')
  def selectgreen():
  
    glassgreen_photo.configure(file='select green.png')
    pink_photo.configure(file='pink.png')
    blue_photo.configure(file='blue.png')
    orange_photo.configure(file='orange.png')
    black_photo.configure(file='Black.png')

    glassgreen_button.configure(bg='#1fe0ae',activebackground='#1fe0ae')
    pink_button.configure(bg='#1fe0ae',activebackground='#1fe0ae')
    blue_button.configure(bg='#1fe0ae',activebackground='#1fe0ae')
    orange_button.configure(bg='#1fe0ae',activebackground='#1fe0ae')
    setting_new.configure(bg='#1fe0ae',activebackground='#1fe0ae')
    black_button.configure(bg='#1fe0ae',activebackground='#1fe0ae')

    pdf_button.configure(bg='#1fe0ae',activebackground='#1fe0ae')
    text_pdf.configure(bg='#1fe0ae',foreground='white')
    pdf_button.configure(bg='#1fe0ae',activebackground='#1fe0ae')
    background.configure(bg='#1fe0ae')
  #black colour
  black_photo = PhotoImage(file='Black.png')
  black_button = Button(root,border=0,image=black_photo,command=selectblack)
  black_button.place(x=50,y=50)

  #blue colour
  blue_photo = PhotoImage(file='blue.png')
  blue_button = Button(root,border=0,image=blue_photo,command=selectblue)
  blue_button.place(x=130,y=50)

  #orange colour
  orange_photo = PhotoImage(file='orange.png')
  orange_button = Button(root,border=0,image=orange_photo,command=selectorange)
  orange_button.place(x=90,y=50)

  #pink colour
  pink_photo = PhotoImage(file='pink.png')
  pink_button = Button(root,border=0,image=pink_photo,command=selectpink)
  pink_button.place(x=170,y=50)

  #glassgreen colour
  glassgreen_photo = PhotoImage(file='green.png')
  glassgreen_button = Button(root,border=0,image=glassgreen_photo,command=selectgreen)
  glassgreen_button.place(x=210,y=50)

def file_open():
     file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF Files","*.pdf"),("All Files","*.*")))
     if file:
        text_pad = Text(root,border=0,width=237,height=134,font=('bold',15))
        text_pad.place(x=0,y=37)
        text_pad.delete(END,1.0)
#Open the PDF File
        pdf_file= PyPDF2.PdfFileReader(file)
      #Select a Page to read
        page= pdf_file.getPage(0)
      #Get the content of the Page
        content=page.extractText()
      #Add the content to TextBox
        text_pad.insert(1.0,content)
        pdf_button.destroy()
        text_pdf.destroy()      

title = Label(root,text="PDF READER",border=0,bg='black',foreground='white',font=('bold',13))
title.place(x=1,y=12)

text_pdf = Label(root,text="UPLOAD PDF TO VIEW",font=('bold',15))
text_pdf.place(x=155,y=330)

setting_image = PhotoImage(file='settings-5666.png')
setting_button = Button(root,border=0,image=setting_image,command=selectcolour)
setting_button.place(x=510,y=450)

pdf_image = PhotoImage(file='PDF_image.png')
pdf_button = Button(root,border=0,image=pdf_image,command=file_open)
pdf_button.place(x=200,y=180)


root.mainloop()
