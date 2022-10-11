### In this file, we are going to implement insertion sort and selection sort 

class sorting:
    def __init__(self,array1):
        self.array1 = array1
    
    def insertion_sort(self):
        a = self.array1.copy()
        for j in range(2,len(a)):
            key = a[j]
            i=j-1
            while (i>0 and a[i]>key):
                a[i+1]=a[i]
                i=i-1
            a[i+1]=key
        return a
    
    def selection_sort(self):
        l = self.array1.copy()
        for start in range(len(l)):
            minpos = start 
            for j in range(start,len(l)):
                if(l[j]<l[minpos]):
                    minpos = j
            l[start],l[minpos] = l[minpos],l[start]
        return l

if __name__ == "__main__":
    s = sorting([1,3,2,4,5,6])
    print(s.insertion_sort())
    print(s.array1)
    print(s.selection_sort())
