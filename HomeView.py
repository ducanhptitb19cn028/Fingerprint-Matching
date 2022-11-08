import random
import time
from datetime import *
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

from LabelManage import Labell
from ReportData import Report
from SampleManage import Sample
from TrainView import Train

value_from_p1 = None

def new_print(value):
    global value_from_p1
    value_from_p1 = value
    print(value_from_p1)


class Home(Toplevel):
    def __init__(self, window):
        Toplevel.__init__(self)
        img = ImageTk.PhotoImage \
            (file='Image\\admin_frame.png')
        self.window = window
        self.geometry("1366x720+0+0")
        self.title("Hệ thống kiểm tra an ninh bằng vân tay")
        self.iconbitmap('Image\\gaming.ico')
        self.resizable(False, False)
        self.admin_dashboard_frame = ImageTk.PhotoImage \
            (file='Image\\admin_frame.png')
        self.image_panel = Label(self, image=self.admin_dashboard_frame)
        self.image_panel.pack(fill='both', expand='yes')
        
        self.txt = "Hệ thống kiểm tra an ninh"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self, text=self.txt, font=('times new roman', 28, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=375, y=65, width=550)
        
        # ========================================================================
        # ============================Date and time==============================
        # ========================================================================
        self.clock_image = ImageTk.PhotoImage(file="Image/time.png")
        self.date_time_image = Label(self, image=self.clock_image, bg="white")
        self.date_time_image.place(x=35, y=65)

        self.date_time = Label(self)
        self.date_time.place(x=65, y=65)
        self.time_running()
        
        # ========================================================================
        # ============================Home button===============================
        # ========================================================================
        self.home = ImageTk.PhotoImage \
            (file='Image\\home.png')
        self.home_button = Button(self, image=self.home,
                                    font=("times new roman", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_home)

        self.home_button.place(x=41, y=200)
    
        
        
        # ========================================================================
        # ============================Manage button===============================
        # ========================================================================
        self.manage = ImageTk.PhotoImage \
            (file='Image\\manage.png')
        self.manage_button = Button(self, image=self.manage,
                                    font=("times new roman", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_manage)

        self.manage_button.place(x=41, y=355)
    
        
        # ========================================================================
        # ============================Exit button===============================
        # ========================================================================
        self.exit = ImageTk.PhotoImage \
            (file='Image\\exit_button.png')
        self.exit_button = Button(self, image=self.exit,
                                  font=("times new roman", 13, "bold"), relief=FLAT, activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", command=self.click_exit)
        self.exit_button.place(x=41, y=505)
        
        # ========================================================================
        # ============================Logout button===============================
        # ========================================================================
        self.logout = ImageTk.PhotoImage \
            (file='Image\\logout.png')
        self.logout_button = Button(self, image=self.logout,
                                    font=("times new roman", 13, "bold"), relief=FLAT, activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2", command=self.click_logout)
        self.logout_button.place(x=1241, y=70)
    
    def click_home(self):
        print("Hi")
    
        
    def click_manage(self):
        """ opens new frame from where one can go to manage label, sample"""
        manage_frame = Frame(self, bg="white")
        manage_frame.place(x=155, y=120, height=535, width=1190)

        self.manage_dashboard_frame = ImageTk.PhotoImage \
            (file='Image\\manage_frame.png')
        self.manage_panel = Label(manage_frame, image=self.manage_dashboard_frame, bg="white")
        self.manage_panel.pack(fill='both', expand='yes')

        # =============Button================
        #nút quản lý nhãn
        img_btn1 = Image.open(r"Image\student2.png")
        # img_btn1 = img_btn1.resize((60, 88), Image.LANCZOS)
        self.photobtn1 = ImageTk.PhotoImage(img_btn1)

        button_labell = Button(manage_frame, text="Quản lý nhãn", font=("times new roman", 14, "bold"), command=self.labell_details,
                    image=self.photobtn1, cursor="hand2",
                    activebackground="white", bg="white", borderwidth=0, compound="top")
        button_labell.place(x=327, y=97, width=135, height=135)

        #nút quản lý mẫu
        img_btn2 = Image.open(r"Image\ghichu.png")
        # img_btn2 = img_btn2.resize((60, 88), Image.ANTIALIAS)
        self.photobtn2 = ImageTk.PhotoImage(img_btn2)

        button_att = Button(manage_frame, text="Quản lý mẫu", font=("times new roman", 14, "bold"),
                                command=self.sample_details,
                                image=self.photobtn2, cursor="hand2",
                                activebackground="white", bg="white", borderwidth=0, compound="top")
        button_att.place(x=717, y=97, width=135, height=135)

        
        #nút train
        img_btn3 = Image.open(r"Image\train.png")
        # img_btn2 = img_btn2.resize((60, 88), Image.ANTIALIAS)
        self.photobtn3 = ImageTk.PhotoImage(img_btn3)

        button_att = Button(manage_frame, text="Train", font=("times new roman", 14, "bold"),
                                command=self.train,
                                image=self.photobtn3, cursor="hand2",
                                activebackground="white", bg="white", borderwidth=0, compound="top")
        button_att.place(x=325, y=315, width=135, height=135)


        #nút thống kê hệ thống
        img_btn4 = Image.open(r"Image\report.png")
        # img_btn4 = img_btn4.resize((60, 88), Image.ANTIALIAS)
        self.photobtn4 = ImageTk.PhotoImage(img_btn4)

        button_att = Button(manage_frame, text="Thống kê", font=("times new roman", 14, "bold"),
                            command=self.report_data,
                            image=self.photobtn4, cursor="hand2",
                            activebackground="white", bg="white", borderwidth=0, compound="top")
        button_att.place(x=717, y=315, width=135, height=135)
    

    
    def click_exit(self):
        self.deiconify()
        ask = messagebox.askyesnocancel("Xác nhận thoát", "Bạn chắc chắn muốn đóng chương trình?", parent=self)
        if ask is True:
            self.quit()
    
    def click_logout(self):
        """Logouts the user to login page from where they will require password in order to login again"""
        Exit = messagebox.askyesno("Đăng xuất", "Bạn có chắc chắn muốn đăng xuất không?", parent=self)
        if (Exit > 0):
            self.destroy()
            self.window.show()
        else:
            if not Exit:
                return


    def labell_details(self):
        self.new_window=Toplevel(self)
        self.app=Labell(self.new_window)
    
    def sample_details(self):
        self.new_window=Toplevel(self)
        self.app=Sample(self.new_window)
    
    def report_data(self):
        self.new_window=Toplevel(self)
        self.app=Report(self.new_window)
    
    def train(self):
        self.new_window=Toplevel(self)
        self.app=Train(self.new_window)
        
    def time_running(self):
        """ displays the current date and time which is shown at top left corner of admin dashboard"""
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%d/%m/%Y')
        concated_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=concated_text, font=("times new roman", 13, "bold"), relief=FLAT
                                 , borderwidth=0, background="white", foreground="black")
        self.date_time.after(100, self.time_running)

    def slider(self):
        if self.count >= len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)

        else:
            self.text = self.text + self.txt[self.count]
            self.heading.config(text=self.text)
        self.count += 1

        self.heading.after(100, self.slider)

    def heading_color(self):
       
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

if __name__ == '__main__':
    window = Tk()  # khoi tao cua so va gan root vao
    obj = Home(window)
    window.mainloop()  # cua so hien len

