import pandas as pd
def Insertion_Sort_Ascending(arr,coloum):
    key=0
    size = len(arr)

    for j in range(1,size):
        key = arr[j][coloum]
        #print(key)
        i=j-1
        while((i>0 or i==0) and arr[i][coloum]>key):
            arr[i+1]=arr[i]
            i=i-1
        arr[i+1]=key
    return 

# descending order insertion_Sort
def Insertion_Sort_Descending(arr,coloum):
    key=0
    size = len(arr)

    for j in range(1,size):
        key = arr[j][coloum]
        #print(key)
        i=j-1
        while((i>0 or i==0) and arr[i][coloum]<key):
            arr[i+1]=arr[i]
            i=i-1
        arr[i+1]=key
    return
# Insertio Sort for Hybrid Quick Sort
def Insertion_Hybrid(arr,low,high,col):
    key=0
    for j in range(low+1,high+1):
        key = arr[j][col]
        i=j-1
        while((i>j or i==j) and arr[i][col]>key):
            arr[i+1]=arr[i]
            i=i-1
        arr[i+1]=key
    return
# Insertio Sort for Hybrid Quick Sort  descending
def Insertion_Hybrid(arr,low,high,col):
    key=0
    for j in range(low+1,high+1):
        key = arr[j][col]
        i=j-1
        while((i>j or i==j) and arr[i][col]<key):
            arr[i+1]=arr[i]
            i=i-1
        arr[i+1]=key
    return            

# Selection Sort
def Selection_Sort_Ascen(arr,colum):
    n=len(arr)

    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if (arr[min][colum]>arr[j][colum]):
                min=j
         # Swapping the elemnts        
        arr[i],arr[min] = arr[min],arr[i]        
    return arr    
# Selection Sort
def Selection_Sort_Dscen(arr,colum):
    n=len(arr)

    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if (arr[min][colum]<arr[j][colum]):
                min=j
         # Swapping the elemnts        
        arr[i],arr[min] = arr[min],arr[i]        
    return arr

#function merge
def Merge_Asce(arr,start,mid,end,colum):
    start -=1
    mid -=1
    end -=1
    left_arr=[]
    right_arr=[]
    for i in range(start,mid+1):
        left_arr.append(arr[i][colum])
    for j in range(mid+1,end+1):
        right_arr.append(arr[j][colum])
    #print(left_arr)
    #print(right_arr)
    i=0
    j=0
    k=start
    for k in range(start,end):
        while i < len(left_arr) and j < len(right_arr):
            if(left_arr[i]<right_arr[j] or left_arr[i]==right_arr[j]):
                arr[k][colum]=left_arr[i]

                i = i+1
            else:
                arr[k][colum]=right_arr[j]
                j=j+1
            k=k+1    
# Checking if any element was left
        while i < len(left_arr):
         #   print("In while")
            arr[k][colum] = left_arr[i]
            i += 1
            k += 1  
        while j < len(right_arr):
            arr[k][colum] = right_arr[j]
            j += 1
            k += 1    
    return
    
#Merge SOrt arry 
def Merge_Sort_Asce(arr,start,end,colum):
    if(start<end):
        mid = (start+end)//2
        Merge_Sort_Asce(arr,start,mid,colum)
        Merge_Sort_Asce(arr,mid+1,end,colum)
        Merge_Asce(arr,start,mid,end,colum)
    else:
        return
#function merge
def Merge_Desc(arr,start,mid,end,colum):
    start -=1
    mid -=1
    end -=1
    left_arr=[]
    right_arr=[]
    for i in range(start,mid+1):
        left_arr.append(arr[i][colum])
    for j in range(mid+1,end+1):
        right_arr.append(arr[j][colum])
    #print(left_arr)
    #print(right_arr)
    i=0
    j=0
    k=start
    for k in range(start,end):
        while i < len(left_arr) and j < len(right_arr):
            if(left_arr[i]>right_arr[j] or left_arr[i]==right_arr[j]):
                arr[k][colum]=left_arr[i]

                i = i+1
            else:
                arr[k][colum]=right_arr[j]
                j=j+1
            k=k+1    
# Checking if any element was left
        while i < len(left_arr):
         #   print("In while")
            arr[k][colum] = left_arr[i]
            i += 1
            k += 1  
        while j < len(right_arr):
            arr[k][colum] = right_arr[j]
            j += 1
            k += 1    
    return

#Merge SOrt arry 
def Merge_Sort_Desc(arr,start,end,colum):
    if(start<end):
        mid = (start+end)//2
        Merge_Sort_Desc(arr,start,mid,colum)
        Merge_Sort_Desc(arr,mid+1,end,colum)
        Merge_Desc(arr,start,mid,end,colum)
    else:
        return 


def convert(arr,colum):
    size = len(arr)
    #print(size)
    for i in range(0,size):
        #print(arr[i][colum])
        time = arr[i][colum].split(" ")
        arr[i][colum] = int(time[0])
        #print(arr[i][colum])
    return arr

# Bubble Sort
def Bubble_Sort_Asc(arr,col):
    control=len(arr)
    for i in range(control-1):
        flag=False
        for j in range(control-1):
            if(arr[j][col]>=arr[j+1][col]):
                arr[j],arr[j+1]=arr[j+1],arr[i]
                flag=True
        if(flag==False):
            break
    return 

# Bubble Sort
def Bubble_Sort_Dsc(arr,col):
    control=len(arr)
    for i in range(control-1):
        flag=False
        for j in range(control-1):
            if(arr[j][col]<=arr[j+1][col]):
                arr[j],arr[j+1]=arr[j+1],arr[i]
                flag=True
        if(flag==False):
            break
    return
    
#Partition Function
def partition_Asc(arr,low,high,col):
    # pi is partitioning index, arr[pi] is now at right place 
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
    # If current element is smaller than the pivot
      if(arr[j][col]<pivot[col]):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
     # Smaller part end and now we swap pivot to its correct place
    arr[i+1],arr[high]=arr[high],arr[i+1] 
    return i+1
#Quick Sort 
def quick_Sort_Asc(arr,low,high,col):
    if(low<high):
        pi=partition_Asc(arr,low,high,col)
        quick_Sort_Asc(arr,low,pi-1,col)
        quick_Sort_Asc(arr,pi+1,high,col) 

#Partition Function Descdening
def partition_Dsc(arr,low,high,col):
    # pi is partitioning index, arr[pi] is now at right place 
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
    # If current element is smaller than the pivot
      if(arr[j][col]>pivot[col]):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
     # Smaller part end and now we swap pivot to its correct place
    arr[i+1],arr[high]=arr[high],arr[i+1] 
    return i+1
#Quick Sort 
def quick_Sort_Dsc(arr,low,high,col):
    if(low<high):
        pi=partition_Dsc(arr,low,high,col)
        quick_Sort_Dsc(arr,low,pi-1,col)
        quick_Sort_Dsc(arr,pi+1,high,col)

# Hybrid Quick Sort (Quick and Insertion)
def Hybrid_Sort(arr,low,high,col):
    while(low<high):
        # First check if the array is smallr enough(less than 10) to apply insertion sort or not
        if(high-low+1<10):
            Insertion_Hybrid(arr,low,high,col)
            break
        else:
            pi=partition_Asc(arr,low,high,col)
            # NOw find out on both sids of pivot that which array is larger so that we can apply 
            # recursive hybridsort on it
            if(pi-low<high-pi):
                Hybrid_Sort(arr,low,pi-1,col)
                low = pi +1
            else:
                Hybrid_Sort(arr,pi+1,high,col)
                high=pi-1

# Hybrid Quick Sort (Quick and Insertion)
def Hybrid_Sort_Desc(arr,low,high,col):
    while(low<high):
        # First check if the array is smallr enough(less than 10) to apply insertion sort or not
        if(high-low+1<10):
            Insertion_Hybrid(arr,low,high,col)
            break
        else:
            pi=partition_Dsc(arr,low,high,col)
            # NOw find out on both sids of pivot that which array is larger so that we can apply 
            # recursive hybridsort on it
            if(pi-low<high-pi):
                Hybrid_Sort_Desc(arr,low,pi-1,col)
                low = pi +1
            else:
                Hybrid_Sort_Desc(arr,pi+1,high,col)
                high=pi-1
# Cocktail Sort
def cocktail_sort_Asc(arr,start,end,col):
    flag=True
    while(flag==True):
        flag=False
        for i in range(start,end):
            if(arr[i][col]>arr[i+1][col]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
                flag = True
        if(flag==False):
            end = end-1
            for i in range(end-1,start-1,-1):
                if(arr[i][col]>arr[i+1][col]):
                    arr[i],arr[i+1] = arr[i+1],arr[i]
                    flag = True
            start =start+1

# Cocktail Sort
def cocktail_sort_Dsc(arr,start,end,col):
    flag=True
    while(flag==True):
        flag=False
        for i in range(start,end):
            if(arr[i][col]<arr[i+1][col]):
                arr[i],arr[i+1] = arr[i+1],arr[i]
                flag = True
        if(flag==False):
            end = end-1
            for i in range(end-1,start-1,-1):
                if(arr[i][col]<arr[i+1][col]):
                    arr[i],arr[i+1] = arr[i+1],arr[i]
                    flag = True
            start =start+1

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
class Tree:
    def __init__(self):
        self.root=None
    def insert_node(self,ddata,root,col):
        if(self.root==None):
            self.root=ddata
        else:
            if(ddata.data[col] < root.data[col] or ddata.data[col] == root.data[col]):
                if(root.left==None):
                    root.left=ddata
                    ddata.parent=root
                else:
                    self.insert_node(ddata,root.left,col)
            elif(ddata.data[col] > root.data[col]):
                if(root.right==None):
                    root.right=ddata
                    ddata.parent=root
                else:
                    self.insert_node(ddata,root.right,col)
    def in_order_traversal(self,node,col,arr):
        if(self.root==None):
            print("tree is empty")
        else:

            if(node.left!=None): 
                self.in_order_traversal(node.left,col,arr)
            arr.append(node.data)
            #print(node.data)
            #print()
            if(node.right!=None):
                self.in_order_traversal(node.right,col,arr)                
        return arr
    def in_order_traversal_Desc(self,node,col,arr):
        if(self.root==None):
            print("tree is empty")
        else:
            if(node.right!=None):
                self.in_order_traversal(node.right,col,arr)
            arr.append(node.data)
            if(node.left!=None): 
                self.in_order_traversal(node.left,col,arr)                            
        return arr




#movies=convert(movies,1)
#movies=Selection_Sort_Ascen(movies,0)
#print(movies[0])
#Insertion_Sort_Ascending(movies,0)
#print()
#print(movies[1])

#Merge_Sort_Desc(movies,1,len(movies),0)
#Bubble_Sort_Asc(movies,0)
#quick_Sort_Asc(movies,0,len(movies)-1,0)
#Hybrid_Sort(movies,0,len(movies)-1,0)
#cocktail_sort_Dsc(movies,0,len(movies)-1,0)
#tt=Tree()
#for i in range(len(movies)):
#    nod = Node(movies[i])
#    tt.insert_node(nod,tt.root,0)
#li=[]    
#li=tt.in_order_traversal_Desc(tt.root,0,li)
#movies=li
#print(movies[0])
#print()
#for i in range(len(li)):
#    print(li[i],end=" " )
