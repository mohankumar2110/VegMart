


from pathlib import Path
from textwrap import fill
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.ttk import Treeview
from turtle import screensize
from vegetable import Vegetable, Cust_item, Cust_cart
from Deq import Deq,DNode
from tkinter import *
from bst import BST
from tkinter import messagebox
from tkinter import filedialog
import csv
from PIL import ImageTk, Image



class Display() :

    def __init__(self,root) :

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets_display")
        self.ASSETS_PIC_PATH = self.OUTPUT_PATH / Path("./assets_pic")

        self.b=BST()
        self.stock = Deq()

        with open("Stock.csv", "r") as f :
            reader = csv.reader(f)

            for i in reader :
                #print(i)
                if i == [] :
                    continue
                else : 
                    self.stock.enqueue_rear(Vegetable(i[0],int(i[1]),float(i[2]),i[3]))


        self.cart = Cust_cart()

        self.display_item = self.stock.getfront()



        self.window = root

        self.window.geometry("1000x600")
        self.window.configure(bg = "#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.bg_image = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("bg.png"))
        self.canvas.create_rectangle(
            24.0,
            22.0,
            1055.0,
            667.0,
            fill="white",
            outline="")
        self.canvas.create_image(
            499.5,
            306.0,
            image=self.bg_image)

        self.entry_image_1 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            405.5,
            76.0,
            image=self.entry_image_1
        )
        self.search_box = Entry(self.canvas,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            font=('Century 15')
        )
        self.search_box.place(
            x=125.0,
            y=44.0,
            width=561.0,
            height=62.0
        )

        self.button_image_1 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_1.png"))
        self._search_but = Button(self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            bg = 'white',
            command=lambda: self._search(),
            relief="flat"
        )
        self._search_but.place(
            x=744.0,
            y=47.0,
            width=161.0,
            height=56.0
        )

        self.Products_frame = Canvas(self.canvas,
            height =400,
            width = 634,
            bg="white")
        self.Products_frame.place(x = 52.0, y = 148)

        self.canvas.create_rectangle(
            722.0,
            148.0,
            942.0,
            336.0,
            fill="white",
            outline="")

        self.canvas.create_rectangle(
            722.0,
            362.0,
            942.0,
            548.0,
            fill="white",
            outline="")

        self.button_image_2 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_2.png"))
        self.cart_btn = Button(self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            bg = 'white',
            command=lambda: self._final(),
            relief="flat"
        )
        self.cart_btn.place(
            x=775.0,
            y=179.0,
            width=114.0,
            height=45.0
        )

        self.button_image_3 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_3.png"))
        self._all_items = Button(self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            bg = 'white',
            command=lambda: self._display_all(),
            relief="flat"
        )
        self._all_items.place(
            x=775.0,
            y=258.0,
            width=114.0,
            height=41.94915771484375
        )

        self.button_image_4 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_4.png"))
        self.prev_button  = Button(self.canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            bg = 'white',
            command=lambda: self.prev(),
            relief="flat",
            state= DISABLED
        )
        self.prev_button.place(
            x=773.0,
            y=392.0,
            width=118.78179931640625,
            height=47.0
        )

        self.button_image_5 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_5.png"))
        self.next_button = Button(self.canvas,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            bg = 'white',
            command=lambda: self.next(),
            relief="flat"
        )
        self.next_button.place(
            x=773.0,
            y=473.0,
            width=118.78179931640625,
            height=47.0
        )

        self.Products_frame.create_rectangle(
            395.0,
            320.0,
            613.0,
            376.0,
            fill="green",
            outline="")

        self.button_image_6 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(self.Products_frame,
            image=self.button_image_6,
            borderwidth=0,
            bg = 'green',
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=479.0,
            y=329.0,
            width=43.0,
            height=39.41667175292969
        )

        self.button_image_7 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_7.png"))
        self.sub_veg = Button(self.Products_frame,
            image=self.button_image_7,
            borderwidth=0,
            bg = 'green',
            highlightthickness=0,
            command=lambda: self._sub(self.display_item.getitem()),
            relief="flat"
        )
        self.sub_veg.place(
            x=549.0,
            y=329.0,
            width=36.0,
            height=36.0
        )

        self.button_image_8 = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("button_8.png"))
        self.add_veg = Button(self.Products_frame,
            image=self.button_image_8,
            borderwidth=0,
            bg = 'green',
            highlightthickness=0,
            command=lambda: self._add(self.display_item.getitem()),
            relief="flat"
        )
        self.add_veg.place(
            x=420.0,
            y=329.0,
            width=36.0,
            height=36.0
        )
        self.canvas.create_rectangle(
            52.0,
            44.0,
            123.0,
            108.0,
            fill="white",
            outline="")

        self.search_img = PhotoImage(master= self.canvas,
            file=self.relative_to_assets("search.png"))
        self.entry_bg_1 = self.canvas.create_image(
            82.5,
            74.0,
            image=self.search_img)

        self.Products_frame.create_text(
            56.0,
            247.0,
            anchor="nw",
            text=f"{self.stock.getfront().getitem().getname()}",
            fill="#000000",
            font=("Inter Bold", 21 * -1)
        )

        self.Products_frame.create_text(
            57.0,
            293.0,
            anchor="nw",
            text=f"Qty:                      Price : ",
            fill="#000000",
            font=("Inter ", 21 * -1)
        )

        self.Products_frame.create_text(
            77.0,
            293.0,
            anchor="nw",
            text=f"     {self.stock.getfront().getitem().getqty()}                               {self.stock.getfront().getitem().getprice()} ",
            fill="#000000",
            font=("Rubik Bold", 21 * -1)
        )

        self.Products_frame.create_text(
            57.0,
            340.0,
            anchor="nw",
            text="Standard Delivery",
            fill="#000000",
            font=("Inter SemiBold", 21 * -1)
        )

        self.Products_frame.create_rectangle(
            66.0,
            430.0,
            663.0008544921875,
            431.0,
            fill="#000000",
            outline="")


        self.canvas.create_rectangle(
            73.0,
            169.0,
            663.0,
            378.0,
            fill="#FFFFFF",
            outline="")

        self.Item_frame=LabelFrame(
            self.Products_frame,
            bg = 'white'
            )

        self.Item_frame.place(x=35,y=15,width=400,height=200)
        self.img=Image.open(f"assets_pic\\{self.stock.getfront().getitem().getimg()}")
        self.resize_img=self.img.resize((390,180))
        self.final_img=ImageTk.PhotoImage(self.resize_img)
        self.img_veg=Label(self.Item_frame,image=self.final_img).pack(padx=3,pady=3)


    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def relative_to_assets_pic(self,path: str) -> Path:
        return self.ASSETS_PIC_PATH / Path(path)


    def _add(self,x) :
        if x.getqty() != 0 :
            self.cart.add(Cust_item(x))
            x.redqty()
        else :
            messagebox.showinfo("Stock Availability","Out of Stock")
            print(x.getqty())

    def _sub(self,x) :

        self.cart.sub(x)

    def _order_num(self):
        self.pay_screen.destroy()
        self.Button_frame.destroy()
        table_root.destroy()

        text="Payment done.\n\nThanks for shopping!\n\nYour order number is 1"
        self.thank_screen=LabelFrame(
            self.root,
            text=text,
            fg="black",
            font=("Segoe UI Semibold",18)
            )
        self.thank_screen.place(x=500,y=200,width=600,height=300)

    def _final(self) :
        
        global table_root,tot_price

        #self.screen.destroy()
        
        table_root = Tk()
        columns = ('ITEM', 'QTY', 'PRICE')
        tree = Treeview(
            table_root, 
            columns=columns, 
            show = 'headings'
            )
        
        tree.heading('ITEM', text='ITEM')
        tree.heading('QTY', text='QTY (IN KG)')
        tree.heading('PRICE', text='PRICE (PER KG)')

        items = []
        tot_price = 0
        for i in self.cart :
            items.append([i.getname(), i.getqty(), i.getprice()])
            tot_price += i.getprice()
            items.append([''])
        items.append(['TOTAL', '', f'{tot_price}'])
        for i in items:
            tree.insert('', END,values=i)
        tree.grid(row=0, column=0, sticky='nsew')

        table_root.title("PAYMENT")
        table_root.geometry("900x1000")

        pay_button=Button(table_root,
                text="Proceed to payment",
                command= lambda : self._pay(),
                font=("Segoe UI Semibold",8)
                )

        pay_button.place(x=90,y=250,width=500,height=150)

    def _final_pay(self):
        self.screen.destroy()
        self.pay_screen=LabelFrame(table_root,text="PAYMENT OPTIONS",fg="black",font=("Segoe UI Semibold",10),bg='white')
        self.pay_screen.place(x=500,y=100,width=400,height=400)

        if tot_price >= 100:
            self.Products_frame.destroy()
            
            self.pay_op1=Label(
                self.pay_screen,
                text="Credit card",
                font=("Segoe UI Semibold",12),
                bg='white'
                ).grid(row=0,column=1)

            self.pay_op2=Label(
                self.pay_screen,
                text="Net banking",
                font=("Segoe UI Semibold",12),
                bg='white'
                ).grid(row=8,column=1)

            self.pay_op3=Label(
                self.pay_screen,
                text="g pay",
                font=("Segoe UI Semibold",12),
                bg='white'
                ).grid(row=16,column=1)

            self.pay_but1=Button(
                self.pay_screen,
                text="Click to proceed",
                command= lambda : self._order_num(),
                font=("Segoe UI Semibold",12)
                ).grid(row=0,column=2)

            self.pay_but2=Button(
                self.pay_screen,
                text="Click to proceed",
                command= lambda : self._order_num(),
                font=("Segoe UI Semibold",12)
                ).grid(row=8,column=2)

            self.pay_but3=Button(
                self.pay_screen,
                text="Click to proceed",
                command= lambda : self._order_num(),
                font=("Segoe UI Semibold",12)
                ).grid(row=16,column=2)

        else:
            self.pay=Label(
                self.pay_screen,
                text="Oops! You have to make a purchase worth 100 to proceed!",
                font=("Segoe UI Semibold",10)
                ).grid(row=1,column=0)

    def _pay(self):
        
        
        self.screen=LabelFrame(
            table_root,
            bd=2,
            bg='white',
            relief="groove"
            )

        self.screen.place(x=200,y=200,height=100,width=555)

        self.screen_label=Label(self.screen,
            text="Would you like to proceed to payment ?",
            font=("Segoe UI Semibold",10),
            bg="White",
            fg="black"
            ).grid(row=0,column=1)

        self.yes=Button(
            self.screen,
            text="YES",
            command = lambda : self._final_pay()
            ).grid(row=1,column=1)

        self.no=Button(
            self.screen,
            text="No",
            command= lambda : self._back()
            ).grid(row=1,column=2)


    def display_next(self,item=None) :

        if item != None:
            self.display_item = item
        else:
            self.display_item = self.display_item.getnext()
        
        self.Products_frame.delete('all')

        if self.display_item.getnext().getnext() is  None :
            pass
        else :

            self.next_button = Button(self.canvas,
                image=self.button_image_5,
                borderwidth=0,
                highlightthickness=0,
                bg = 'white',
                command=lambda: self.next(),
                relief="flat"
            )
            self.next_button.place(
                x=773.0,
                y=473.0,
                width=118.78179931640625,
                height=47.0
            )

        self.prev_button  = Button(self.canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            bg = 'white',
            command=lambda: self.prev(),
            relief="flat"
        )
        self.prev_button.place(
            x=773.0,
            y=392.0,
            width=118.78179931640625,
            height=47.0
        )
            
        self.Products_frame.create_text(
            56.0,
            247.0,
            anchor="nw",
            text=f"{self.display_item.getitem().getname()}",
            fill="#000000",
            font=("Inter Bold", 21 * -1)
        )

        self.Products_frame.create_text(
            57.0,
            293.0,
            anchor="nw",
            text=f"Qty:                      Price : ",
            fill="#000000",
            font=("Inter ", 21 * -1)
        )

        self.Products_frame.create_text(
            77.0,
            293.0,
            anchor="nw",
            text=f"     {self.display_item.getitem().getqty()}                               {self.display_item.getitem().getprice()} ",
            fill="#000000",
            font=("Rubik Bold", 21 * -1)
        )

        self.Products_frame.create_text(
            57.0,
            340.0,
            anchor="nw",
            text="Standard Delivery",
            fill="#000000",
            font=("Inter SemiBold", 21 * -1)
        )

        self.Products_frame.create_rectangle(
            395.0,
            320.0,
            613.0,
            376.0,
            fill="green",
            outline="")

        self.Item_frame=LabelFrame(
            self.Products_frame,
            bg = 'white'
            )

        self.Item_frame.place(x=35,y=15,width=400,height=200)

        self.img=Image.open(self.relative_to_assets_pic(f"{self.display_item.getitem().getimg()}"))
        self.resize_img=self.img.resize((395,180))
        self.final_img=ImageTk.PhotoImage(self.resize_img)
        
        self.img_veg=Label(self.Item_frame,image=self.final_img).pack(padx=3,pady=3)

    def next(self) :
        
    
        if self.display_item.getnext().getnext() is  None :
            self.next_button['state'] = DISABLED
        else :
            self.display_next()


    def display_prev(self,item=None) :
        if item != None:
            self.display_item=item
        else:
            self.display_item = self.display_item.getprev()

        self.Products_frame.delete('all')

        if self.display_item.getprev().getprev() is None :
            pass
        else :
            self.prev_button  = Button(self.canvas,
                image=self.button_image_4,
                borderwidth=0,
                highlightthickness=0,
                bg = 'white',
                command=lambda: self.prev(),
                relief="flat"
            )
            self.prev_button.place(
                x=773.0,
                y=392.0,
                width=118.78179931640625,
                height=47.0
            )
        

        self.next_button = Button(self.canvas,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            bg = 'white',
            command=lambda: self.next(),
            relief="flat"
        )
        self.next_button.place(
            x=773.0,
            y=473.0,
            width=118.78179931640625,
            height=47.0
        )

        self.Products_frame.create_text(
            56.0,
            247.0,
            anchor="nw",
            text=f"{self.display_item.getitem().getname()}",
            fill="#000000",
            font=("Inter Bold", 21 * -1)
        )

        self.Products_frame.create_text(
            57.0,
            293.0,
            anchor="nw",
            text=f"Qty:                      Price : ",
            fill="#000000",
            font=("Inter ", 21 * -1)
        )

        self.Products_frame.create_text(
            77.0,
            293.0,
            anchor="nw",
            text=f"     {self.display_item.getitem().getqty()}                               {self.display_item.getitem().getprice()} ",
            fill="#000000",
            font=("Rubik Bold", 21 * -1)
        )

        self.Products_frame.create_text(
            57.0,
            340.0,
            anchor="nw",
            text="Standard Delivery",
            fill="#000000",
            font=("Inter SemiBold", 21 * -1)
        )

        self.Products_frame.create_rectangle(
            395.0,
            320.0,
            613.0,
            376.0,
            fill="green",
            outline="")

        self.Item_frame=LabelFrame(
            self.Products_frame,
            bg = 'white'
            )

        self.Item_frame.place(x=35,y=15,width=400,height=200)

        self.img=Image.open(self.relative_to_assets_pic(f"{self.display_item.getitem().getimg()}"))
        self.resize_img=self.img.resize((390,180))
        self.final_img=ImageTk.PhotoImage(self.resize_img)
        
        self.img_veg=Label(self.Item_frame,image=self.final_img).pack(padx=3,pady=3)


    def prev(self) :
        
        if self.display_item.getprev().getprev() is  None :
            self.prev_button['state'] = DISABLED
        else :
            self.display_prev()
        

    def _search_node(self,item):
        p=self.stock.getfront()
        while p.getitem().getname().upper() != item.upper() :
            p=p.getnext()
        self.display_next(p)

    def _search(self,item=None,p=0):
        if item==None:
            item=self.search_box.get()
        if p==0:
            p=self.b.root
        if p != None:
            if item.lower()==self.b.item(p)[0].lower():
                print("SEARCH",item)
                self._search_node(item)
                
            elif self.b._ord_val(item) < self.b._ord_val((self.b.item(p))[0]):
                self._search(item,self.b.left(p))
            elif self.b._ord_val(item) > self.b._ord_val((self.b.item(p))[0]):
                self._search(item,self.b.right(p))
        else:
            messagebox.showinfo("Search",'Searched vegetable not available')

    

    def _display_all(self):
        self.Products_frame.delete('all')
        self.Products_frame = Canvas(self.canvas,
            height =400,
            width = 634,
            bg="white")
        self.Products_frame.place(x = 52.0, y = 148)
        
        
        canvas=Canvas(self.Products_frame,width= 634, height=400)
        canvas.pack(side=LEFT,fill=BOTH,expand=0)

        scrollbar_y=Scrollbar(self.Products_frame,orient=VERTICAL,command=canvas.yview)
        scrollbar_y.pack(side=RIGHT,fill=Y)
        canvas.configure(yscrollcommand=scrollbar_y.set)
        canvas.bind('<Configure>',lambda e : canvas.configure(scrollregion=canvas.bbox('all')) )
        disp_all_frame= Frame(canvas)
        canvas.create_window((0,0),window=disp_all_frame,anchor='nw')

        for veg in self.stock :

            self.Item_frame=Canvas(
                disp_all_frame,
                bd=2,
                relief= SOLID,
                bg = 'white',
                width= 600,
                height= 300
                )

            
            self.Item_frame.grid(padx = 10, pady = 10)
            self.Item_frame.grid_propagate(False)




            self.button_6 = Button(self.Item_frame,
                image=self.button_image_6,
                borderwidth=0,
                bg = 'green',
                highlightthickness=0,
                command=lambda: print("button_6 clicked"),
                relief="flat"
            ).place(x=470,y=235)

            self.name_veg = Label(
                self.Item_frame,
                text= f"{veg.getname()}",
                font=('Segoe UI Semibold',20),
                bg= 'white',
                ).place(x=420,y=50)

            self.Item_frame.create_rectangle(
                395.0,
                230.0,
                593.0,
                276.0,
                fill="green",
                outline="")


            self.add_veg = Button(self.Item_frame,
                image=self.button_image_8,
                borderwidth=0,
                bg = 'green',
                highlightthickness=0,
                command=lambda a = veg : self._add(a),
                relief="flat"
            ).place(x=420,y=235)

            self.sub_veg = Button(self.Item_frame,
                image=self.button_image_7,
                borderwidth=0,
                bg = 'green',
                highlightthickness=0,
                command=lambda a = veg : self._sub(a),
                relief="flat"
            ).place(x=530,y=235)

            self.qty_veg = Label(self.Item_frame,
                text=f"Qty: {veg.getqty()}           Price : Rs. {veg.getprice()} ",
                bd=1,
                font=('Segoe UI Semibold',20),
                justify="left",
                bg = 'white'
                ).place(x=10,y=230)

            self.img=Image.open(self.relative_to_assets_pic(f"{veg.getimg()}"))
            self.resize_img=self.img.resize((350,180))
            self.final_img=ImageTk.PhotoImage(self.resize_img)
        
        
            self.img_veg=Label(self.Item_frame,image=self.final_img).place(x =20, y = 15)

            self._all_items['state'] = DISABLED
            

root = Tk()
a = Display(root)
root.mainloop()

