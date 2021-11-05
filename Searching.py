from numpy import fabs
import pandas as pd
def Search_StartWith(arr,item,col):
    newArr =[]
    size = len(arr)
    for i in range(size):
        entit_size=len(arr[i][col])
        k=0
        flag=False
        count=0
        #print(arr[i][col])
        if(entit_size<len(item)):
            i+=1
        else:    
            for j in range(entit_size):
                #print("in j loop")
                while(k!=len(item)):
                    #print("in k loop")
                    if(arr[i][col][j]==item[k]):
                        count+=1
                        k+=1
                        j=j+1
                        #print("k is "+str(k))
                        #print("j is "+str(j))
                        #print(count)
                        if(count==len(item)):
                            flag = True
                    elif(arr[i][col][j]!=item[k]):
                        k+=1
                        j+=1
                    else:
                        print()
                            
                if(flag==True):
                    print("going to add")
                    newArr.append(arr[i])
                    break
                elif(flag==False):
                    break
    return newArr

def End_Search(arr,item,col):
    new_list=[]
    size = len(arr)
    size_entit=len(item)    
    for i in range(size):
        s = len(arr[i][col])
        if(s<size_entit):
            
            i+=1
        else:
            t=(s-size_entit)
            if(t>=size_entit):
                k=0
                count=0
                flag=False
                for j in range(t,s):
                    while(k!=len(item)):
                        if(arr[i][col][j]==item[k]):
                            k+=1
                            j+=1
                            count+=1
                            if(count==size_entit):
                               flag = True
                        elif(arr[i][col][j]!=item[k]):
                            k+=1
                            j+=1
                        else:
                            print()
                    if(flag==True):
                        new_list.append(arr[i])
                        break
                    elif(flag==False):
                        break
            else:
                
                i+=1                
    return new_list        

def Simple_Search(arr,item,col):
    new_lit=[]
    for i in range(len(arr)):
        if(arr[i][col]==item):
            new_lit.append(arr[i])
    return new_lit        

# df = pd.read_csv("MoviesScraped.csv")
# movie=[]
# movie = df.values.tolist()
# print(movie[0])
# kl = Search_StartWith(movie,"Dun",0)
# print(kl)
