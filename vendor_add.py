

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from tkinter import messagebox
import csv
import shutil
import os
import re
from Display_new import Display
class Add_veg() :

    def __init__(self,root) :


        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets_add_veg")





        self.window = root

        self.window.geometry("1000x600")
        self.window.configure(bg = "#E6E6E6")
        self.img_name = ''

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

        self.button_image_1 = PhotoImage(master= self.canvas,
            file= self.relative_to_assets("button_1.png"))
        self.Proceed = Button(self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._add(),
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
            text="ENTER NAME  ",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            326.0,
            297.0,
            anchor="nw",
            text="ENTER QUANTITY (Example : 5-1kg)",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            326.0,
            221.0,
            anchor="nw",
            text="ENTER  PRICE (Example : 10 per kg)",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_1 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            493.0,
            187.0,
            image=self.entry_image_1
        )
        self.register_veg_name = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.register_veg_name.place(
            x=323.0,
            y=163.0,
            width=340.0,
            height=46.0
        )

        self.button_image_2 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_2.png"))
        self.addimg_btn = Button(self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_img(),
            relief="flat"
        )
        self.addimg_btn.place(
            x=365.0,
            y=391.0,
            width=267.0,
            height=48.0
        )

        self.entry_image_2 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            496.0,
            263.0,
            image=self.entry_image_2
        )
        self.register_veg_price = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.register_veg_price.place(
            x=326.0,
            y=239.0,
            width=340.0,
            height=46.0
        )

        self.entry_image_3 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            496.0,
            339.0,
            image= self.entry_image_3
        )
        self.register_veg_qty = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.register_veg_qty.place(
            x=326.0,
            y=315.0,
            width=340.0,
            height=46.0
        )

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def _add(self) :

        name = self.register_veg_name.get()
        qty = self.register_veg_qty.get()
        price = self.register_veg_price.get()
        img = self.img_name
        print(name,qty,price,img)

        qty_lst = qty.split()
        price_lst = price.split()
        print("testtttttt",qty_lst,price_lst)

        if name.isalpha() and len(price_lst) == 3 and len(qty_lst) == 1 :
            if isinstance(int(price_lst[0]),int) and int(price_lst[0]) > 0 and price_lst[1] == 'per' and price_lst[2] == 'kg' and re.search("[1-9]+-[1-9]+[a-z]",qty_lst[0]):

                if self.add_check(name) :
                    messagebox.showinfo('', 'Vegetable already exists in stock!')
                    return 



                with open('Stock.csv','a') as csvfile: 
                
                    csvwriter = csv.writer(csvfile) 
                    csvwriter.writerow([name,qty,price,img])

                messagebox.showinfo('', 'Vegetable added!')
            else:
                messagebox.showerror('',"Enter a Valid Input!")
        else:
            messagebox.showerror('',"Enter a Valid Input!")
        

    def add_img(self) :
        
        f_types = [('Jpg Files', '*.jpg')]
        img_path = filedialog.askopenfilename(filetypes=f_types)
        self.img_name = os.path.basename(img_path)
        shutil.copyfile(img_path, f'./assets_pic/{self.img_name}')
        self.img_name = os.path.basename(img_path)

    def add_check(self,name) :
        with open("Stock.csv", "r") as f :
            reader = csv.reader(f)

            for i in reader :
                if i == [] :
                    continue
                elif i[0].lower() == name.lower() :
                    return True
            else :
                return False


class Mod_veg() :

    def __init__(self,root) :


        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets_add_veg")





        self.window = root

        self.window.geometry("1000x600")
        self.window.configure(bg = "#E6E6E6")
        self.img_name = ''

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

        self.button_image_1 = PhotoImage(master= self.canvas,
            file= self.relative_to_assets("button_1.png"))
        self.Proceed = Button(self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._Mod(),
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
            text="ENTER NAME  ",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            326.0,
            297.0,
            anchor="nw",
            text="ENTER QUANTITY (Example : 5-1kg)",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            326.0,
            221.0,
            anchor="nw",
            text = "ENTER  PRICE (Example : 10 per kg)",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_1 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            493.0,
            187.0,
            image=self.entry_image_1
        )
        self.mod_veg_name = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.mod_veg_name.place(
            x=323.0,
            y=163.0,
            width=340.0,
            height=46.0
        )

        self.button_image_2 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_2.png"))
        self.addimg_btn = Button(self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_img(),
            relief="flat"
        )
        self.addimg_btn.place(
            x=365.0,
            y=391.0,
            width=267.0,
            height=48.0
        )

        self.entry_image_2 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            496.0,
            263.0,
            image=self.entry_image_2
        )
        self.mod_veg_price = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.mod_veg_price.place(
            x=326.0,
            y=239.0,
            width=340.0,
            height=46.0
        )

        self.entry_image_3 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            496.0,
            339.0,
            image= self.entry_image_3
        )
        self.mod_veg_qty = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.mod_veg_qty.place(
            x=326.0,
            y=315.0,
            width=340.0,
            height=46.0
        )

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def add_img(self) :
        
        f_types = [('Jpg Files', '*.jpg')]
        self.img_name = filedialog.askopenfilename(filetypes=f_types)

    def _Mod(self) :

        name = self.mod_veg_name.get()
        qty = self.mod_veg_qty.get()
        price = self.mod_veg_price.get()
        img = self.img_name

        qty_lst = qty.split()
        price_lst = price.split()

        if name.isalpha() and len(price_lst) == 3 and len(qty_lst) == 1:
            if isinstance(int(price_lst[0]),int) and int(price_lst[0]) > 0 and price_lst[1] == 'per' and price_lst[2] == 'kg' and re.search("[1-9]+-[1-9]+[a-z]",qty_lst[0]):
                with open("Stock.csv", "r") as f :
                    state = False
                    reader = csv.reader(f)
                    with open('temp.csv','w') as temp :
                        writer = csv.writer(temp)
                        for i in reader :
                            print(i)
                            if i == [] :
                                continue
                            else : 
                                if i[0].lower() == name.lower() :
                                    state = True
                                    if qty != '' : i[1] = qty
                                    if price != '' : i[2] = price
                                    if img != '' : i[1] = img    
                                writer.writerow(i)    
                    if not(state) :
                        messagebox.showinfo('', 'Vegetable not found!')
                    else :
                        messagebox.showinfo('', 'Vegetable Modified')
                                
                with open("Stock.csv",'w') as f :
                    writer = csv.writer(f)
                    with open('temp.csv','r') as temp :
                        reader = csv.reader(temp) 
                        for i in reader :
                            writer.writerow(i)
            else:
                messagebox.showerror('',"Ente a Valid Input!")
        else:
            messagebox.showerror('',"Ente a Valid Input!")

class Del_veg() :
    def __init__(self,root) :
        

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets_del_veg")




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
            504.0,
            355.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            284.0,
            128.0,
            716.0,
            418.0,
            fill="#FFFFFF",
            outline="")

        self.button_image_1 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_1.png"))
        self.delete = Button(self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._Del(),
            relief="flat"
        )
        self.delete.place(
            x=426.0,
            y=308.0,
            width=134.0,
            height=47.0
        )

        self.canvas.create_text(
            323.0,
            188.0,
            anchor="nw",
            text="ENTER NAME  ",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_1 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            493.0,
            234.0,
            image=self.entry_image_1
        )
        self.del_veg_name = Entry(self.canvas,
            bd=0,
            bg="#F7F7F7",
            highlightthickness=0
        )
        self.del_veg_name.place(
            x=323.0,
            y=210.0,
            width=340.0,
            height=46.0
        )


    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def _Del(self) :

        name = self.del_veg_name.get()

        if name.isalpha():
            with open("Stock.csv", "r") as f :
                state = False
                reader = csv.reader(f)
                with open('temp.csv','w') as temp :
                    writer = csv.writer(temp)
                    for i in reader :
                        print(i)
                        if i == [] :
                            continue
                        else : 
                            if i[0].lower() == name.lower() :
                                state = True
                                continue
                            writer.writerow(i)    
                if not(state) :
                    messagebox.showinfo('', 'Vegetable not found!')
                else :
                    messagebox.showinfo('', 'Vegetable deleted')
                            
            with open("Stock.csv",'w') as f :
                writer = csv.writer(f)
                with open('temp.csv','r') as temp :
                    reader = csv.reader(temp) 
                    for i in reader :
                        writer.writerow(i)
        else:
            messagebox.showerror('',"Ente a Valid Input!")
