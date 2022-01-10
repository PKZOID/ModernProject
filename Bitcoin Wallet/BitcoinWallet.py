from tkinter import *
from bitcoin import *
root = Tk()
root.title("Bitcoin Wallet")
root.geometry('700x500')
root.resizable(False,False)

#bitcoin wallet address generate
my_private_key = random_key()
public_key = privtopub(my_private_key)
wallet_address = pubtoaddr(public_key)

def generateaddress():
    addressentry.delete(0,END)
    addressentry.insert(END,wallet_address)
#Wallet Label
Wallet_Label = Label(root,text="Wallet",font=("bold",24),border=0)
Wallet_Label.place(x=50,y=50)

Balance = Label(root,text="Balance:",font=('bold',14),border=0)
Balance.place(x=50,y=100)

Btcbalance = Label(root,text="0.000000Btc",font=('bold',12),border=0)
Btcbalance.place(x=125,y=103)

recentwithdraw = Label(root,text="Withdraw:",font=('bold',14),border=0)
recentwithdraw.place(x=50,y=130)

withdrawtext = Label(root,text="0.00000000Btc",font=('bold',12),border=0)
withdrawtext.place(x=137,y=133)

send = Label(root,text="Send:",font=("bold",14),border=0)
send.place(x=50,y=160)

sendtext = Label(root,text="0.00000000Btc",font=('bold',12),border=0)
sendtext.place(x=110,y=163)

revicced = Label(root,text="Revicced:",font=('bold',14),border=0)
revicced.place(x=50,y=190)

reviccedtext = Label(root,text="0.00000000Btc",font=('bold',12),border=0)
reviccedtext.place(x=137,y=193)

#recent transaction
recent_Label = Label(root,text="Recent Transaction",font=("bold",24),border=0)
recent_Label.place(x=400,y=50)

Norevviced = Label(root,text="No AnyRecent\nTransaction",font=('bold',28),border=0,foreground="#999999")
Norevviced.place(x=430,y=130)

#Button Generate Wallet Adddress
Generate = Button(root,text="Generate Address",width=20,height=1,relief='groove',command=generateaddress)
Generate.place(x=260,y=250)

addressentry = Entry(root,width=50,border=0,font=('bold',18))
addressentry.place(x=30,y=280)

#Send Bitcoin
SendBitcoin = Button(root,text="Send Bitcoin",width=20,height=1,relief='groove')
SendBitcoin.place(x=260,y=320)

reviccedsentry = Entry(root,width=50,border=0,font=('bold',18))
reviccedsentry.place(x=30,y=360)


root.mainloop()