
import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from tkinter import messagebox
import csv
from vendor_page import Vendor_Page
from Display_new import Display



class Cust_Login() :
    def __init__(self,root) :
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets_Login")



        self.window = root

        self.window.geometry("1000x600")
        self.window.configure(bg = "#E6E6E6")


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
        self.image_image_1 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            554.0,
            355.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            284.0,
            78.0,
            716.0,
            509.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            438.0,
            105.0,
            anchor="nw",
            text="LOGIN",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        self.button_image_1 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("button_1.png"))
        self.Proceed = Button(self.canvas,
            image= self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._login(),
            relief="flat"
        )
        self.Proceed.place(
            x=426.0,
            y=406.0,
            width=134.0,
            height=47.0
        )

        self.canvas.create_text(
            326.0,
            198.0,
            anchor="nw",
            text="ENTER MAIL",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            326.0,
            293.0,
            anchor="nw",
            text="ENTER PASSWORD",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.entry_image_1 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            496.0,
            339.0,
            image=self.entry_image_1
        )
        self.pwd = Entry(self.canvas,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.pwd.place(
            x=326.0,
            y=315.0,
            width=340.0,
            height=46.0
        )

        self.entry_image_2 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            496.0,
            248.0,
            image=self.entry_image_2
        )
        self.email = Entry(self.canvas,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.email.place(
            x=326.0,
            y=224.0,
            width=340.0,
            height=46.0
        )


    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def _login(self) :

        email = self.email.get()
        pwd = self.pwd.get()

        with open("customers.csv","r") as f:
            reader = csv.reader(f)

            for i in reader :
                if i == [] :
                    continue
                elif i[1] == email and i[-1] == pwd :
                    messagebox.showinfo('Login Status', 'Logged in Successfully!')
                    self.display_click()
                    break
            else :
                messagebox.showerror('Login Status', 'invalid username or password')

    def display_click(self) :
        root_1 = Toplevel()
        self.window.destroy()
        a=Display(root_1)
        root_1.mainloop()
    


class Vendor_Login() :
    def __init__(self,root) :
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets_Login")



        self.window = root

        self.window.geometry("1000x600")
        self.window.configure(bg = "#E6E6E6")


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
        self.image_image_1 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            554.0,
            355.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            284.0,
            78.0,
            716.0,
            509.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            438.0,
            105.0,
            anchor="nw",
            text="LOGIN",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        self.button_image_1 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("button_1.png"))
        self.Proceed = Button(self.canvas,
            image= self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._login(),
            relief="flat"
        )
        self.Proceed.place(
            x=426.0,
            y=406.0,
            width=134.0,
            height=47.0
        )

        self.canvas.create_text(
            326.0,
            198.0,
            anchor="nw",
            text="ENTER MAIL",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.canvas.create_text(
            326.0,
            293.0,
            anchor="nw",
            text="ENTER PASSWORD",
            fill="#000000",
            font=("Inter Bold", 15 * -1)
        )

        self.entry_image_1 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            496.0,
            339.0,
            image=self.entry_image_1
        )
        self.pwd = Entry(self.canvas,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.pwd.place(
            x=326.0,
            y=315.0,
            width=340.0,
            height=46.0
        )

        self.entry_image_2 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            496.0,
            248.0,
            image=self.entry_image_2
        )
        self.email = Entry(self.canvas,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.email.place(
            x=326.0,
            y=224.0,
            width=340.0,
            height=46.0
        )


    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def _login(self) :

        email = self.email.get()
        pwd = self.pwd.get()

        with open("vendor.csv","r") as f:
            reader = csv.reader(f)

            for i in reader :
                if i == [] :
                    continue
                elif i[1] == email and i[-1] == pwd :
                    messagebox.showinfo('Login Status', 'Logged in Successfully!')
                    self.next_page()
                    break
            else :
                messagebox.showerror('Login Status', 'invalid username or password')

    def next_page(self) :
        root = Tk()
        a= Vendor_Page(root)
        self.window.destroy()
        root.mainloop()


