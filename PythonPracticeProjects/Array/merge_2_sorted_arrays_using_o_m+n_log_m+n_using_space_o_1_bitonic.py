"""
uSING SHELL SORT's merge with Gap .
CHoosing gap to be ceil((m+n)/2)
then gap = gap/2 each time .

"""

def calc_gap(gap):
    if gap <=1:
        return 0
    gap = gap//2 + gap%2;
    return gap


def sort(arr1 , arr2 , len1 , len2):

    gap = calc_gap(len1)
    x = min(len1, len2)
    print("gap :{0} , min :{1}".format(gap, x))
    # form bitonic array .
    #sort 1 and 2 with gap using shell sort . // forming
    for i in range(0,x):
        if arr1[len1-i-1] > arr2[i]:
            arr1[len1-i-1],arr2[i]= arr2[i],arr1[len1-i-1]

    print("arr1 : {0}".format(arr1))
    print("arr2 : {0}".format(arr2))

    #sort 1
    while gap > 0:
        for i in range(gap ,len1):
            print("comparing {0} .. {1}--{2}".format(i ,gap , i-gap))
            if arr1[i] > arr1[i-gap]:
                print("in ")
                arr1[i], arr1[i-gap] = arr1[i-gap], arr1[i]
                print(arr1)
            i += 1
        gap = calc_gap(gap)

    # sort arr2
    while gap > 0:
        for i in range(gap , len2):
            if arr2[i] > arr2[i-gap]:
                arr2[i],arr2[i-gap] = arr2[i-gap],arr2[i]
            i +=1
        gap = calc_gap(gap)

    print ("arr1 : {0}".format(arr1))
    print ("arr2 : {0}".format(arr2))



if __name__ =="__main__":
    arr1 =[3,4,56,78,99]
    arr2=[3,5,6]
    sort(arr1 , arr2,len(arr1),len(arr2))