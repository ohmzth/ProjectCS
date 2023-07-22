from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import process
w = Tk()
w.title("Live shop admin ")
mylabel1 =Label(text="Live Shop Admin",font=50).pack()
w.geometry("800x700")
mylabel2=Label(text="ร้านปิรันย่าซ๊อป",font=50).place(x=100,y=70)
mylabel3=Label(text="ของฝากใต้ราคาถูก",font=50).place(x=330,y=70)
mylabel3=Label(text="Aoom shop live V2",font=50).place(x=550,y=70)
def ShopDisplay(img1,x1,y1):
    img = Image.open(img1)
    img = img.resize((220, 400), Image.LANCZOS)
    tkimage= ImageTk.PhotoImage(img)
    label=Label(w,image=tkimage)
    label.place(x=30+x1,y=120+y1)

    button1 = tk.Button(w, text="Capture",background='green',command=lambda: print("Create"))
    button1.pack(pady=10, padx=15)
    button1.place(x=30+x1,y=530+y1)
    button2 = tk.Button(w, text="Detail", background='yellow' ,command=lambda: print("Detail"))
    button2.pack(pady=10, padx=15)
    button2.place(x=120+x1,y=530+y1)
    button3 = tk.Button(w, text="Clear", background='red' ,command=lambda: print("Delete"))
    button3.pack(pady=10, padx=20)
    button3.place(x=210+x1,y=530+y1)
ShopDisplay(process.frame1,0,0)
ShopDisplay("kan23.png",250,0)
ShopDisplay("kan23.png",500,0)
w.mainloop()
