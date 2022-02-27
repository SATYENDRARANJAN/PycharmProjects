# if a no  divisible y 2 ,3, 5 beacoms 1 , then its an ugly number .
# n =n% 2 -->
# n = n% 3 -->
# 1,2 3,4 ,5 ,6,

# TO FIND NTH UGLY NUMBER
# Find the ugly numbers divisible by 2 and then 3 and then 5 .
# top down or memoization approach is not possible because  the we dont know where to start .
# bottom up approach suggests we calculate next multiples of 2 , 3, and 5 and choose the smallest one to

# 1,2,3,4,5,6,8,9,10,


# 1 -> A[1]*2           , 1*3          , 1*5                    i1 = 0 , i2 = 0 , i3 =0 min = A[1] = 2
# 2 -> 2*2              , A[1]*3       , 1*5                    i1 =1 , min = A[2] = 3
# 3 -> A[2]*2=6         , 2*3          , 1*5                    min = A[3] = 4
# 3 -> A[2]*2=6         , 2*3          , A[1]*5 =10             min = A[4] = 5
# 3 -> A[3]*2=8         , 2*3          , A[1]*5 =10             min = A[5] = 6
# 3 -> A[4]*2=10        , 2*3          , 1*5                    min = A[6] = 8
# 3 -> A[4]*2=10        , 2*3          , 1*5                    min = A[6] = 9
# 4 -> 2*2*2 , 3*3 , *5 min = A[4] = 5
# 4 -> 2*2*2 , 3*3 , 1*5 min = A[5] = 6
# 5 -> 2*2*2*2 , 3*3 , 2*5 = min = A[6] = 8
# ...  there on calculating i1 ,i2 ,i3
# and then choosing the minimum of them
# and multiplying the min by 2
# increase the counter .

def find_the_150th_ugly_no():

    ugly_arr = [0] * 150
    i2 = i3 = i5 =0

    n2 = 2
    n3 = 3
    n5 = 5
    count =0
    min_i=0
    while count<=149:
        min_i = min(n2 , n3 , n5)

        ugly_arr[count] = min_i
        if n2 == min_i:
            n2 = ugly_arr[i2] * 2
            i2 =i2 + 1
        if n3 == min_i:
            n3 = ugly_arr[i3] * 3
            i3 = i3 + 1
        if n5 == min_i:
            n5 = ugly_arr[i5] * 5
            i5 = i5 + 1

        count = count + 1
    print(ugly_arr[149])
    print(ugly_arr)


if __name__ == "__main__":
    print(find_the_150th_ugly_no())