import sys
import math
class heap:
    def __init__(self):
        self.heap = []
        self.heap.append(sys.maxsize)
        self.heapsize=0
    def left(self,i):
        return 2*i
    def right(self,i):
        return 2*i+1.
    def parent(self,i):
        return math.ceil(i/2)
    def max_heapify(self,i):
        l = self.left(i)
        r = self.right(i)
        if(l<=self.heapsize and self.heap[l]>self.heap[i]):
            largest = l
        else:
            largest = i
        if(r<self.heapsize and self.heap[r]>self.heap[largest]):
            largest = r
        if(largest!=i):
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]
            self.max_heapify(self,largest)
    def build_maxheap(self):
        self.heapsize = len(self.heap)
        for i in range(math.floor(len(self.heap)),0,-1):
            self.max_heapify(i)
    def heap_sort(self):
        self.build_maxheap()
        for i in range(len(self.heap),0,-1):
            self.heap[self.heapsize],self.heap[1] = self.heap[1],self.heap[self.heapsize]
            self.heapsize = self.heapsize-1
            self.max_heapify(1)
    def max(self):
        return self.heap[1]
    def extract_max(self):
        if(self.heapsize<1):
            print("underflow")
        else:
            max = self.heap[1]
            self.heap[1] = self.heap[self.heapsize]
            self.heapsize = self.heapsize -1
            self.max_heapify(1)
    def increase_key(self,i,key):
        if(self.heap[i]>key):
            print("new key is lower than existing key")
        else:
            self.heap[i] = key
            while(i>1 and self.heap[i]>self.heap[self.parent(i)]):
                self.heap[i],self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
                i = self.parent(i)
            
    def insert(self,key):
        self.heapsize = self.heapsize+1
        self.heap.append(-1*sys.maxsize)
        self.increase_key(self.heapsize,key)

    def print(self):
        print("heap array is ",self.heap)

if __name__ == "__main__":
    a = heap()
    a.insert(3)
    a.insert(4)
    a.insert(1)
    a.heap_sort()