
from Deq import Deq,DNode
import ctypes
import csv


class Node:
    def __init__(self,left=None,item=None,right=None,parent=None):
        self._item=item
        self._left=left
        self._right=right
        self._parent=parent

class BST():
    def __init__(self):

        self.root=Node(item=None)
        
        with open("Stock.csv", "r") as f :
            reader = csv.reader(f)
            for i in reader :
                self._data=i
                if i == [] :
                    continue
                else : 
                    
                    self.c=self._ord_val(i[0])
                    self.add(i)

    
    def _ord_val(self,item):
        c=0
        for i in item:
            c+=ord(i.lower())
        print(item,c)
        return c

    def _root(self):
        return self.root._item

    def parent(self,p):
        return p._parent

    def item(self,p):
        return p._item

    def left(self,p):
        return p._left

    def right(self,p):
        return p._right

    def isroot(self,p):
        if self.parent(p) == None:
            return True
        else:
            return False

    def isleaf(self,p):
        if self.left(p)==None and self.right(p)==None:
            return True
        else:
            return False

    def numchildren(self,p):
        if self.left(p)==None and self.right(p)==None:
            return 0
        elif self.left(p)==None and self.right(p) !=None:
            return 1
        elif self.left(p)!=None and self.right(p)==None:
            return 1
        else:
            return 2

    def sibling(self,p):
        if self.isroot(p)==True:
            return None
        else:
            par=self.parent(p)
            if p._item==self.left(par)._item:
                return self.rightsib(p)
            elif p._item==self.right(par)._item:
                return self.leftsib(p)
            else:
                return None

    def leftsib(self,p):
        if self.isroot(p)==True:
            return None
        par=self.parent(p)
        return self.right(par)._item

    def rightsib(self,p):
        if self.isroot(p)==True:
            return None
        par=self.parent(p)
        return self.left(par)._item

    def children(self,p):
        if self.numchildren(p)==2:
            return [self.left(p)._item,self.right(p)._item]
        elif self.left(p)==None:
            return self.right(p)._item
        elif self.left(p)==None:
            return self.right(p)._item
        else:
            return "No children"

    def addroot(self,inp):
        if self.root._item==None:
            new_node=Node(item=inp)
            self.root=new_node
            print("Root",self.root._item)
            return self.root
        else:
            return "Root already exists"

    def add(self,item,p=None):
        
        if p==None:
            p=self.root
        if self.root._item==None:
            self.addroot(item)
        elif self.c < self._ord_val((self.item(p))[0]):                   
            return self.addleft(item,p)                       
        else:
            return self.addright(item,p)

    def addleft(self,item,p):
        if self.left(p)==None:
            new_node=Node(item=item,parent=p)
            p._left=new_node
            print("Left",p._item,p._left._item)
        else:
            self.add(item,self.left(p))
        return p._left

    def addright(self,item,p):
        if self.right(p)==None:
            new_node=Node(item=item,parent=p)
            p._right=new_node
            print("Right",p._item,p._right._item)
        else:
            self.add(item,self.right(p))
        return p._right

    def height(self,p=0):
        
        if p==None:
            return -1
        else:
            if p._left==None and p._right==None:
                return 0
            elif p._left != None or p._right != None:
                return 1+max(self.height(p._left),self.height(p._right))

    def depth(self,p):
        if self.isroot(p)=="Root":
            return 0
        else:
            return 1+self.depth(self.parent(p))

    def preorder(self,p,l=[]):
        print(p._item)
        l.append(p)
        if self.left(p) != None:
            self.preorder(self.left(p))
        if self.right(p) !=None:
             self.preorder(self.right(p))

        return l

    def postorder(self,p=0):
        if p==0:
            p=self.root
        if self.left(p) != None:
            self.postorder(self.left(p))
        if self.right(p) !=None:
             self.postorder(self.right(p))
        print(p._item)
        

        

    def inorder(self,p=0,l=[]):
        if p==0:
            p=self.root
        if self.left(p) != None:
            self.inorder(self.left(p),l)
        #print(p._item)
        l.append(p)
        if self.right(p) !=None:
             self.inorder(self.right(p),l)
        
        return l

    def mini(self,p=0):
        if p==0:
            p=self.root
        if self.left(p) != None:
            return self.mini(self.left(p))
        else:
            self.min_node=p
            print(self.item(p))
            return p
            
    def max(self,p=0):
        if p==0:
            p=self.root
        if self.right(p) != None:
            return self.max(self.right(p))
        else:
            self.max_node=p
            print(self.item(p))

    def search(self,item,p=0):
        if p==0:
            p=self.root
        if item==self.item(p):
            print("Search",item)
        elif self._ord_val(item) < self._ord_val((self.item(p))[0]):
            self.search(item,self.left(p))
        elif self._ord_val(item) > self._ord_val((self.item(p))[0]):
            self.search(item,self.right(p))
        else:
            print("Item Not Found")

    def _print(self):
        print(self._l_items)
        print(self._ord_items)
