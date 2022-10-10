class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_node(self,data):
        if(self.data==data):
            return
        elif(data<self.data):
            if(self.left is not None):
                self.left.add_node(data)
            else:
                self.left = BinarySearchTreeNode(data)
        elif(data>self.data):
            if(self.right is not None):
                self.right.add_node(data)
            else:
                self.right = BinarySearchTreeNode(data)
    def search(self,val):
        if(self.data==val):
            return True
        elif(val<self.data):
            if(self.left is not None):
                return self.left.search(val)
            else:
                return False
        else:
            if(self.right is not None):
                return self.right.search(val)
            else:
                return False
    
    def in_order_traversal(self):
        elements = []
        if(self.left is not None):
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if(self.right is not None):
            elements+=self.right.in_order_traversal()
        return elements
    
    def find_max(self):
        if(self.right is None):
            return self.data
        else:
            return self.right.find_max()
    
    def find_min(self):
        if(self.left is None):
            return self.data
        else:
            return self.left.find_min()
    
    def delete_node(self,val):
        if(val<self.data):
            if (self.left is not None):
                self.left = self.left.delete_node(val)
        elif(val>self.data):
            if (self.right is not None):
                self.right = self.right.delete_node(val)
        else:
            if(self.left is None and self.right is None):
                return None
            elif(self.left is None):
                return self.right
            elif(self.right is None):
                return self.left 
            else:
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete_node(min_val)
        return self

def create_bst(list1):
    root = BinarySearchTreeNode(list1[0])
    for i in range(1,len(list1)):
        root.add_node(list1[i])
    return root

if __name__=="__main__":
    list1 = [1,3,2,4,5,63]
    root = create_bst(list1)
    root.add_node(67)
    print(root.in_order_traversal())
    root.delete_node(3)
    print(root.in_order_traversal())
    print(root.find_max())
    print(root.find_min())
            