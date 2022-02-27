

def bin_search(a,l ,h , key):
    # find mid point
    # if < , find in left half
    # if > find in right
    # if = , return mid
    # if st >end , retunr null
    if (l==h):
        if a[l] == key :
            return l
        else :
            return  "Not found"
    mid = l + (h-l)//2
    if key == a[mid]:
        return mid
    if key < a[mid]:
        return bin_search(a,l,mid-1,key)
    return bin_search(a,mid+1,h,key)






if __name__ == "__main__":
    arr  =[2,3,4,5,6,7,8,8,9,6,5,4,3]
    key = 3
    print(bin_search(arr, 0  , len(arr)-1,  key ))
