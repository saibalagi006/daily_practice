from email.errors import NonPrintableDefect


class binarysearchtreeNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

    def insert(self,data):
        if(self.val==data):
            return 
        elif(data<self.val):
            if(self.left is not None):
                self.left.insert(data)
            else:
                self.left = binarysearchtreeNode(data)
        
        elif(data>self.val):
            if(self.right is not None):
                self.right.insert(data)
            else:
                self.right = binarysearchtreeNode(data)

    def search(self,data):
        if(self.val==data):
            return True
        elif(data<self.val):
            if(self.left is not None):
                return self.left.search(data)
            else:
                return False
        elif(data>self.val):
            if(self.right is not None):
                return self.right.search(data)
            else:
                return False

    def in_order_traversal(self):
        ele = []
        if(self.left is not None):
            ele+=self.left.in_order_traversal()
        ele.append(self.val)
        if(self.right is not None):
            ele+=self.right.in_order_traversal()
        return ele 
    
    def find_max(self):
        if(self.right is None):
            return self.val
        return self.right.find_max()
    
    def find_min(self):
        if(self.left is None):
            return self.val
        return self.left.find_min()

    def delete(self,data):
        if(data<self.val):
            if(self.left is not None):
                self.left = self.left.delete(data)
        elif(data>self.val):
            if(self.right is not None):
                self.right = self.right.delete(val)
        else:
            if(self.left is None and self.right is None):
                return None
            elif(self.left is None):
                return self.right 
            elif(self.right is None):
                return self.left 
            else:
                min_val = self.right.find_min()
                self.right = min_val
                self.right = self.right.delete(min_val)
        return self 

def build_binarytree(list1):
    root = binarysearchtreeNode(list1[0])
    for i in range(1,len(list1)):
        root.insert(list1[i])
    return root 

if __name__=="__main__":
    list1 = [9,8,7,6,5,4,3,2,1]
    root = build_binarytree(list1)
    print(root.search(9))
    print(root.in_order_traversal())
    root.delete(6)
    print(root.in_order_traversal())
    root.delete(16)
    print(root.in_order_traversal())
    print(root.find_max())
    print(root.find_min())


