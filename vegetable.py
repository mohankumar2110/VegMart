from Deq import Deq
from ArrayList import ArrayList

class Vegetable(object) :
    
    
    def __init__(self, name, qty, display_qty, price, display_price,img='') :
        
        self._name = name
        self._qty = qty
        self._price = price 
        self._img = img
        self._dis_price = display_price
        self._dis_qty = display_qty
        
        
    def getname(self) :
        
        return self._name
    
    def getqty(self) :
        return self._qty
    
    def getprice(self) :
        return self._price
    
    def changeprice(self, new_price) :       
        self._price = new_price
        
    def changeqty(self, new_qty) :
        self._qty = new_qty
    
    def getimg(self) :
        return self._img
    def redqty(self) :
        self._qty -= 1
    def getdisqty(self) :
        return self._dis_qty
    def getdisprice(self) :
        return self._dis_price
    
    
class Cust_item() :
    
    def __init__(self, veg, qty=1) :
        
        self._veg = veg
        self._vegname = veg.getname() 
        self._qty = qty
        self._price = veg.getprice()
        
    def modify_add(self) :
        self._qty += 1

    def modify_red(self) :
        self._qty -= 1
    
    
    def getname(self) :
            
        return self._vegname
    
    def getqty(self) :
        return self._qty
    
    def getprice(self) :
        return self._price*self._qty
        

class Cust_cart() :
    
    def __init__(self) :
        self._items = ArrayList()
        self._name_list = ArrayList()
        self._size = 0
        
    def __len__(self) :
        return self._size
    
    def __getitem__(self, index) :
        return self._items[index]
        
    def add(self, item) :
        
        if item.getname() not in self._name_list :
            self._items.append(item)
            self._name_list.append(item.getname())
            self._size += 1
        else :
            index = self._name_list.index(item.getname()) 
            self._items[index].modify_add()

        
            
    def delete(self, item) :
        self._items.remove(item)

    def sub(self, item) :
        index = self._name_list.index(item.getname()) 

        if self._items[index].getqty() !=0 :
            self._items[index].modify_red()
        else :
            self._items.delete(self._items[index])
        


