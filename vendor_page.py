


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from vendor_add import *



class Vendor_Page() :

    def __init__(self,root) :

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets_vendor")





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
            292.0,
            71.0,
            724.0,
            502.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            423.0,
            105.0,
            anchor="nw",
            text="VENDOR",
            fill="#000000",
            font=("Inter Bold", 40 * -1)
        )

        self.button_image_1 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("button_1.png"))
        self.mod_btn = Button(self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.mod_click(),
            relief="flat"
        )
        self.mod_btn.place(
            x=362.0,
            y=371.0,
            width=277.0,
            height=61.0
        )

        self.button_image_2 = PhotoImage(master = self.canvas,
            file=self.relative_to_assets("button_2.png"))
        self.del_btn = Button(self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.del_click(),
            relief="flat"
        )
        self.del_btn.place(
            x=362.0,
            y=278.0,
            width=277.0,
            height=61.0
        )

        self.button_image_3 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_3.png"))
        self.add_btn = Button(self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_click(),
            relief="flat"
        )
        self.add_btn.place(
            x=362.0,
            y=185.0,
            width=277.0,
            height=61.0
        )


    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def add_click(self) :
        root = Tk()
        a = Add_veg(root)
        root.mainloop()

    def del_click(self) :
        root = Tk()
        a = Del_veg(root)
        root.mainloop()

    def mod_click(self) :
        root = Tk()
        a = Mod_veg(root)
        root.mainloop()

