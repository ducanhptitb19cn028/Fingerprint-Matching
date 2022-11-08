import os
import shutil
from time import strftime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import PIL.Image
from PIL import Image, ImageTk


class Labell:
    def __init__(self,root):
        self.root=root
        w = 1250  # chiều dài giao diện
        h = 766  # chiều rộng giao diện

        ws = self.root.winfo_screenwidth()  # độ dài màn hình
        hs = self.root.winfo_screenheight()  # độ rộng màn
        x = (ws / 2) - (w / 2)  # vị trí cách lề trái x px
        y = (hs / 2) - (h / 2)  # vị trí cách lề trên y px

        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))  # kích thước và vị trí hiển thị giao diện
        self.root.title("Quản lý nhãn")
        self.root.iconbitmap('Image\\gaming.ico')
        today = strftime("%d-%m-%Y")

        img3 = PIL.Image.open(r"Image\bgnt.png")#Ảnh nền
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)#label chứa ảnh nền
        bg_img.place(x=0, y=0, width=1250, height=766)
        
         # ==================================heading====================================
        # ====time====
        img_time = PIL.Image.open(r"Image\timsearch50.png")#Ảnh icon thời gian
        img_time = img_time.resize((27, 27), PIL.Image.ANTIALIAS)
        self.photoimgtime = ImageTk.PhotoImage(img_time)
        time_img = Label(self.root, image=self.photoimgtime, bg="white")
        time_img.place(x=43, y=40, width=27, height=27)
        
        def time():#Hàm thời gian thay đổi mỗi giây
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(self.root, font=("times new roman", 11, "bold"), bg="white", fg="black")
        lbl.place(x=80, y=35, width=100, height=18)
        time()#chạy hàm time
        lbl1 = Label(self.root, text=today, font=("times new roman", 11, "bold"), bg="white", fg="black")
        lbl1.place(x=80, y=60, width=100, height=18)
        
        # ====title=========
        self.txt = "Quản lý nhãn"#tiêu đề
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.root, text=self.txt, font=("times new roman", 24, "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)
        self.heading.place(x=300, y=25, width=650)
        # self.slider()
        # self.heading_color()

        main_frame = Frame(bg_img, bd=2, bg="white")#main frame
        main_frame.place(x=24, y=90, width=1200, height=650)
        
        #biến tên nhãn
        self.var_lb_name = StringVar()
    
        
        #================================================================================================================
        #================================================================================================================
        # Frame bên phải chứa bảng dữ liệu và chức năng tìm kiếm
        Right_frame = LabelFrame(main_frame, bd=2, bg="white",
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=515, y=50, width=610, height=550)
        
        #Tìm kiếm
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Danh sách các nhãn",
                                         font=("times new roman", 11, "bold"))
        search_frame.place(x=5, y=5, width=600, height=70)
        search_label = Label(search_frame, text="Nhập tên nhãn", font=("times new roman", 12, "bold"),
                            bg="white",fg="red2")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.var_search = StringVar()#Chữ cần tìm kiếm
        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 13, "bold"),textvariable=self.var_search)
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        #Nút tìm kiếm
        img_btn3 = PIL.Image.open(r"Image\btnRed.png")#ảnh nền màu đỏ
        img_btn3 = img_btn3.resize((105, 35), PIL.Image.ANTIALIAS)#resize ảnh
        self.photobtn3 = ImageTk.PhotoImage(img_btn3)#convert ảnh dạng ImageTk để truyền vào Button
        #nút tìm kiếm
        search_btn = Button(search_frame, text="Tìm kiếm", font=("times new roman", 11, "bold"),command=self.search_data,bd=0,bg="white",cursor='hand2' ,activebackground='white',
                        width=105,image=self.photobtn3,fg="white",compound="center")
        search_btn.grid(row=0, column=3,padx=4)

        #nút xem tất cả
        showAll_btn = Button(search_frame, text="Xem tất cả", font=("times new roman", 11, "bold"), command=self.fetch_data,bd=0,bg="white",cursor='hand2' ,activebackground='white',
                        width=105,image=self.photobtn3,fg="white",compound="center")
        showAll_btn.grid(row=0, column=4,padx=4)
        
        
        #Bảng dữ liệu
        # table_label = Label(main_frame, text="Danh sách các nhãn",  font=("times new roman", 20, "bold"), bg="white")
        # table_label.grid(row=0, column=0, padx=800,pady=50, sticky=W)
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=85, width=600, height=455)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
         #các trường dữ liệu
        self.label_table=ttk.Treeview(table_frame,column=("id","name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.label_table.xview)
        scroll_y.config(command=self.label_table.yview)
        
        
        #đặt tên các cột dữ liệu
        self.label_table.heading("id", text="STT")
        self.label_table.heading("name", text="Tên nhãn")
        self.label_table["show"]="headings"
        
        
        #độ dài các cột
        self.label_table.column("id", width=100)
        self.label_table.column("name", width=100)
        self.label_table.pack(fill=BOTH,expand=1)
        self.label_table.bind("<ButtonRelease>",self.get_cursor)#sự kiện khi click vào bảng các thông tin in ra các txtbox
        self.fetch_data()#load du lieu len bảng
        
        
        
       
        #================================================================================================================
        #================================================================================================================
        #left_label
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",font=("times new roman",12,"bold"))
        Left_frame.place(x=15,y=50,width=500, height=550)
        
        #Frame thông tin nhan
        label_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Xử lí thông tin nhãn",
                                font=("times new roman", 12, "bold"))
        label_frame.place(x=5, y=7, width=480, height=540)
        
        labelname = Label(Left_frame, text="Tên nhãn : ",  font=("times new roman", 13, "bold"), bg="white")
        labelname.grid(row=0, column=0, padx=30,pady=50, sticky=W)
        self.labelname_entry=Entry(Left_frame,width=23,textvariable=self.var_lb_name, font=("times new roman", 13, "normal"))
        self.labelname_entry.grid(row=0,column=1,padx=70,pady=50,sticky=W)
       
       
        #nút lưu thông tin nhan
        img_btn1 = PIL.Image.open(r"Image\btnRed.png")
        img_btn1 = img_btn1.resize((120, 35), PIL.Image.ANTIALIAS)
        self.photobtn1 = ImageTk.PhotoImage(img_btn1)
        save_btn=Button(Left_frame,text="Lưu",command=self.add_data,font=("times new roman",11,"bold"),bd=0,bg="white",cursor='hand2' ,activebackground='white',
                        width=115,image=self.photobtn1,fg="white",compound="center")
        save_btn.place(x=70,y=150)
        
        # nút xoa thông tin nhan
        delete_btn=Button(Left_frame,text="Xóa",command=self.delete_data,font=("times new roman",11,"bold"),bd=0,bg="white",cursor='hand2' ,activebackground='white',
                        width=115,image=self.photobtn1,fg="white",compound="center")
        delete_btn.place(x=270,y=150)
        
        
        # nút lam moi
        reset_btn=Button(Left_frame,text="Làm mới",command=self.reset_data,font=("times new roman",11,"bold"),bd=0,bg="white",cursor='hand2' ,activebackground='white',
                        width=115,image=self.photobtn1,fg="white",compound="center")
        reset_btn.place(x=70,y=250)
        
    def add_data(self):
        
        label_array = []
        path = 'data/test/'
        for _, dirnames, filenames in os.walk(path):
            label_array=dirnames
            break
        
        if self.labelname_entry.get() == "" :
            messagebox.showerror("Error","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        elif ( self.labelname_entry.get() in label_array) :
                  messagebox.showerror("Error","Thông tin nhãn đã tồn tại",parent=self.root)
        else :
            os.mkdir("data/test/"+self.labelname_entry.get())
            os.mkdir("data/train/"+self.labelname_entry.get())
            os.mkdir("data/validation/"+self.labelname_entry.get())
    
    def delete_data(self):
        
        label_array = []
        path = 'data/test/'
        for _, dirnames, filenames in os.walk(path):
            label_array=dirnames
            break
        
        if self.labelname_entry.get() == "" :
            messagebox.showerror("Error","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else :
            delete=messagebox.askyesno("Xoá Học sinh","Bạn có muốn xóa Học sinh này?",parent=self.root)
            if delete>0:
                shutil.rmtree("data/test/"+self.labelname_entry.get())
                shutil.rmtree("data/train/"+self.labelname_entry.get())
                shutil.rmtree("data/validation/"+self.labelname_entry.get())
                messagebox.showinfo("Xóa","Xóa Học sinh thành công",parent=self.root)
            else:
                if not delete:
                    return
    
    def reset_data(self) :
        self.label_table.delete(*self.label_table.get_children()) #xóa dữ liệu cũ
        
            #============ Lấy danh sách nhãn bằng tên các folder trong thư mục
        label_array = []
        path = 'data/test/'
        for _, dirnames, filenames in os.walk(path):
            label_array=dirnames
            break
        index = 1;
        for i in label_array:
            self.label_table.insert("", END, values=(index, i))
            index+=1
    
    def search_data(self):
        
        label_array = []
        path = 'data/test/'
        for _, dirnames, filenames in os.walk(path):
            label_array=dirnames
            break
        if self.var_search.get() == "":
            messagebox.showerror("Lỗi !", "Vui lòng nhập thông tin đầy đủ",parent=self.root)
        else : 
            if self.var_search.get() in label_array:
                self.label_table.delete(*self.label_table.get_children())
                self.label_table.insert("", END, values=(1,self.var_search.get()))
            else:#nếu ko có dữ liệu thông báo ko có bản ghi 
                self.label_table.delete(*self.label_table.get_children())
                messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                
        
    def fetch_data(self):
        self.label_table.delete(*self.label_table.get_children()) #xóa dữ liệu cũ
        
            #============ Lấy danh sách nhãn bằng tên các folder trong thư mục
        label_array = []
        path = 'data/test/'
        for _, dirnames, filenames in os.walk(path):
            label_array=dirnames
            break
        index = 1;
        for i in label_array:
            self.label_table.insert("", END, values=(index, i))
            index+=1
        
    #======================get-cursor==============================
    def get_cursor(self,event=""):#Sự kiện khi click vào bảng thì hiện chi tiết thông tin ra các txtbox
        cursor_focus=self.label_table.focus()
        content=self.label_table.item(cursor_focus)
        data=content["values"]
        self.var_lb_name.set(data[1]),
        
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao

    obj=Labell(root)
    root.mainloop()# cua so hien len