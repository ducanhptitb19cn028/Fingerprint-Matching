import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox

import PIL
from PIL import ImageTk, Image
value_from_label=None

def label_id(value):
    global value_from_label
    value_from_label = value
    print(value_from_label)
    
class ShowSample:
    def __init__(self, root) :
        self.root = root
        self.root.geometry("800x600+300+50")  # kích thước và vị trí hiển thị giao diện
        self.root.title("Quản lý mẫu")
        self.root.iconbitmap('Image\\gaming.ico')
        
        #========== Left frame
        #hien thi list label
        Left_frame = Frame(root, bd=2, bg="white")
        Left_frame.place(x=20, y=10, width=200, height=550)

        self.lst = tk.Listbox(Left_frame, width=20)
        self.lst.pack(side="left", fill=tk.BOTH, expand=0)
        self.lst.place(x=20,y=20,width=150,height=500)
        self.lst.bind("<<ListboxSelect>>", self.showimg)

        sbr=tk.Scrollbar(Left_frame)
        sbr.pack(side=RIGHT,fill="y")
        sbr.config(command=self.lst.yview)

        self.lst.config(yscrollcommand=sbr.set)
        
        #Right Frame hien thi anh
        right_fr = LabelFrame(root, bd=2, bg="white", relief=RIDGE, text="Thông tin mẫu",
                                          font=("times new roman", 12, "bold"))
        right_fr.place(x=230, y=10, width=560, height=550)
        
        #label info
        self.lb = Label(right_fr, text="Tên nhãn:",
                                     font=("times new roman", 12, "bold"), bg="white")
        self.lb.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.lbName = Label(right_fr, text="", font=("times new roman", 12, "bold"),
                                           bg="white", fg="red2")
        self.lbName.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        self.lbName = value_from_label
        
        #image_frame
        img_fr = LabelFrame(right_fr, bd=2, bg="white", relief=RIDGE)
        img_fr.place(x=170, y=120, width=235, height=235)
        
        #image
        self.insertfiles()
        self.canvas = tk.Canvas(img_fr)
        self.canvas.place(x=5,y=5)
        
        delete_btn=Button(right_fr,text="Xóa mẫu",command=self.delete,font=("times new roman",13,"bold"),bg="#000000", fg="white",width=17)
        delete_btn.place(x=200,y=450)
        
    def insertfiles(self):
        lb = str(value_from_label)
        directory1 = f"data/train/{lb}"
        directory2 = f"data/test/{lb}"
        directory3 = f"data/validation/{lb}"
        file_names1 = os.listdir(directory1)
        file_names2 = os.listdir(directory2)
        file_names3 = os.listdir(directory3)
        for f in file_names1:
            full_path = os.path.join(directory1, f)
            self.lst.insert(tk.END, full_path)
        
        
    def showimg(self, event) :
        n = self.lst.curselection()
        filename = self.lst.get(n)
        
        self.img_right = PIL.Image.open(filename)
        self.img_right = self.img_right.resize((220, 220), PIL.Image.ANTIALIAS)
        
        img = ImageTk.PhotoImage(self.img_right)
        w, h = img.width(), img.height()
        print(filename)
        self.canvas.image = img
        self.canvas.config(width=w, height=h)
        self.canvas.create_image(0, 0, image=img, anchor=tk.NW)
        
    def delete(self):

        Exit = messagebox.askyesno("Xóa ảnh", "Bạn có chắc chắn muốn xóa ảnh này?", parent=self.root)
        if (Exit > 0):
            n = self.lst.curselection()
            filename = self.lst.get(n)
            os.remove(filename)
            self.lst.delete(n)  # clear listbox
            messagebox.showinfo("Thông báo", f"Bạn vừa xóa ảnh {filename} thành công.", parent=self.root)
            print("Bạn vừa xóa ảnh" + filename)

        else:
            if not Exit:
                return

if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=ShowSample(root)
    root.mainloop()# cua so hien len