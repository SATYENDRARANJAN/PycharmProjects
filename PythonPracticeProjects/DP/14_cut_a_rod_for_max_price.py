# This problem is about cutting a rod in pieces so that all piece's price sums up to be maximum .
# We start by cutting the first part of each integer length
# and then finding the subparts recursively.

# rod_price = [1, 5, 8, 9, 10, 17, 17, 20]

def cutrod(price,l):
    if l==0 :
        return 0,[]
    max_price =0
    list =[]
    price1 =p1=0
    max_ind =[]
    print("l: ",l)
    for i in range(1,l+1):
        print("further Cutting first rod into  : ",i,l-i)
        price1,list = cutrod(price,l-i)
        print("price1,list,i:",price1,list,i)
        p1 = price[i-1] + price1
        print("p1:{4} + {5} = {0} ,l:{1} ,l-i:{2} ,i:{3} ".format(p1,l,l-i,i,price[i-1],price1))
        if p1>max_price:
            max_price =p1
            max_list = list
            max_ind =[i]
            print("2.1:", max_price, max_ind, max_list)

    list = max_ind+max_list
    print("2 ********** :",max_price,list,max_list)
    return max_price,list





def find_max_price(l , price_arr):
    max_price =0
    max_list =[]
    price1 =p1=0
    max_index =[]

    for i in range(1,l+1):
        print("Cutting first rod of : ",l-i)
        price1,list =  cutrod(price_arr , l-i)
        price = price_arr[i-1] + price1
        if price > max_price:
            max_price = price
            max_index  = [i]
            max_list = list
    list = max_index +max_list
    print("3:",max_price,list)




def cutrod_memo(price_arr,l,dpmemo):
    max_price = 0
    max_list =list = []
    price1 = p1 =0
    max_ind=[]
    if l ==0 :
        dpmemo[0] = 0,[]
        return 0,[]
    if dpmemo[l][0] !=-1:
        print("dpmemo[l]: ",dpmemo[l])
        return dpmemo[l]

    else:
        for i in range(1,l+1):
            price , list = cutrod_memo(price_arr, l-i,dpmemo)
            p1 = price_arr[i-1] + price
            if p1>max_price :
                max_price  = p1
                max_list =list
                max_ind = [i]
        dpmemo[l] = max_price,(max_ind + max_list)
    return dpmemo[l]




def find_max_price_memoized(l , price_arr):
    max_price = price = 0
    max_ind =[]
    max_list =list = []

    # dpmemmo stores max sum of the price till ith subscript in the array
    dpmemo = [ (-1,[]) for i in range(l+1)]
    for i in range(1,l+1):
        price,list =cutrod_memo(price_arr ,l-i, dpmemo)
        p1 = price_arr[i-1] + price

        if p1 > max_price:
            max_price = p1
            max_list = list
            max_ind = [i]
    list =max_ind + max_list
    return max_price , list



if __name__ == "__main__":
    rod_length = 8
    rod_price=[1,5,8,9,10,18,23,20]
    print([1]+[2])
    # print(find_max_price(rod_length,rod_price))
    print(find_max_price_memoized(rod_length,rod_price))