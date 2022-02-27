#put a marker after the sorted section
# compare the unsorted with the sorted .
def insertionsort(a):

    for i in  range(1,len(a)):
        ptr = a[i]
        for j in reversed(range(0, i)):
            if a[j] > ptr:
                a[j+1] =a[j]
            else:
                break
        a[j] =ptr
    print(a)


if __name__=="__main__":
    a =[12,24,21,12,34,56,64,34,56,66,64,33,33,33,45,64]
    insertionsort(a)