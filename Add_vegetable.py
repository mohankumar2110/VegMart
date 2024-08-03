


from tkinter import *
import csv
from tkinter import filedialog
from tkinter import messagebox

class Add_veg() :



    def __init__(self,root) :
        super().__init__()  

        

        
        self.root = root
        self.root.title("ADD")
        self.f = ('Times', 14)
        self.var = StringVar()
        self.var.set('male')
        self.img_name = ''



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
            text="Enter Vegetable Name", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=0, column=0, sticky=W, pady=10)

        Label(
            self.right_frame, 
            text="Enter Quantity", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=1, column=0, sticky=W, pady=10)

        Label(
            self.right_frame, 
            text="Enter Price", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=2, column=0, sticky=W, pady=10)




        Label(
            self.right_frame, 
            text="Enter Img", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=5, column=0, sticky=W, pady=10)



        self.register_veg_name = Entry(
            self.right_frame, 
            font=self.f
            )

        self.register_veg_qty = Entry(
            self.right_frame, 
            font=self.f
            )

        self.register_veg_price = Entry(
            self.right_frame, 
            font=self.f
            )



        self.register_pwd = Button(
           
            self.right_frame, 
            text = 'Add image',
            font=self.f,
            command= lambda : self.add_img()
            
        )


        self.register_btn = Button(
            self.right_frame, 
            width=15, 
            text='Add', 
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command= lambda: self._add()
        )


        self.register_veg_name.grid(row=0, column=1, pady=10, padx=20)
        self.register_veg_qty.grid(row=1, column=1, pady=10, padx=20) 
        self.register_veg_price.grid(row=2, column=1, pady=10, padx=20)
        self.register_pwd.grid(row=5, column=1, pady=10, padx=20)

        self.register_btn.grid(row=7, column=1, pady=10, padx=20)
        self.right_frame.pack()

    def _add(self) :

        name = self.register_veg_name.get()
        qty = self.register_veg_qty.get()
        price = self.register_veg_price.get()
        img = self.img_name

        with open('Stock.csv','a') as csvfile: 
         
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow([name,qty,price,img])

        messagebox.showinfo('', 'Vegetable added!')
        

    def add_img(self) :
        
        f_types = [('Jpg Files', '*.jpg')]
        self.img_name = filedialog.askopenfilename(filetypes=f_types)


class Del_veg() :



    def __init__(self,root) :
        super().__init__()  

        self.root = root
        self.root.title("DELETE")
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
            text="Enter Vegetable Name", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=0, column=0, sticky=W, pady=10)

        self.register_veg_name = Entry(
            self.right_frame, 
            font=self.f
            )

 
        self.Delete_btn = Button(
            self.right_frame, 
            width=15, 
            text='Delete', 
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command= lambda: self._Del()
        )


        self.register_veg_name.grid(row=0, column=1, pady=10, padx=20)
        self.Delete_btn.grid(row=1, column=1, pady=10, padx=20)
        self.right_frame.pack()

    def _Del(self) :

        name = self.register_veg_name.get()


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

class Mod_veg() :



    def __init__(self,root) :
        super().__init__()  

        self.root = root
        self.root.title("MODIFY")
        self.f = ('Times', 14)
        self.var = StringVar()
        self.var.set('male')
        self.img_name = ''
   



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
            text="Enter Vegetable Name", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=0, column=0, sticky=W, pady=10)

        Label(
            self.right_frame, 
            text="Enter Quantity", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=1, column=0, sticky=W, pady=10)

        Label(
            self.right_frame, 
            text="Enter Price", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=2, column=0, sticky=W, pady=10)




        Label(
            self.right_frame, 
            text="Enter Img", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=5, column=0, sticky=W, pady=10)



        self.mod_veg_name = Entry(
            self.right_frame, 
            font=self.f
            )

        self.mod_veg_qty = Entry(
            self.right_frame, 
            font=self.f
            )

        self.mod_veg_price = Entry(
            self.right_frame, 
            font=self.f
            )



        self.mod_pwd = Button(
           
            self.right_frame, 
            text = 'Add image',
            font=self.f,
            command= lambda : self.add_img()
            
        )


        self.mod_btn = Button(
            self.right_frame, 
            width=15, 
            text='Modify', 
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command= lambda: self._Mod()
        )


        self.mod_veg_name.grid(row=0, column=1, pady=10, padx=20)
        self.mod_veg_qty.grid(row=1, column=1, pady=10, padx=20) 
        self.mod_veg_price.grid(row=2, column=1, pady=10, padx=20)
        self.mod_pwd.grid(row=5, column=1, pady=10, padx=20)

        self.mod_btn.grid(row=7, column=1, pady=10, padx=20)
        self.right_frame.pack()


        

    def add_img(self) :
        
        f_types = [('Jpg Files', '*.jpg')]
        self.img_name = filedialog.askopenfilename(filetypes=f_types)

    def _Mod(self) :

        name = self.mod_veg_name.get()
        qty = self.mod_veg_qty.get()
        price = self.mod_veg_price.get()
        img = self.img_name


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

                    


        
        







        
