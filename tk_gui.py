from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from main import *
#creation of GUI window

root=Tk()
root.geometry("800x350")
root.minsize(500,400)
root.title("Encrypter/Decrypter")

Label(text="TEXT ENCRYPTER/DECRYPTER" ,font="elephant 19 bold",padx=10,pady=10, fg="blue").pack()

#Input field
f1=Frame(root)
f1.pack(padx=10,pady=10)
l1=Label(f1,text="Input:", font="Castellar 12 bold").pack(side=LEFT)
scrollbar=Scrollbar(f1)
scrollbar.pack(side=RIGHT,fill=Y)
t1=Text(f1,padx=10,pady=10 ,height=9,width=100 ,border=5 ,yscrollcommand=scrollbar.set)
t1.pack(side=LEFT)
scrollbar.config(command=t1.yview)

#combobox to select fuctions
label=ttk.Label(text='Please select a function:', font="bold")
label.place(x=20, y=255)
comboOneTwoPunch= ttk.Combobox(root, values=('String to Binary', 'Binary to String', 'Decimal to Binary', 'Binary to Decimal', 'Frequency analysis'
	,'Reverse String','ROT13 Encode','ROT13 Decode','base64 Encode','base64 Decode','md5 hashing','salted md5 hashing',
	'sha1 hashing','sha256 hashing','sha512 hashing'), font=('arial', 12, 'normal'), width=15)
comboOneTwoPunch.place(x=200, y=255)

#submit button to execute the functions
f2=Frame(root)
f2.pack()
Button(f2,text="Submit", border=5, command=showMsg).pack(side=LEFT)

#output field for displaying output
f3=Frame(root)
f3.pack(padx=10,pady=10)
l2=Label(f3,text="Output:", font="Castellar 12 bold").pack(side=LEFT)
disp_out=Entry(f3,width=120)
disp_out.pack(side=LEFT)

root.mainloop()
