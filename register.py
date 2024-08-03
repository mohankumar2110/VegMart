

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
import csv
from vendor_page import Vendor_Page
from Display_new import Display
from tkinter import messagebox
import re




class Cust_Register() :

    def __init__(self,root) :
        

        self.window = root


        self.window.geometry("1000x600")
        self.window.configure(bg = "#E6E6E6")
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets_register")


        self.canvas = Canvas(
            self.window,
            bg = "#E6E6E6",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(master=self.canvas,
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            504.0,
            355.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            284.0,
            65.0,
            716.0,
            536.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            426.0,
            81.0,
            anchor="nw",
            text="REGISTER ",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        self.button_image_1 = PhotoImage(master=self.canvas,
            file=self.relative_to_assets("button_1.png"))
        self.Proceed = Button(self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._register(),
            relief="flat"
        )
        self.Proceed.place(
            x=429.0,
            y=471.0,
            width=134.0,
            height=47.0
        )

        self.canvas.create_text(
            326.0,
            145.0,
            anchor="nw",
            text="ENTER MAIL",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            326.0,
            297.0,
            anchor="nw",
            text="ENTER PASSWORD",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            326.0,
            375.0,
            anchor="nw",
            text="ENTER PHONE NUMBER",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            326.0,
            221.0,
            anchor="nw",
            text="ENTER NAME",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_1 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            493.0,
            187.0,
            image=self.entry_image_1
        )
        self.register_email = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.register_email.place(
            x=323.0,
            y=163.0,
            width=340.0,
            height=46.0
        )

        self.entry_image_2 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            496.0,
            417.0,
            image= self.entry_image_2
        )
        self.register_mobile = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.register_mobile.place(
            x=326.0,
            y=393.0,
            width=340.0,
            height=46.0
        )

        self.entry_image_3 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            496.0,
            263.0,
            image=self.entry_image_3
        )
        self.register_name = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.register_name.place(
            x=326.0,
            y=239.0,
            width=340.0,
            height=46.0
        )

        self.entry_image_4 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            496.0,
            339.0,
            image= self.entry_image_4
        )
        self.register_pwd = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.register_pwd.place(
            x=326.0,
            y=315.0,
            width=340.0,
            height=46.0
        )




    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def _register(self) :

        name = self.register_name.get()
        mail = self.register_email.get()
        phone_no = self.register_mobile.get()
        password = self.register_pwd.get()

        print(name,mail,phone_no,password)

        if re.search("[a-zA-Z0-9]+@[a-zA-Z]+\.(com|in|net)",mail) and phone_no[0] == '9' and len(phone_no) == 10:
                with open('customers.csv','a') as csvfile: 
                
                    csvwriter = csv.writer(csvfile) 
                    csvwriter.writerow([name,mail,phone_no,password])

                messagebox.showinfo('Register','Registered Successfully!')
                self.display_next()

        else:
            messagebox.showerror("Register","Invalid mail Id or phone number")
    def display_next(self) :
        root = Toplevel()
        a = Display(root)
        self.window.destroy()
        root.mainloop()

class Vendor_Register() :

    def __init__(self,root) :
        

        self.window = root


        self.window.geometry("1000x600")
        self.window.configure(bg = "#E6E6E6")
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets_register")


        self.canvas = Canvas(
            self.window,
            bg = "#E6E6E6",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(master=self.canvas,
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            504.0,
            355.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            284.0,
            65.0,
            716.0,
            536.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            426.0,
            81.0,
            anchor="nw",
            text="REGISTER ",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        self.button_image_1 = PhotoImage(master=self.canvas,
            file=self.relative_to_assets("button_1.png"))
        self.Proceed = Button(self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._register(),
            relief="flat"
        )
        self.Proceed.place(
            x=429.0,
            y=471.0,
            width=134.0,
            height=47.0
        )

        self.canvas.create_text(
            326.0,
            145.0,
            anchor="nw",
            text="ENTER MAIL",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            326.0,
            297.0,
            anchor="nw",
            text="ENTER PASSWORD",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            326.0,
            375.0,
            anchor="nw",
            text="ENTER PHONE NUMBER",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            326.0,
            221.0,
            anchor="nw",
            text="ENTER NAME",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_1 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            493.0,
            187.0,
            image=self.entry_image_1
        )
        self.register_email = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.register_email.place(
            x=323.0,
            y=163.0,
            width=340.0,
            height=46.0
        )

        self.entry_image_2 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            496.0,
            417.0,
            image= self.entry_image_2
        )
        self.register_mobile = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.register_mobile.place(
            x=326.0,
            y=393.0,
            width=340.0,
            height=46.0
        )

        self.entry_image_3 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            496.0,
            263.0,
            image=self.entry_image_3
        )
        self.register_name = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.register_name.place(
            x=326.0,
            y=239.0,
            width=340.0,
            height=46.0
        )

        self.entry_image_4 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            496.0,
            339.0,
            image= self.entry_image_4
        )
        self.register_pwd = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.register_pwd.place(
            x=326.0,
            y=315.0,
            width=340.0,
            height=46.0
        )




    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def _register(self) :

        name = self.register_name.get()
        mail = self.register_email.get()
        phone_no = self.register_mobile.get()
        password = self.register_pwd.get()

        print(name,mail,phone_no,password)

        if re.search("[a-zA-Z0-9]+@[a-zA-Z]+\.(com|in|net)",mail) and phone_no[0] == '9' and len(phone_no) == 10:

                with open('vendor.csv','a') as csvfile: 
                
                    csvwriter = csv.writer(csvfile) 
                    csvwriter.writerow([name,mail,phone_no,password])

                messagebox.showinfo('Register','Registered Successfully!')
                self.next_page()
        else:
            messagebox.showerror("Register","Invalid mail ID or phone number")
    def next_page(self) :
        root = Tk()
        a= Vendor_Page(root)
        self.window.destroy()
        root.mainloop()


    
