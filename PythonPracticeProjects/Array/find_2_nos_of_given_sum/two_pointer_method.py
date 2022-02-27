

def find_2_nos_of_given_sum(a,k):
    ptr1=0
    ptr2=len(a)-1
    list=[]
    while(ptr1<=ptr2):
        if a[ptr1]+a[ptr2]>k:
            ptr2-=1
        elif a[ptr1]+a[ptr2]<k:
            ptr1+=1
        else:
            list.append(str(a[ptr1])+ " " + str(a[ptr2]))
            ptr1+=1
    return list


if __name__ == "__main__":
    a =[2,3,4,5,18,1,-9]
    a.sort()
    k=9
    print(find_2_nos_of_given_sum(a,k))