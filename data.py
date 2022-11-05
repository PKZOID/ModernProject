import gc
from tkinter import messagebox,filedialog
import os
import pyAesCrypt

gc.collect()

store = "786"

def Lock():
    in_path = filedialog.askopenfilename()
    password = store
    pyAesCrypt.encryptFile(in_path, in_path+".lock", password)
    messagebox.showinfo("File Locked", "Your File Has Been Locked")

def Unlock():
    in_path_dec = filedialog.askopenfilename()
    new_name = os.path.splitext(in_path_dec)[0]
    password = store
    pyAesCrypt.decryptFile(in_path_dec, new_name, password)
    messagebox.showinfo("File Decrypted", "Your File Decrypted")
    
