
def bin_search(key , arr):
    l = len(arr)
    low = 0
    high = l
    while (l <=h):
        mid = low +(high -low)/2
        if key ==arr[mid]:
            return mid
        if key < arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return 0



if __name__ =="__main__":
    k =3
    arr =[4,5,7,8,2,3,5,6,3,2,1,3,4,5]
    print(bin_search(k , arr))