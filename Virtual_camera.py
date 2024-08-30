from tkinter import *
from tkinter import ttk,font
import cv2,os
from PIL import  Image,ImageTk
import random

def open_camera():
                  ret,frame = vision.read()
                  if ret :
                         new_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                         img = Image.fromarray(new_frame)
                         img = img.resize((550,650))
                         img = ImageTk.PhotoImage(img)
                         l1.imgtk = img
                         l1.configure(image=img)
                         l1.after(10,open_camera)

def capture():
                 ret,frame = vision.read()
                 if ret :
                         v = random.randint(100000,999999)
                         image = cv2.resize(frame,(550,650))
                         path = f"C:\\Users\\DELL\\Desktop\\speech\\Gallery\\"+f"IMG_{v}.png"
                         cv2.imwrite(path,image)
                 # l = 0

                 if blnk != blnk.count(0):
                            blnk.clear()
                            for i in arr :
                                 i.destroy()
                 display_cap()
def display_cap():
    m = 0
    list = os.listdir(f"C:\\Users\\DELL\\Desktop\\speech\\Gallery\\")
    # print(len(list))
    for im in list:
        # print(im)
        image = Image.open(f"C:\\Users\\DELL\\Desktop\\speech\\Gallery\\" + im)
        re = image.resize((100, 100))
        new_image = ImageTk.PhotoImage(re)
        blnk.append(new_image)
        # print(blnk)
    if blnk != len(blnk):
         count = 0
         while count < len(blnk):
                    l = 0
                    for j in range(0,int(766/110)):
                         if count > (len(blnk) - 1):
                                             break
                         print(count)
                         l2 = ttk.Label(frame2,image=blnk[count])
                         l2.place(x=15 + l, y=50 + m, width=100, height=100)
                         arr.append(l2)
                         l = l + 110
                         count = count + 1

                    m = m + 120

page = Tk()
page.title("Virtual_camera")
page.state("zoomed")
style = ttk.Style()
style.configure("TButton",font=("Poppins",16,"bold"),borderwidth = 0)

blnk = []
arr = []
f = font.Font(family="Poppins",size=16,weight="bold")

frame1 = Frame(page,background="black")
frame1.place(x=0,y=0,width=600,height=768)

l1 = ttk.Label(frame1,background="black")
l1.pack()

frame2 = Frame(page,background="white")
frame2.place(x=600,y=0,width=766,height=768)

display_cap()
image = Image.open("images-removebg-preview.png")
re = image.resize((50, 50))
new_i = ImageTk.PhotoImage(re)

ttk.Label(frame2,text="Gallery",font=f,background="white").place(x=10,y=10,width=100,height=30)

Button(frame1,text="Capture",command=capture,image=new_i,background="black",borderwidth=0).place(x=275,y=655,width=60,height=50)

vision = cv2.VideoCapture(0)

if vision.isOpened() :
         open_camera()

page.mainloop()


