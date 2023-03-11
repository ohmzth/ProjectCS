from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
w = Tk()
w.title("Live shop admin ")
mylabel1 =Label(text="Live Shop Admin",font=50).pack()
w.geometry("800x700")

def shopname1(mylabel2=Label):
    mylabel2=Label(text="ร้านปิรันย่าซ๊อป",font=50).place(x=100,y=70)
def shopname2(mylabel2=Label):    
    mylabel3=Label(text="ของฝากใต้ราคาถูก",font=50).place(x=330,y=70)
def shopname3(mylabel2=Label):    
    mylabel3=Label(text="Aoom shop live V2",font=50).place(x=550,y=70)

shopname1()
shopname2()
shopname3()





def Imageshop1(label):
    img = Image.open("a31.png")
    img = img.resize((220, 400), Image.LANCZOS)
    tkimage = ImageTk.PhotoImage(img)
    label.configure(image=tkimage)
    label.image = tkimage  
    label.place(x=30, y=120)
    return label

def Imageshop2():
    img = Image.open("kan24.png")
    img = img.resize((220, 400), Image.LANCZOS)
    tkimage = ImageTk.PhotoImage(img)
    label = Label(w, image=tkimage)
    label.image = tkimage  
    label.place(x=280, y=120)
    return label

def Imageshop3():
    img = Image.open("kan23.png")
    img = img.resize((220, 400), Image.LANCZOS)
    tkimage = ImageTk.PhotoImage(img)
    label = Label(w, image=tkimage)
    label.image = tkimage  
    label.place(x=530,y=120)
    return label

label = Label(w)
label = Imageshop1(label)
label2 = Imageshop2()
label3 = Imageshop3()
    



button1 = tk.Button(w, text="Capture",background='green',command=lambda: print("Button was clicked!"))
button1.pack(pady=10, padx=15)
button1.place(x=30,y=530)
button2 = tk.Button(w, text="Detail", background='yellow' ,command=lambda: print("Button was clicked!"))
button2.pack(pady=10, padx=15)
button2.place(x=120,y=530)
button3 = tk.Button(w, text="Clear", background='red' ,command=lambda: print("Button was clicked!"))
button3.pack(pady=10, padx=20)
button3.place(x=210,y=530)
w.mainloop()
