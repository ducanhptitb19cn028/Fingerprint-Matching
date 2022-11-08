from time import strftime
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

from HomeView import Home


class LoginPage(object):
    # hàm khởi tạo giao diện
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')#kích thước giao diện
        self.window.resizable(0, 0) #ko cho giao diện thu nhỏ
        self.window.state('zoomed') #giao diện hiển thị toàn màn hình
        self.window.title('Đăng nhập hệ thống') #tiêu đề của cửa sổ app
        self.window.iconbitmap("Image\\gaming.ico")
        today = strftime("%d-%m-%Y")  # thời gian ngày-tháng-năm

        # =============biến kiểu string email,password============
        self.var_email = StringVar()
        self.var_password = StringVar()

        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open("Image\\background1.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)#Khai báo biến bg_panel chứa ảnh photo
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')#Vị trí của lớp Label : chính giữa giao diện
        # ====== Login Frame =========================

        self.lgn_frame = Frame(self.window, bg='#15233c', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ======Hiện thị ngày====
        self.txt = today
        self.heading = Label(self.lgn_frame, text=self.txt, font=('times new roman', 25, "bold"), bg="#15233c",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('Image\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#15233c')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('Image\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#15233c')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Đăng nhập", bg="#15233c", fg="white",
                                    font=("times new roman", 17, "bold"))
        self.sign_in_label.place(x=630, y=240)

        # ========================================================================
        # ============================tài khoản====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Tài khoản", bg="#15233c", fg="white",
                                    font=("times new roman", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.txtuser = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#15233c", fg="#6b6a69",
                                    font=("times new roman ", 12, "bold"),textvariable=self.var_email)
        self.txtuser.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('Image\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#15233c')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================Nút đăng nhập================================
        # ========================================================================
        self.lgn_button = Image.open('Image\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#15233c')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='Đăng nhập',command=self.login,
                            font=("times new roman", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=20, y=10)


       

        # ========================================================================
        # ============================Mật khẩu====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Mật khẩu", bg="#15233c", fg="white",
                                    font=("times new roman", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.txtpass = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#15233c", fg="white",
                                    font=("times new roman", 12, "bold"), show="*",textvariable=self.var_password)
        self.txtpass.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('Image\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#15233c')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        #ảnh nút hiển thị password
        self.show_image = ImageTk.PhotoImage \
            (file='Image\\show.png')

        #ảnh  nút ẩn password
        self.hide_image = ImageTk.PhotoImage \
            (file='Image\\hide.png')

        #nút hiển thị password
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.showpass, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def showpass(self):#hàm hiển thị mật khẩu
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.txtpass.config(show='')
    def show(self):
        """"""
        self.window.update()
        self.window.deiconify()
    def hide(self):#hàm ẩn mật khẩu dưới dạng ***
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.showpass, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.txtpass.config(show='*')

    #reset thông tin password_tài khoản
    def reset(self):
        self.var_email.set("")
        self.var_password.set("")
        self.varcheck.set(0)

    # hàm đăng nhập
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Lỗi !!","Vui lòng nhập đầy đủ thông tin")
        else :
            if self.txtuser.get()!="admin" or self.txtpass.get()!="123456":
                    messagebox.showerror("Lỗi", "Sai tên đăng nhập, mật khẩu hoặc quyền đăng nhập")
            else:
                messagebox.showinfo("Thông báo","Bạn đã đăng nhập thành công với quyền Admin")
                self.window.withdraw()
                self.app = Home(self)
      



if __name__ == '__main__':
    window = Tk()  # tạo giao diện tkinter Tk() và gán nó vào biến window
    obj = LoginPage(window)
    window.mainloop()  # hiển thị giao diện và bắt đầu nhận các sự kiện để xử lý.