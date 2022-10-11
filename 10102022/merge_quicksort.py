## merge sort 

def merge(a,b):
    i=0 
    j=0
    m = len(a)
    n = len(b)
    c=[]
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
    elif(r-l>1):
        mid = (l+r)//2
        left = merge_sort(a,l,mid)
        right = merge_sort(a,mid,r)
        return merge(left,right)

def quicksort(a,l,r):
    if(r-l<=1):
        return a[l:r]
    elif(r-l>1):
        yellow = l+1
        for green in range(l+1,r):
            if(a[green]<a[l]):
                a[yellow],a[green]=a[green],a[yellow]
                yellow = yellow+1
        a[l],a[yellow-1] = a[yellow-1],a[l]
        quicksort(a,l,yellow-1)
        quicksort(a,yellow,r)

if __name__=="__main__":
    ele = [8,6,5,3,2,2]
    print(merge_sort(ele,0,len(ele)))
    ele1 = [9,8,5,3,2,2,1]
    quicksort(ele1,0,len(ele1))
    #print(ele)
    print(ele1)
