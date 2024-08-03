
from tkinter import *
import csv
from tkinter import messagebox
from Display_final import Display
from vendor_page import Vendor_page



class Registerv() :

    def __init__(self,root) :
        super().__init__()  

        self.root = root
        self.root.title("VENDOR REGISTRATION")
        self.f = ('Times', 14)
        self.var = StringVar()
        self.var.set('male')



        self.right_frame = Frame(
            self.root, 
            bd=2, 
            bg='#CCCCCC',
            relief=SOLID, 
            padx=10, 
            pady=10
            )


        Label(
            self.right_frame, 
            text="Enter Name", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=0, column=0, sticky=W, pady=10)

        Label(
            self.right_frame, 
            text="Enter Email", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=1, column=0, sticky=W, pady=10)

        Label(
            self.right_frame, 
            text="Contact Number", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=2, column=0, sticky=W, pady=10)




        Label(
            self.right_frame, 
            text="Enter Password", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=5, column=0, sticky=W, pady=10)



        self.register_name = Entry(
            self.right_frame, 
            font=self.f
            )

        self.register_email = Entry(
            self.right_frame, 
            font=self.f
            )

        self.register_mobile = Entry(
            self.right_frame, 
            font=self.f
            )



        self.register_pwd = Entry(
            self.right_frame, 
            font=self.f,
            show='*'
        )


        self.register_btn = Button(
            self.right_frame, 
            width=15, 
            text='Register', 
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command= lambda: self._register()
        )


        self.register_name.grid(row=0, column=1, pady=10, padx=20)
        self.register_email.grid(row=1, column=1, pady=10, padx=20) 
        self.register_mobile.grid(row=2, column=1, pady=10, padx=20)
        self.register_pwd.grid(row=5, column=1, pady=10, padx=20)

        self.register_btn.grid(row=7, column=1, pady=10, padx=20)
        self.right_frame.pack()

    def _register(self) :

        name = self.register_name.get()
        mail = self.register_email.get()
        phone_no = self.register_mobile.get()
        password = self.register_pwd.get()

        with open('vendor.csv','a') as csvfile: 
         
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow([name,mail,phone_no,password])

        messagebox.showinfo('Register','Registered Successfully!')
        self.display_click()

    def display_click(self) :
        root = Tk()
        v=Vendor_page(root)
        root.mainloop()

class Loginv() :



    def __init__(self, root) :

        self.root = root
        self.root.title("VENDOR LOGIN")
        self.root.geometry("700x600")
        self.root.config(bg='#FFFAF0')

        self.f = ('Times', 14)

        self.left_frame = Frame(
            self.root, 
            bd=2, 
            bg='#CCCCCC',   
            relief=SOLID, 
            padx=50, 
            pady=50
            )

        Label(
            self.left_frame, 
            text="Enter Email", 
            bg='#CCCCCC',
            font=self.f).grid(row=0, column=0, sticky=W, pady=10)

        Label(
            self.left_frame, 
            text="Enter Password", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=1, column=0, pady=10)

        self.email_tf = Entry(
            self.left_frame, 
            font=self.f
            )
        self.pwd_tf = Entry(
            self.left_frame, 
            font=self.f,
            show='*'
            )
        self.login_btn = Button(
            self.left_frame, 
            width=15, 
            text='Login', 
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command= lambda : self._login()
            )

        self.email_tf.grid(row=0, column=1, pady=10, padx=20)
        self.pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        self.login_btn.grid(row=2, column=1, pady=10, padx=20)
        self.left_frame.place(relx=.5,rely=.5,anchor=CENTER)

    def _login(self) :

        email = self.email_tf.get()
        pwd = self.pwd_tf.get()

        with open("vendor.csv","r") as f:
            reader = csv.reader(f)

            for i in reader :
                if i == [] :
                    continue
                elif i[1] == email and i[-1] == pwd :
                    messagebox.showinfo('Login Status', 'Logged in Successfully!')
                    self.modify_click()
                    break
            else :
                messagebox.showerror('Login Status', 'invalid username or password')

    def modify_click(self) :
        root = Tk()
        v=Vendor_page(root)
        root.mainloop()

    

    


