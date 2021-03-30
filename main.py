from tkinter import *
from tkinter.tix import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil
from database import Account


color1 = '#BB8B6A';
font = ('Calibri', 13)
font_bold = ('Calibri', 13, 'bold')
font_big_bold = ('Calibri', 15, 'bold')


# Textfile to save load users
users = {}

class LoginScreen(Tk):

    def __init__(self):
        Tk.__init__(self)

        # root = Tk()
        self.title("Grade Manager")
        self.geometry("1100x670")
        self.resizable(False, False)

        # Background Image
        self.img = Image.open('bg.jpg')
        self.bg_img = self.img.resize((1100, 670), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg = Label(self, image=self.bg_img)
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.admin = Account('admin')
        self.login_page()



    def login_page(self):

        self.admin.create_login('login')
        logins = self.admin.load_login('login')
        if logins:
            self.users = logins
        else:
            self.users = {}


        # Login Frame
        self.login_frame = Frame(self, bg='white')
        self.login_frame.place(x=150, y=150, height=360, width=420)

        title = Label(self.login_frame, text="Login", bg='white', fg=color1, font=('Calibri', 30, 'bold'))
        title.place(x=60, y=10)
        desc = Label(self.login_frame, text="Login to view your account", bg='white', fg=color1, font=('Calibri', 13))
        desc.place(x=60, y=60)

        lbl_user = Label(self.login_frame, text="Username", bg='white', fg=color1, font=('Calibri', 13))
        lbl_user.place(x=60, y=120)
        self.txt_user = Entry(self.login_frame, bg='#FEF9F5', font=('Calibri', 13))
        self.txt_user.place(x=60, y=150, width=300, height=35)

        lbl_pass = Label(self.login_frame, text="Password", bg='white', fg=color1, font=('Calibri', 13))
        lbl_pass.place(x=60, y=190)
        self.txt_pass = Entry(self.login_frame, bg='#FEF9F5', font=('Calibri', 13), show='*')
        self.txt_pass.place(x=60, y=220, width=300, height=35)

        self.btn_reg = Button(self.login_frame, text="Need an account?", bg='white', fg='#BB8B6A', border=0, font=('Calibri', 11), cursor='hand2', command=self.signup_press)
        self.btn_reg.place(x=60, y=260, width=110, height=20)

        self.btn_login = Button(self.login_frame, text='Login', bg='#BB8B6A', fg='white', border=0, font=('Calibri', 13),
                                activebackground='black', activeforeground='white', cursor='hand2', command=self.login)
        self.btn_login.place(x=60, y=285, width=300, height=40)


    def login(self):
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror('Error', 'All fields are required', parent=self)
        elif self.txt_user.get() not in self.users:
            messagebox.showerror('Error', 'User doesn\'t exist', parent=self)
        elif self.txt_pass.get() != self.users[self.txt_user.get()]:
            messagebox.showerror('Error', 'Invalid password', parent=self)
        else:
            global loginScr
            loginScr = self
            self.admin.db.close()
            self.withdraw()                     # .deiconify to undo
            MainScreen.username = self.txt_user.get()
            app = MainScreen()


    def register_page(self):

        # Register Frame
        self.register_frame = Frame(self, bg='white')
        self.register_frame.place(x=150, y=20, height=620, width=400)


        title = Label(self.register_frame, text="Register", bg='white', fg=color1, font=('Calibri', 30, 'bold'))
        title.place(x=50, y=10)
        desc = Label(self.register_frame, text="Type in details to register new user", bg='white', fg=color1, font=('Calibri', 13))
        desc.place(x=50, y=60)

        lbl_fname = Label(self.register_frame, text="Firstname", bg='white', fg=color1, font=('Calibri', 13))
        lbl_fname.place(x=50, y=120)
        self.reg_txt_fname = Entry(self.register_frame, bg='#FEF9F5', font=('Calibri', 13))
        self.reg_txt_fname.place(x=50, y=150, width=300, height=35)

        lbl_lname = Label(self.register_frame, text="Lastname", bg='white', fg=color1, font=('Calibri', 13))
        lbl_lname.place(x=50, y=190)
        self.reg_txt_lname = Entry(self.register_frame, bg='#FEF9F5', font=('Calibri', 13))
        self.reg_txt_lname.place(x=50, y=220, width=300, height=35)

        lbl_matric = Label(self.register_frame, text="Matric. no.", bg='white', fg=color1, font=('Calibri', 13))
        lbl_matric.place(x=50, y=260)
        self.reg_txt_matric = Entry(self.register_frame, bg='#FEF9F5', font=('Calibri', 13))
        self.reg_txt_matric.place(x=50, y=290, width=300, height=35)

        lbl_user = Label(self.register_frame, text="Username", bg='white', fg=color1, font=('Calibri', 13))
        lbl_user.place(x=50, y=330)
        self.reg_txt_user = Entry(self.register_frame, bg='#FEF9F5', font=('Calibri', 13))
        self.reg_txt_user.place(x=50, y=360, width=300, height=35)


        lbl_pass = Label(self.register_frame, text="Password", bg='white', fg=color1, font=('Calibri', 13))
        lbl_pass.place(x=50, y=400)
        self.reg_txt_pass = Entry(self.register_frame, bg='#FEF9F5', font=('Calibri', 13), show='*')
        self.reg_txt_pass.place(x=50, y=430, width=300, height=35)

        lbl_pass_confirm = Label(self.register_frame, text="Confirm Password", bg='white', fg=color1, font=('Calibri', 13))
        lbl_pass_confirm.place(x=50, y=470)
        self.reg_txt_pass_confirm = Entry(self.register_frame, bg='#FEF9F5', font=('Calibri', 13), show='*')
        self.reg_txt_pass_confirm.place(x=50, y=500, width=300, height=35)

        self.btn_log = Button(self.register_frame, text="Already have an account?", bg='white', fg='#BB8B6A', border=0,
                              font=('Calibri', 11), cursor='hand2', command=self.login_press)
        self.btn_log.place(x=50, y=540, width=170, height=20)

        self.btn_register = Button(self.register_frame, text='Register', bg=color1, fg='white', border=0,
                                               font=('Calibri', 13), cursor='hand2', command=self.register)
        self.btn_register.place(x=50, y=565, width=300, height=40)


    def signup_press(self):
        self.register_page()
        self.login_frame.destroy()

    def login_press(self):
        self.login_page()
        self.register_frame.destroy()

    def register(self):
        if self.reg_txt_user.get()=="" or self.reg_txt_pass.get()=="" or self.reg_txt_pass_confirm.get()=="" or self.reg_txt_lname.get()=="" or self.reg_txt_fname.get()=="" or self.reg_txt_matric.get()=="":
            messagebox.showerror('Error', 'All fields are required', parent=self)
        elif self.reg_txt_pass_confirm.get() != self.reg_txt_pass.get():
            messagebox.showerror('Error', 'Confirm password doesn\'t match', parent=self)
        elif self.reg_txt_user.get() in self.users:
            messagebox.showerror('Error', 'Username already exist', parent=self)
        else:
            username = self.reg_txt_user.get()
            fName = self.reg_txt_fname.get()
            lName = self.reg_txt_lname.get()
            matric = self.reg_txt_matric.get()
            password = self.reg_txt_pass.get()

            try:
                self.admin.create_login('login')
                self.admin.insert_login('login', username, password)    # save password to db

                self.acct = Account(username)       # initialize db
                self.acct.create_profile("profile")     # create profile table
                self.acct.insert_profile("profile", fName, "", lName, "", "", "", "", "", "", matric)
                self.acct.create_prog("programme")  # create programmes table
                self.acct.insert_prog("programme", "Software Engineering")
                self.acct.create("courses")         # create courses table
                self.acct.db.close()

                messagebox.showinfo('Successful', 'Registration successful! proceed to login', parent=self.master)
                self.login_press()
            except:
                messagebox.showerror('Error', 'Registration denied!', parent=self)



class MainScreen(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        username = self.username

        self.left_margin1 = 40
        self.left_margin2 = 230
        self.top_margin = 70
        self.bgcolor= '#FEF9F5'
        self.fgcolor = '#BB8B6A'
        self.fgcolorlight = '#EEDFD4'
        style = ttk.Style()
        style.configure("Avatar.TCombobox", foreground=self.fgcolor, background=self.bgcolor, bd=0)


        self.title("Account")
        self.geometry("1200x700")
        self.resizable(False, False)

        self.acct = Account(username)       # initialize database
        self.programme = self.acct.load_prog("programme")



        # self.menubar = self.menu_bar()    #adding menu bar
        # self.config(menu=self.menubar)

        # for paging
        nb = ttk.Notebook(self, width=1200, height=650)
        nb.pack()
        self.canvas_personal = Canvas(nb, width=500, height=500, bg=self.bgcolor)
        # canvas_programme = Canvas(nb, width=500, height=500, bg='brown')
        self.canvas_courses = Canvas(nb, width=500, height=500, bg=self.bgcolor)
        self.canvas_personal.pack(fill="both", expand=1)
        # canvas_programme.pack(fill="both", expand=1)
        self.canvas_courses.pack(fill="both", expand=1)

        # add Pages to Notebook
        nb.add(self.canvas_personal, text='  Personal  ')
        # nb.add(canvas_programme, text='  Programme  ')
        nb.add(self.canvas_courses, text='  Courses  ')

        # ======= PERSONAL ==========#
        self.details = self.acct.load_profile("profile")       # load profile from database                   #self.details = {
                                                                                                               # 'First Name':'Pune', 'Middle Name':'Mumbai', 'Surname':'Kutra',
                                                                                                               # 'Gender':'Male', 'Date of Birth':'01/11/2001', 'Nationality':'Indian',
                                                                                                               # 'Place of Birth':'Mumbai', 'Languages':'Hindi', 'Blood Group':'O+',
                                                                                                               # 'Matriculation Number':'UI/2020/CE/556'}

        self.total_rows = len(self.details)   # find total number of rows and
        self.total_columns = 2   # columns in list

        self.user = Label(self.canvas_personal, text=self.details['First Name']+' '+self.details['Surname'], font=font_bold, fg=self.fgcolor, bg=self.bgcolor)
        self.user.place(x=self.left_margin1, y=12)

        self.btn_logout = Button(self.canvas_personal, text="Logout", font=font, fg='black', bg=self.bgcolor, bd=0, cursor='hand2',
                                 activebackground=self.bgcolor, command=self.logout)
        self.btn_logout.place(x=1085, y=15, height=18)
        self.btn_logout.bind("<Enter>", self.hover_over)
        self.btn_logout.bind("<Leave>", self.leave)
        line = self.canvas_personal.create_line(self.left_margin1, 40, 1140, 40, width=2, fill=self.fgcolorlight)

        # profile picture #
        self.pic_frame = Frame(self.canvas_personal, cursor='hand2', highlightbackground=self.fgcolor,
                               highlightcolor=self.fgcolor, highlightthickness=3, bd=0)
        self.pic_frame.place(x=self.left_margin1, y=self.top_margin, width=150, height=150)
        self.load_pic(self.pic_frame)

        #--- details table ------
        head = Frame(self.canvas_personal, bg=self.fgcolor)
        table_head = Label(head, text='Personal Details', bg=self.fgcolor, fg=self.bgcolor, font=font_bold)
        table_head.place(x=4, y=0)
        head.place(x=self.left_margin2, y=self.top_margin, width=909, height=30)

        self.table_frame = Frame(self.canvas_personal, bg=self.bgcolor)
        self.table_frame.place(x=self.left_margin2, y=self.top_margin+30, width=910, height=500)
        self.load_details()

        #---- update profile form ------
        self.update_form = Frame(self.canvas_personal, bg=self.bgcolor)
        self.update_form.columnconfigure(0, weight=1)
        self.update_form.columnconfigure(1, weight=2)
        self.update_form.columnconfigure(2, weight=4)
        self.values_box = []
        for i in range(self.total_rows):
            self.update_form.rowconfigure(i, weight=1)
            var = StringVar()
            var.set(list(self.details.values())[i])
            lbl = Label(self.update_form, text=list(self.details.keys())[i], fg=self.fgcolor, bg=self.bgcolor, font=font)
            lbl.grid(row=i, column=0, padx=4, pady=3, sticky='e')
            if i==0 or i==2 or i==9:
                self.txtBox = Entry(self.update_form, textvariable=var, state='disabled', disabledbackground=self.bgcolor,
                                    fg=self.fgcolor, bg=self.bgcolor, font=font)
                self.txtBox.grid(row=i, column=1, padx=4, pady=3, sticky='nsew')
            elif i==3:
                keep = list(self.details.values())[i]
                self.txtBox = ttk.Combobox(self.update_form, textvariable=keep, state='readonly', font=font, style='Avatar.TCombobox')
                self.txtBox['values'] = ('Male', 'Female')
                self.txtBox.current(0)
                self.txtBox.grid(row=i, column=1, padx=4, pady=3, sticky='nsew')
            else:
                self.txtBox = Entry(self.update_form, textvariable=var, fg=self.fgcolor, bg=self.bgcolor, font=font)
                self.txtBox.grid(row=i, column=1, padx=4, pady=3, sticky='nsew')
            self.values_box.append(self.txtBox)
        self.btn_update = Button(self.canvas_personal, text="Update", font=font, fg=self.bgcolor, bg=self.fgcolor, bd=0,
                                 activebackground='black', activeforeground='white', cursor='hand2', command=self.update_profile)   # update button
        self.btn_cancel = Button(self.canvas_personal, text="Cancel", font=font, fg=self.fgcolor, bg=self.bgcolor, bd=1, activebackground='black',
                                activeforeground='white', cursor='hand2', command=self.cancel_profile_update)

        # Edit and Print Button
        self.btn_edit = Button(self.canvas_personal, text="Edit", font=font, fg=self.bgcolor, bg=self.fgcolor, bd=0,
                                 activebackground='black', activeforeground='white', cursor='hand2', command=self.edit)
        self.btn_edit.place(x=860, y=self.top_margin+500, height=25,  width=130)

        self.btn_print = Button(self.canvas_personal, text="Print", font=font, fg=self.fgcolor, bg=self.bgcolor, bd=1,
                                activebackground='black', activeforeground='white', cursor='hand2', command=self.print_profile)
        self.btn_print.place(x=1000, y=self.top_margin+500, height=25, width=130)


        # ======= COURSES ==========#

        self.courses = self.acct.load("courses")          # load courses from db                   # self.courses = {
                                                                                                        #     'MTH101':['Mathematics', '40hrs', '85'],
                                                                                                        #     'ENG121':['English Study', '20hrs', '75'],
                                                                                                        #     'PHY111':['Physics', '30hrs', '92'],
                                                                                                        #     'DSN 101':['Designs, Implentations and Documentation', '40hrs', '78'],
                                                                                                        #     'GST131':['General Knowledge', '10hrs', '37'],
                                                                                                        #     'TED111':['Technical Drawing', '40hrs', '44'],
        if self.courses:                                                                                                # }
            self.keys = len(self.courses)
        else:
            self.keys = 0
            self.courses = {}

        self.user = Label(self.canvas_courses, text=self.details['First Name']+' '+self.details['Surname'], font=font_bold, fg=self.fgcolor, bg=self.bgcolor)
        self.user.place(x=self.left_margin1, y=12)

        lbl_program = Label(self.canvas_courses, text="Programme:", font=font_bold, fg=self.fgcolor, bg=self.bgcolor)
        lbl_program.place(x=650, y=12)

        self.prog = StringVar()
        self.prog.set(self.programme)
        self.box_program = ttk.Combobox(self.canvas_courses, textvariable=self.prog, state='readonly', font=font, style='Avatar.TCombobox')
        self.box_program['values'] = ('Software Engineering', 'Computer Engineering', 'Electrical/Electronics')
        # self.box_program.current(0)
        self.box_program.bind('<<ComboboxSelected>>', self.on_prog_change)
        self.box_program.place(x=750, y=12)

        self.btn_logout = Button(self.canvas_courses, text="Logout", font=font, fg='black', bg=self.bgcolor, bd=0, cursor='hand2',
                                 activebackground=self.bgcolor, command=self.logout)
        self.btn_logout.place(x=1085, y=15, height=18)
        self.btn_logout.bind("<Enter>", self.hover_over)
        self.btn_logout.bind("<Leave>", self.leave)

        line = self.canvas_courses.create_line(self.left_margin1, 42, 1140, 42, width=2, fill=self.fgcolorlight)

        #--- Courses table ------
        head = Frame(self.canvas_courses, bg=self.fgcolor)
        table_head = Label(head, text='Courses Details', bg=self.fgcolor, fg=self.bgcolor, font=font_bold)
        table_head.place(x=4, y=0)
        head_details = Label(self.canvas_courses, text=' Code\t\t            Title \t\t\t\t            Credit Hour\t\t   Score\t\t             Grade\t\t   ',
                             bg=self.fgcolorlight, fg=self.fgcolor, font=font_bold)
        head_details.place(x=self.left_margin1, y=self.top_margin+30)
        head.place(x=self.left_margin1, y=self.top_margin, width=1100, height=30)

        self.courses_frame = Frame(self.canvas_courses, bg=self.bgcolor)
        self.load_courses()
        self.courses_frame.place(x=self.left_margin1, y=self.top_margin+60, width=1100, height=500)

        self.courses_box = []


    # load profile picture
    def load_pic(self, frame):
        self.acct.create_photo('photo')
        data = self.acct.load_photo('photo')
        if data and os.path.isfile('profile.jpg'):
            with open('profile.jpg', 'wb') as file:
                file.write(data)
            self.img = Image.open('profile.jpg')
        else:
            self.img = Image.open('default.jpg')

        self.bg_img = self.img.resize((150, 150), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.profile_pic = Label(frame, image=self.bg_img)
        self.profile_pic.place(x=0, y=0, relwidth=1, relheight=1)
        self.profile_pic.bind('<Button-1>', self.change_pic)
        # add tiptool
        tip = Balloon(frame)
        tip.subwidget('label')['image'] = BitmapImage()     #removes arrow on tiptool
        tip.bind_widget(self.profile_pic, balloonmsg="Click to change")


    def load_details(self):
        for i in range(self.total_rows):
            for j in range(self.total_columns):

                if j == 1:
                    self.e = Entry(self.table_frame, width=50, fg=self.fgcolor, bg=self.bgcolor, font=font, highlightbackground=self.fgcolorlight,
                                   highlightcolor=self.fgcolorlight, highlightthickness=1, bd=0)
                    self.e.grid(row=i, column=j, ipady=5)
                    self.e.bind("<Button>", lambda a: "break")      # make entry box unselectable
                    self.e.insert(END, ' '+list(self.details.values())[i])
                else:
                    self.e = Entry(self.table_frame, width=50, fg=self.fgcolor, bg='#F4EDE8', font=font, highlightbackground=self.fgcolorlight,
                                   highlightcolor=self.fgcolorlight, highlightthickness=1, bd=0)
                    self.e.grid(row=i, column=j, ipady=5)
                    self.e.bind("<Button>", lambda a: "break")      # make entry box unselectable
                    self.e.insert(END, ' '+list(self.details.keys())[i])

    def on_prog_change(self, e):
        program = self.box_program.get()
        self.acct.update_prog("programme", program)


    def change_pic(self, e):
        src_dir = os.getcwd()
        try:
            self.filename = filedialog.askopenfilename(initialdir=src_dir, title='Select a file', filetypes=(("png", "*.png"),("jpg", "*.jpg"),("jpeg", "*.jpeg")))
            shutil.copy(self.filename, 'profile.jpg')   # copying photo to root folder

            # saving photo to db
            with open('profile.jpg', 'rb') as file:
                blobData = file.read()
            self.acct.create_photo('photo')
            self.acct.insert_photo('photo', blobData)

            self.avatar = 1
            self.load_pic(self.pic_frame)
        except:
            messagebox.showerror('Error', 'Failed to change profile picture!', parent=self)


    def load_courses(self):

        print(self.keys)
        for i in range(self.keys):
            for j in range(2):
                if j == 0:
                    self.e = Entry(self.courses_frame, width=20, fg=self.fgcolor, bg=self.bgcolor, font=font, highlightbackground=self.fgcolorlight,
                                   highlightcolor=self.fgcolorlight, highlightthickness=1, bd=0)
                    self.e.grid(row=i, column=j, ipady=5)
                    self.e.bind("<Button>", lambda a: "break")      # make entry box unselectable
                    self.e.insert(END, ' '+list(self.courses.keys())[i])
                else:
                    for v in range(3):
                        if v==0:
                            self.e = Entry(self.courses_frame, width=40, fg=self.fgcolor, bg='#F4EDE8', font=font, highlightbackground=self.fgcolorlight,
                                           highlightcolor=self.fgcolorlight, highlightthickness=1, bd=0)     # make course name column wider (width:40)
                        else:
                            self.e = Entry(self.courses_frame, width=20, fg=self.fgcolor, bg='#F4EDE8', font=font, highlightbackground=self.fgcolorlight,
                                           highlightcolor=self.fgcolorlight, highlightthickness=1, bd=0)
                        self.e.grid(row=i, column=j+v, ipady=5)
                        self.e.bind("<Button>", lambda a: "break")      # make entry box unselectable
                        self.e.insert(END, ' '+str(list(self.courses.values())[i][v]))
                mark = int(list(self.courses.values())[i][2])
                # --- grades --- #
                self.e = Entry(self.courses_frame, width=20, fg=self.fgcolor, bg='#F4EDE8', font=font, highlightbackground=self.fgcolorlight,
                               highlightcolor=self.fgcolorlight, highlightthickness=1, bd=0)
                self.e.grid(row=i, column=5, ipady=5)
                self.e.bind("<Button>", lambda a: "break")      # make entry box unselectable
                self.e.insert(END, ' A' if mark>90 else ' B' if mark>80 else ' C' if mark>60 else ' D' if mark>45 else ' E' if mark>40 else ' F')

        self.btn_add_courses = Button(self.canvas_courses, text="Add", font=font, fg=self.bgcolor, bg=self.fgcolor, bd=0,
                                       activebackground='black', activeforeground='white', cursor='hand2', command=self.add_courses_page)
        self.btn_add_courses.place(x=860, y=self.top_margin+500, height=25,  width=130)
        self.btn_edit_courses = Button(self.canvas_courses, text="Edit", font=font, fg=self.fgcolor, bg=self.bgcolor, bd=1,
                                       activebackground='black', activeforeground='white', cursor='hand2', command=self.update_courses_page)
        self.btn_edit_courses.place(x=1000, y=self.top_margin+500, height=25,  width=130)

        if self.keys > 9:
            self.btn_add_courses.config(state='disabled')
        else:
            self.btn_add_courses.config(state='normal')


    def add_courses_page(self):
        self.add_courses_form = Frame(self.canvas_courses, bg=self.bgcolor)
        self.add_courses_form.columnconfigure(0, weight=1)
        self.add_courses_form.columnconfigure(1, weight=2)
        self.add_courses_form.columnconfigure(2, weight=1)
        self.add_courses_form.rowconfigure(0, weight=3)
        self.add_courses_form.rowconfigure(1, weight=1)
        self.add_courses_form.rowconfigure(2, weight=2)
        self.add_courses_form.rowconfigure(3, weight=1)
        self.add_courses_form.rowconfigure(4, weight=2)
        self.add_courses_form.rowconfigure(5, weight=1)
        self.add_courses_form.rowconfigure(6, weight=2)
        self.add_courses_form.rowconfigure(7, weight=1)
        self.add_courses_form.rowconfigure(8, weight=2)
        self.add_courses_form.rowconfigure(9, weight=1)
        self.add_courses_form.rowconfigure(10, weight=3)

        vcmd = (self.register(self.callback))       #to validate and accept only numbers

        # course code
        lbl_code = Label(self.add_courses_form, text='Course Code', fg=self.fgcolor, bg=self.bgcolor, font=font)
        lbl_code.grid(row=1, column=1, padx=4, pady=2, sticky='w')
        self.code_entry = Entry(self.add_courses_form, disabledbackground=self.bgcolor,
                                fg=self.fgcolor, bg=self.fgcolorlight, font=font_big_bold)
        self.code_entry.grid(row=2, column=1, padx=4, pady=3, sticky='nsew')

        # course title
        lbl_title = Label(self.add_courses_form, text='Course Title', fg=self.fgcolor, bg=self.bgcolor, font=font)
        lbl_title.grid(row=3, column=1, padx=4, pady=2, sticky='w')
        self.title_entry = Entry(self.add_courses_form, disabledbackground=self.bgcolor,
                                fg=self.fgcolor, bg=self.fgcolorlight, font=font_big_bold)
        self.title_entry.grid(row=4, column=1, padx=4, pady=3, sticky='nsew')

        # credit hour
        lbl_ch = Label(self.add_courses_form, text='Credit Hour', fg=self.fgcolor, bg=self.bgcolor, font=font)
        lbl_ch.grid(row=5, column=1, padx=4, pady=2, sticky='w')
        self.ch_entry = Entry(self.add_courses_form, disabledbackground=self.bgcolor, validate='all', validatecommand=(vcmd, '%P'),
                                fg=self.fgcolor, bg=self.fgcolorlight, font=font_big_bold)
        self.ch_entry.grid(row=6, column=1, padx=4, pady=3, sticky='nsew')

        # grade
        lbl_grade = Label(self.add_courses_form, text='Score', fg=self.fgcolor, bg=self.bgcolor, font=font)
        lbl_grade.grid(row=7, column=1, padx=4, pady=2, sticky='w')
        self.grade_entry = Entry(self.add_courses_form, disabledbackground=self.bgcolor, validate='all', validatecommand=(vcmd, '%P'),
                                fg=self.fgcolor, bg=self.fgcolorlight, font=font_big_bold)
        self.grade_entry.grid(row=8, column=1, ipadx=6, padx=4, pady=3, sticky='nsew')


        self.btn_confirm = Button(self.add_courses_form, text='Confirm', fg=self.bgcolor, bg=self.fgcolor, font=font,
                                  command=self.add_course, width=30)
        self.btn_confirm.grid(row=9, column=1, padx=4, pady=3, sticky='nse')


        self.add_courses_form.place(x=self.left_margin1, y=self.top_margin+30, width=1100, height=500)
        self.courses_frame.destroy()
        self.btn_edit_courses.destroy()

    def callback(self, P):
        if str.isdigit(P) or P=="":
            return True
        else:
            return False



    def update_courses_page(self):
        self.update_courses_form = Frame(self.canvas_courses, bg=self.bgcolor)
        self.update_courses_form.columnconfigure(0, weight=1)
        self.update_courses_form.columnconfigure(1, weight=2)
        self.update_courses_form.columnconfigure(2, weight=1)
        self.update_courses_form.columnconfigure(3, weight=1)
        self.courses_box = []

        print(self.keys)
        for i in range(self.keys):
            for j in range(2):
                self.sub_box = []    # a list for each textbox
                if j == 0:
                    self.a = Entry(self.update_courses_form, width=20, fg=self.fgcolor, bg='#F4EDE8', font=font, highlightbackground=self.fgcolorlight,
                                   highlightcolor=self.fgcolorlight, highlightthickness=1, bd=0)
                    self.a.grid(row=i, column=j, ipady=5, pady=3)
                    self.a.bind("<Button>", lambda a: "break")      # make entry box unselectable
                    self.a.insert(END, ' '+list(self.courses.keys())[i])
                    self.sub_box.append(self.a)
                else:
                    for v in range(3):
                        if v==0:
                            self.e = Entry(self.update_courses_form, width=40, fg=self.fgcolor, bg='#F4EDE8', font=font, highlightbackground=self.fgcolorlight,
                                           highlightcolor=self.fgcolorlight, highlightthickness=1, bd=0)     # make course name column wider (width:40)
                            self.e.bind("<Button>", lambda a: "break")      # make entry box unselectable
                        else:
                            self.e = Entry(self.update_courses_form, width=20, fg=self.fgcolor, bg=self.bgcolor, font=font, highlightbackground=self.fgcolorlight,
                                           highlightcolor=self.fgcolorlight, highlightthickness=1, bd=0)
                        self.e.grid(row=i, column=j+v, ipady=5, pady=3)
                        self.e.insert(END, ' '+str(list(self.courses.values())[i][v]))
                        self.sub_box.append(self.e)

            self.courses_box.append(self.sub_box)   # appending each list of entry to a general list for courses

        btn_names = []
        btns = []
        for i in range(len(self.courses)):
            btn_names.append("Button"+str(i))
            btns.append(Button(self.update_courses_form, text='Del', width=5, fg=self.fgcolor, bg='#F4EDE8', font=font,
                                            activebackground='black', activeforeground='white', bd=0, cursor='hand2', command=lambda c=i: self.confirm_delete(c)))
            btns[i].grid(row=i, column=5, ipady=3, pady=3)

        self.btn_update_courses = Button(self.canvas_courses, text="Update", font=font, fg=self.bgcolor, bg=self.fgcolor, bd=0,
                               activebackground='black', activeforeground='white', cursor='hand2', command=self.update_courses)
        self.btn_update_courses.place(x=860, y=self.top_margin+500, height=25,  width=130)
        self.btn_cancel_update_courses = Button(self.canvas_courses, text="Cancel", font=font, fg=self.fgcolor, bg=self.bgcolor, bd=1,
                                         activebackground='black', activeforeground='white', cursor='hand2', command=self.cancel_update_courses)
        self.btn_cancel_update_courses.place(x=1000, y=self.top_margin+500, height=25,  width=130)

        self.update_courses_form.place(x=self.left_margin1, y=self.top_margin+30, width=1100, height=500)

        self.courses_frame.destroy()
        self.btn_edit_courses.destroy()


    def hover_over(self, e):
        self.btn_logout.config(font=('Calibri', 13, 'underline'))

    def leave(self, e):
        self.btn_logout.config(font=('Calibri', 13))

    def logout(self):
        self.acct.db.commit()
        self.acct.db.close()
        self.destroy()                     # .deiconify to undo
        loginScr.deiconify()

    def edit(self):
        self.table_frame.place_forget()
        self.btn_edit.place_forget()
        self.btn_print.place_forget()
        self.update_form.place(x=self.left_margin2, y=self.top_margin+30, width=910, height=500)
        self.btn_update.place(x=860, y=self.top_margin+500, height=25,  width=130)
        self.btn_cancel.place(x=1000, y=self.top_margin+500, height=25, width=130)

    def update_profile(self):
        values = []
        for i in self.values_box:
            values.append(i.get())
        try:
            for j in range(self.total_rows):
                self.details[list(self.details.keys())[j]] = values[j]
            self.acct.update_profile("profile",values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9])    #update profile table in db
            messagebox.showinfo('Successful', 'Profile updated successfully', parent=self)
            self.cancel_profile_update()    # hide form & unhide table
        except:
            messagebox.showerror('Error', 'Ooops! Cannot update.', parent=self)
        # print(self.details)




    def cancel_profile_update(self):
        self.update_form.place_forget()
        self.btn_update.place_forget()
        self.btn_cancel.place_forget()
        self.table_frame.place(x=self.left_margin2, y=self.top_margin+30, width=910, height=500)
        self.load_details()
        self.btn_edit.place(x=860, y=self.top_margin+500, height=25,  width=130)
        self.btn_print.place(x=1000, y=self.top_margin+500, height=25, width=130)


    def add_course(self):
        code = self.code_entry.get().strip()
        title = self.title_entry.get().strip()
        ch = self.ch_entry.get().strip()
        grade = self.grade_entry.get().strip()
        keys = [title, ch, grade]

        if code=="" or title=="" or ch=="" or grade=="":
            messagebox.showerror('Error', 'All fields are required', parent=self)
        else:
            try:
                self.courses[code] = keys
                self.acct.insert("courses", code, title, ch, grade)
                messagebox.showinfo('Successful', f'You added {title}', parent=self)

                self.add_courses_form.destroy()
                self.keys += 1
                self.courses_frame = Frame(self.canvas_courses, bg=self.bgcolor)
                self.load_courses()
                self.courses_frame.place(x=self.left_margin1, y=self.top_margin+30, width=1100, height=500)
            except:
                messagebox.showerror('Failed', f'You cannot add {title}', parent=self)

            # print(self.courses)





    def update_courses(self):
        self.values = []
        for i in self.courses_box:
            details = []
            for j in range(3):
                # print(i[j].get())
                details.append(i[j].get())
            self.values.append(details)
        try:
            for course in range(len(self.courses)):
                self.courses[list(self.courses.keys())[course]] = self.values[course]
                self.acct.update("courses", list(self.courses.keys())[course], self.values[course][0], self.values[course][1], self.values[course][2])
            messagebox.showinfo('Successful', 'Updated course(s)!', parent=self)
            self.courses_box = []
            self.cancel_update_courses()
        except:
            messagebox.showerror('Failed', 'Cannot update', parent=self)
        # print(self.courses)
        # self.load_courses()


    def cancel_update_courses(self):
        self.update_courses_form.place_forget()
        self.update_courses_form.destroy()
        self.btn_update_courses.place_forget()
        self.btn_update_courses.destroy()
        self.btn_cancel_update_courses.place_forget()
        self.btn_cancel_update_courses.destroy()

        self.courses_frame = Frame(self.canvas_courses, bg=self.bgcolor)
        self.load_courses()
        self.courses_frame.place(x=self.left_margin1, y=self.top_margin+30, width=1100, height=500)


    def confirm_delete(self, e):
        confirm = messagebox.askyesno('Confirm', 'Delete this course?')
        if(confirm):
            try:
                self.acct.delete("courses", list(self.courses.keys())[e])   #removes course from database
                del self.courses[list(self.courses.keys())[e]]  #removes course from self.courses dict
                self.keys = self.keys - 1
                self.update_courses_form.place_forget()
                self.update_courses_form.destroy()
                self.update_courses_page()
            except:
                messagebox.showerror('Failed', f'Cannot delete {list(self.courses.keys())[e]}', parent=self)


    def print_profile(self):
        pass


    # creating menu bar
    def menu_bar(self):
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Save as...")
        filemenu.add_command(label="Close")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo")
        editmenu.add_separator()
        editmenu.add_command(label="Cut")
        editmenu.add_command(label="Copy")
        editmenu.add_command(label="Paste")
        editmenu.add_command(label="Delete")
        editmenu.add_command(label="Select All")
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index")
        helpmenu.add_command(label="About...")
        menubar.add_cascade(label="Help", menu=helpmenu)
        return menubar



if __name__ == '__main__':
    app = LoginScreen()
    app.mainloop()