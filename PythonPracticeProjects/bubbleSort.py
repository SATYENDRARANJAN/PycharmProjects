def bubblesort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1] =temp
            print (arr)
        print("ww\n")
    return arr


if __name__ =="__main__":
    arr =[19,6,12,5,7,4,2]
    bubbleSort(arr)
