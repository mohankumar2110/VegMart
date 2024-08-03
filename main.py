


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from register import Cust_Register,Vendor_Register
from Login import Cust_Login,Vendor_Login


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets_main")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def _login_cust() :
    root = Tk()
    a = Cust_Login(root)
    root.mainloop()


def _reg_cust() :
    root = Tk()
    a = Cust_Register(root)
    root.mainloop()

def _login_vend() :
    root = Tk()
    a = Vendor_Login(root)
    root.mainloop()


def _reg_vend() :
    root = Tk()
    a = Vendor_Register(root)
    root.mainloop()

window = Tk()

window.geometry("1000x600")
window.configure(bg = "#E6E6E6")


canvas = Canvas(
    window,
    bg = "#E6E6E6",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    504.0,
    355.0,
    image=image_image_1
)

canvas.create_rectangle(
    167.0,
    69.0,
    833.0,
    500.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    612.0,
    196.0,
    anchor="nw",
    text="VENDOR",
    fill="#000000",
    font=("Inter Bold", 25 * -1)
)

canvas.create_text(
    243.0,
    196.0,
    anchor="nw",
    text="CUSTOMER",
    fill="#000000",
    font=("Inter Bold", 25 * -1)
)

canvas.create_text(
    375.0,
    90.0,
    anchor="nw",
    text="WELCOME!",
    fill="#000000",
    font=("Inter Bold", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: _reg_vend(),
    relief="flat"
)
button_1.place(
    x=552.0,
    y=359.0,
    width=254.0,
    height=53.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: _reg_cust(),
    relief="flat"
)
button_2.place(
    x=200.0,
    y=359.0,
    width=254.0,
    height=53.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: _login_vend(),
    relief="flat"
)
button_3.place(
    x=552.0,
    y=258.0,
    width=254.0,
    height=53.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: _login_cust(),
    relief="flat"
)
button_4.place(
    x=200.0,
    y=258.0,
    width=254.0,
    height=53.0
)

canvas.create_rectangle(
    499.0,
    153.0,
    500.0,
    474.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
