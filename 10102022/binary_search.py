def bsearch(seq,v,l,r):
    if(r-l==0):
        return False
    else:
        mid = (l+r)//2
        if(seq[mid]==v):
            return True
        elif(v<seq[mid]):
            return bsearch(seq,v,l,mid)
        elif(v>seq[mid]):
            return bsearch(seq,v,mid+1,r)
    
if __name__ == "__main__":
    elements = [1,2,3,4,5,6]
    print(bsearch(elements,-2,0,len(elements)))
    print(bsearch(elements,3,0,len(elements)))
    print(bsearch(elements,6,0,len(elements)))

