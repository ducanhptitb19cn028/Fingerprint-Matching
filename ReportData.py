import os
from time import strftime, localtime
from tkinter import *
from tkinter import ttk

import PIL.Image
from PIL import Image, ImageTk


class Report:
    def __init__(self,root):
        self.root=root
        w = 1250  # chiều dài giao diện
        h = 766  # chiều rộng giao diện

        ws = self.root.winfo_screenwidth()  # độ dài màn hình
        hs = self.root.winfo_screenheight()  # độ rộng màn
        x = (ws / 2) - (w / 2)  # vị trí cách lề trái x px
        y = (hs / 2) - (h / 2)  # vị trí cách lề trên y px
        
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))  # kích thước và vị trí hiển thị giao diện
        self.root.title("Thống kế dữ liệu")
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
        self.txt = "Thống kê"#tiêu đề
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.root, text=self.txt, font=("times new roman", 24, "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)
        self.heading.place(x=300, y=25, width=650)
        img_btn1 = PIL.Image.open(r"Image\btnRed.png")
        img_btn1 = img_btn1.resize((120, 35), PIL.Image.ANTIALIAS)
        self.photobtn1 = ImageTk.PhotoImage(img_btn1)
        
        #====================== Lấy danh sách nhãn
        label_array = []
        path = 'data/test'
        for _, dirnames, filenames in os.walk(path):
            label_array=dirnames
            break
        
        
        main_frame = Frame(bg_img, bd=2, bg="white")#main frame
        main_frame.place(x=24, y=90, width=1200, height=650)
        
        #================================================================================================================
        #================================================================================================================
        # Frame bên phải chứa bảng dữ liệu và chức năng lịch sử train data
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",font=("times new roman",12,"bold"))
        Left_frame.place(x=15,y=50,width=500, height=550)
        
        train_path = "data/train/"
        val_path = "data/validation"
        test_path = "data/test"

        train_num = 0
        test_num=0
        for _, dirnames, filenames in os.walk(train_path):
            train_num += len(filenames)
        for _, dirnames, filenames in os.walk(val_path):
            train_num += len(filenames)

        for _, dirnames, filenames in os.walk(test_path):
            test_num += len(filenames)
            
        lastTrained = os.path.getmtime('model_cv.h5')
        modifiedTime = strftime('%Y-%m-%d %H:%M:%S', localtime(lastTrained))
        
        train_name_lb = Label(Left_frame, text="Số mẫu đã train: ",  font=("times new roman", 13, "bold"), bg="white")
        train_num_lb = Label(Left_frame, text=train_num,  font=("times new roman", 13, "bold"), bg="white" )
        train_name_lb.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        train_num_lb.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        
        test_name_lb = Label(Left_frame, text="Số mẫu đã test: ",  font=("times new roman", 13, "bold"), bg="white")
        test_num_lb = Label(Left_frame, text=test_num,  font=("times new roman", 13, "bold"), bg="white" )
        test_name_lb.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        test_num_lb.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        time_name_lb = Label(Left_frame, text="Lần cuối train dữ liệu: ",  font=("times new roman", 13, "bold"), bg="white")
        time_num_lb = Label(Left_frame, text=modifiedTime,  font=("times new roman", 13, "bold"), bg="white" )
        time_name_lb.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        time_num_lb.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        #================================================================================================================
        #================================================================================================================
        #rigth_label thống kê nhãn và mẫu
        Right_frame = LabelFrame(main_frame, bd=2, bg="white",
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=515, y=50, width=610, height=550)
        
        #Tìm kiếm
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Danh sách các mẫu",
                                         font=("times new roman", 11, "bold"))
        search_frame.place(x=5, y=5, width=600, height=70)
        
        
        self.var_search = StringVar()#Chữ cần tìm kiếm
        searchlabel = Label(search_frame, text="Chọn nhãn : ",  font=("times new roman", 12, "bold"), bg="white", fg="red2")
        searchlabel.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search, font=("times new roman", 12, "normal"), state="readonly",
                                    width=20)
        search_combo["values"] = label_array
        search_combo.current(0)
        search_combo.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
            
        #Nút tìm kiếm
        img_btn3 = PIL.Image.open(r"Image\btnRed.png")#ảnh nền màu đỏ
        img_btn3 = img_btn3.resize((105, 35), PIL.Image.ANTIALIAS)#resize ảnh
        self.photobtn3 = ImageTk.PhotoImage(img_btn3)#convert ảnh dạng ImageTk để truyền vào Button
       
        #nút tìm kiếm
        search_btn = Button(search_frame, text="Tìm kiếm", font=("times new roman", 11, "bold"),command=self.search_data,bd=0,bg="white",cursor='hand2' ,activebackground='white',
                        width=105,image=self.photobtn3,fg="white",compound="center")
        search_btn.grid(row=0, column=2,padx=4)

        #nút xem tất cả
        showAll_btn = Button(search_frame, text="Xem tất cả", font=("times new roman", 11, "bold"), command=self.fetch_data,bd=0,bg="white",cursor='hand2' ,activebackground='white',
                        width=105,image=self.photobtn3,fg="white",compound="center")
        showAll_btn.grid(row=0, column=3,padx=4)
        
        
        #Bảng dữ liệu
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=85, width=600, height=455)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
         #các trường dữ liệu
        self.label_table=ttk.Treeview(table_frame,column=("id", "label", "numOfSam"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.label_table.xview)
        scroll_y.config(command=self.label_table.yview)
        
        
        #đặt tên các cột dữ liệu
        self.label_table.heading("id", text="STT")
        self.label_table.heading("label", text="Tên nhãn")
        self.label_table.heading("numOfSam", text="Số lượng mẫu")
        self.label_table["show"]="headings"
        
        
        #độ dài các cột
        self.label_table.column("id", width=50)
        self.label_table.column("label", width=70)
        self.label_table.column("numOfSam", width=180)
        self.label_table.pack(fill=BOTH,expand=1)
        self.fetch_data()#load du lieu len bảng
     
     
    def search_data(self):
        self.label_table.delete(*self.label_table.get_children()) #xóa dữ liệu cũ
        index=1
        count=0
        directory1 = f"data/train/{self.var_search.get()}"
        directory2 = f"data/test/{self.var_search.get()}"
        directory3 = f"data/validation/{self.var_search.get()}"
        file_names1 = os.listdir(directory1)
        file_names2 = os.listdir(directory2)
        file_names3 = os.listdir(directory3)
        for f in file_names1:
            count+=1
        for f in file_names2:
            count+=1
        for f in file_names3:
            count+=1
        self.label_table.insert("", END, values=(index, self.var_search.get(),  count))
        
    def fetch_data(self):
        self.label_table.delete(*self.label_table.get_children()) #xóa dữ liệu cũ
        
        
        label_array = []
        path = 'data/test/'
        for _, dirnames, filenames in os.walk(path):
            label_array=dirnames
            break
            #============ Lấy danh sách nhãn bằng tên các folder trong thư mục
        index = 1
        for i in label_array:
            count = 0
            directory1 = f"data/train/{i}"
            directory2 = f"data/test/{i}"
            directory3 = f"data/validation/{i}"
            file_names1 = os.listdir(directory1)
            file_names2 = os.listdir(directory2)
            file_names3 = os.listdir(directory3)
            for f in file_names1:
                count+=1
            for f in file_names2:
                count+=1
            for f in file_names3:
                count+=1
            self.label_table.insert("", END, values=(index, i,  count))
            index+=1
        
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao

    obj=Report(root)
    root.mainloop()# cua so hien len