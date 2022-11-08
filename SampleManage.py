from PIL import Image, ImageTk
import os
import shutil
from time import strftime
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

import PIL.Image
from PIL import Image, ImageTk

from ShowSample import ShowSample, label_id


class Sample:
    def __init__(self,root):
        self.root=root
        w = 1250  # chiều dài giao diện
        h = 766  # chiều rộng giao diện

        ws = self.root.winfo_screenwidth()  # độ dài màn hình
        hs = self.root.winfo_screenheight()  # độ rộng màn
        x = (ws / 2) - (w / 2)  # vị trí cách lề trái x px
        y = (hs / 2) - (h / 2)  # vị trí cách lề trên y px

        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))  # kích thước và vị trí hiển thị giao diện
        self.root.title("Quản lý mẫu")
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
        self.txt = "Quản lý mẫu"#tiêu đề
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
        self.var_label = StringVar()
        self.var_location = StringVar()
        
        main_frame = Frame(bg_img, bd=2, bg="white")#main frame
        main_frame.place(x=24, y=90, width=1200, height=650)
        
        #================================================================================================================
        #================================================================================================================
        # Frame bên phải chứa bảng dữ liệu và chức năng tìm kiếm
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
        # table_label = Label(main_frame, text="Danh sách các nhãn",  font=("times new roman", 20, "bold"), bg="white")
        # table_label.grid(row=0, column=0, padx=800,pady=50, sticky=W)
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=85, width=600, height=455)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
         #các trường dữ liệu
        self.label_table=ttk.Treeview(table_frame,column=("id", "name", "location"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.label_table.xview)
        scroll_y.config(command=self.label_table.yview)
        
        
        #đặt tên các cột dữ liệu
        self.label_table.heading("id", text="STT")
        self.label_table.heading("name", text="Tên ảnh")
        self.label_table.heading("location", text="Đường dẫn ảnh")
        self.label_table["show"]="headings"
        
        
        #độ dài các cột
        self.label_table.column("id", width=50)
        self.label_table.column("name", width=70)
        self.label_table.column("location", width=180)
        self.label_table.pack(fill=BOTH,expand=1)
        self.label_table.bind("<ButtonRelease>",self.get_cursor)#sự kiện khi click vào bảng các thông tin in ra các txtbox
        self.fetch_data()#load du lieu len bảng
        
        
        #================================================================================================================
        #================================================================================================================
        #left_label
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",font=("times new roman",12,"bold"))
        Left_frame.place(x=15,y=50,width=500, height=550)
        
        #Frame thông tin mẫu
        sample_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Xử lí thông tin mẫu",
                                font=("times new roman", 12, "bold"))
        sample_frame.place(x=5, y=7, width=480, height=540)
        
        Labelname = Label(sample_frame, text="Tên nhãn : ",  font=("times new roman", 13, "bold"), bg="white")
        Labelname.grid(row=1, column=0, padx=15, sticky=W)
        label_combo = ttk.Combobox(sample_frame, textvariable=self.var_label, font=("times new roman", 13, "normal"), state="readonly",
                                    width=28)
        label_combo["values"] = label_array
        label_combo.current(0)
        label_combo.grid(row=1, column=1, padx=15, pady=10, sticky=W)
        
        
        locationlabel = Label(sample_frame, text="Đường dẫn : ",  font=("times new roman", 13, "bold"), bg="white")
        locationlabel.grid(row=3, column=0, padx=15, sticky=W)
        self.locationname_entry=Entry(sample_frame,width=30,textvariable=self.var_location, font=("times new roman", 13, "normal"))
        self.locationname_entry.grid(row=3,column=1,padx=15,sticky=W)
        
        
        #==============================================================================================================
        #==============================================================================================================
        #===========Button quản lý mẫu===================================================================================================
        
        #Button them
        btnImport=Button(sample_frame,text="Import mẫu",command = lambda:self.upload_file(label_combo.get()),font=("times new roman",11,"bold"),bd=0,bg="white",cursor='hand2' ,activebackground='white',
                        width=115,image=self.photobtn1,fg="white",compound="center")
        btnImport.place(x=50, y=120)
    
        #Button xem anh
        btnShow=Button(sample_frame,text="Xem mẫu",command = lambda:self.show_file(label_combo.get()),font=("times new roman",11,"bold"),bd=0,bg="white",cursor='hand2' ,activebackground='white',
                        width=115,image=self.photobtn1,fg="white",compound="center")
        btnShow.place(x=250, y=120)
        
        #button xóa
        btndelete=Button(sample_frame,text="Xóa mẫu",command = self.deletesample,font=("times new roman",11,"bold"),bd=0,bg="white",cursor='hand2' ,activebackground='white',
                        width=115,image=self.photobtn1,fg="white",compound="center")
        btndelete.place(x=50, y=200)

        #button reset
        btnsave=Button(sample_frame,text="Làm mới",command =self.updatesample,font=("times new roman",11,"bold"),bd=0,bg="white",cursor='hand2' ,activebackground='white',
                        width=115,image=self.photobtn1,fg="white",compound="center")
        btnsave.place(x=250, y=200)
        
  
   
    
    def deletesample(self):
        if(self.locationname_entry.get() == ""):
            messagebox.showerror("Chọn mẫu", "Chọn mẫu để xóa", parent=self.root)
        else  :
            Exit = messagebox.askyesno("Xóa ảnh", "Bạn có chắc chắn muốn xóa ảnh này?", parent=self.root)
            if (Exit > 0):
                os.remove(self.locationname_entry.get())
                messagebox.showinfo("Thông báo", f"Bạn vừa xóa ảnh thành công.", parent=self.root)
                print("Bạn vừa xóa ảnh" + self.locationname_entry.get())
            else:
                if not Exit:
                    return
    
    def updatesample(self):
        self.label_table.delete(*self.label_table.get_children()) #xóa dữ liệu cũ
        index=1
        
        directory1 = f"data/train/{self.var_search.get()}"
        directory2 = f"data/test/{self.var_search.get()}"
        directory3 = f"data/validation/{self.var_search.get()}"
        file_names1 = os.listdir(directory1)
        file_names2 = os.listdir(directory2)
        file_names3 = os.listdir(directory3)
        for f in file_names1:
            full_path = os.path.join(directory1, f)
            self.label_table.insert("", END, values=(index, f, full_path))
            index+=1
        for f in file_names2:
            full_path = os.path.join(directory1, f)
            self.label_table.insert("", END, values=(index, f,  full_path))
            index+=1
        for f in file_names3:
            full_path = os.path.join(directory1, f)
            self.label_table.insert("", END, values=(index, f, full_path))
            index+=1
        
                
    
    def show_file(self, lb):
        label_id(lb)
        self.new_window = Toplevel(self.root)
        self.app = ShowSample(self.new_window)
    
    def upload_file(self, lb):
        f_types = (('{PNG Files', '*.png'), ('All Files', '*.*'))
        filename = filedialog.askopenfiles(multiple=True,filetypes=f_types)
        count = 0
        for f in filename:
            try:
                print(f.name)
                shutil.move(f.name, "data/train/"+lb ) 
            except PermissionError:
                print('as expected')
            count+=1
        messagebox.showinfo("Import sample", f"Bạn đã tải lên {count} mẫu")
        
    def search_data(self):
        self.label_table.delete(*self.label_table.get_children()) #xóa dữ liệu cũ
        index=1
        
        directory1 = f"data/train/{self.var_search.get()}"
        directory2 = f"data/test/{self.var_search.get()}"
        directory3 = f"data/validation/{self.var_search.get()}"
        file_names1 = os.listdir(directory1)
        file_names2 = os.listdir(directory2)
        file_names3 = os.listdir(directory3)
        for f in file_names1:
            full_path = os.path.join(directory1, f)
            self.label_table.insert("", END, values=(index, f, full_path))
            index+=1
        for f in file_names2:
            full_path = os.path.join(directory1, f)
            self.label_table.insert("", END, values=(index, f,  full_path))
            index+=1
        for f in file_names3:
            full_path = os.path.join(directory1, f)
            self.label_table.insert("", END, values=(index, f, full_path))
            index+=1
        
                
        
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
            directory1 = f"data/train/{i}"
            directory2 = f"data/test/{i}"
            directory3 = f"data/validation/{i}"
            file_names1 = os.listdir(directory1)
            file_names2 = os.listdir(directory2)
            file_names3 = os.listdir(directory3)
            for f in file_names1:
                full_path = os.path.join(directory1, f)
                self.label_table.insert("", END, values=(index, f,  full_path))
            for f in file_names2:
                full_path = os.path.join(directory1, f)
                self.label_table.insert("", END, values=(index, f,  full_path))
            for f in file_names3:
                full_path = os.path.join(directory1, f)
                self.label_table.insert("", END, values=(index, f,  full_path))
            index+=1
        
    def get_cursor(self,event=""):#Sự kiện khi click vào bảng thì hiện chi tiết thông tin ra các txtbox
        cursor_focus=self.label_table.focus()
        content=self.label_table.item(cursor_focus)
        data=content["values"]
        self.var_label.set(self.var_search.get()),
        self.var_location.set(data[2]),
        
        
                
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao

    obj=Sample(root)
    root.mainloop()# cua so hien len