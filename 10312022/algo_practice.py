### Binary Search 

def bsearch(seq,v,l,r):
    if(r-l==0):
        return False
    mid = (l+r)//2
    if(seq[mid]==v):
        return True
    elif(seq[mid]>v):
        return bsearch(seq,v,l,mid)
    elif(seq[mid]<v):
        return bsearch(seq,v,mid+1,r)

def insertion_sort(a):
    for j in range(1,len(a)):
        key = a[j]
        i = j-1
        while(i>-1 and a[i]>key):
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key

def selection_sort(l):
    for start in range(len(l)):
        minpos = start
        for i in range(start,len(l)):
            if(l[i]<l[minpos]):
                minpos = i
        l[start], l[minpos] = l[minpos], l[start]

def quicksort(a,l,r):
    if(r-l<=1):
        return a[l:r]
    yellow = l+1
    for green in range(l+1,r):
        if(a[green]<=a[l]):
            a[yellow],a[green] = a[green], a[yellow]
            yellow = yellow+1
    a[l],a[yellow-1] = a[yellow-1],a[l]
    quicksort(a,l,yellow-1)
    quicksort(a,yellow,r)

class stack:
    def __init__(self):
        self.stack1 = []
    def push(self,ele):
        self.stack1.append(ele)
    def pop(self):
        if(len(self.stack1)<1):
            return None
        else:
            self.stack1.pop()
    def len(self):
        return len(self.stack1)
    def print(self):
        print(self.stack1)

class queue:
    def __init__(self):
        self.queue1 = []
    def enqueue(self,ele):
        self.queue1.append(ele)
    def dequeue(self):
        if(len(self.queue1)<1):
            return None
        self.queue1.pop(0)

    def queue_len(self):
        print(len(self.queue1))
    
    def print_queue(self):
        print(self.queue1)


        


def merge(a,b):
    c=[]
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    while(i+j<m+n):
        if(i==m):
            c.append(b[j])
            j = j+1
        elif(j==n):
            c.append(a[i])
            i = i+1
        elif(a[i]<=b[j]):
            c.append(a[i])
            i = i+1
        elif(a[i]>b[j]):
            c.append(b[j])
            j = j+1
    return c

def merge_sort(a,l,r):
    if(r-l<=1):
        return a[l:r]
    if(r-l>1):
        mid = (l+r)//2
        left = merge_sort(a,l,mid)
        right = merge_sort(a,mid,r)
        return merge(left,right)

class binarysearchtree:
    def __init__(self):
        


if __name__ == "__main__":
    list1 = [1,3,4,5,6]
    list2 = [2,1,43,53,543,9]
    list3 = [9,8,7,6,5,4,3,2,1]
    list4 = [6,5,4,3,2,1,0]
    list5 = [90,80,70,60]
    v = 0
    print(bsearch(list1,v,0,len(list1)))
    insertion_sort(list2)
    print(list2)
    print("list before sorting",list3)
    selection_sort(list3)
    #print(list3)
    print("list after sorting",list3)
    k = merge_sort(list4,0,len(list4))
    print(k)
    (quicksort(list5,0,len(list5)))
    print(list5)
    s = stack()
    s.push(5)
    s.push(4)
    s.push(1)
    s.print()
    s.pop()
    s.pop()
    s.print()
    s.pop()
    s.pop()
    s.print()
    q = queue()
    q.enqueue(4)
    q.enqueue(6)
    q.enqueue(8)
    q.print_queue()
    q.dequeue()
    q.dequeue()
    q.print_queue()
    q.queue_len()
    q.dequeue()
    q.dequeue()
    q.print_queue()