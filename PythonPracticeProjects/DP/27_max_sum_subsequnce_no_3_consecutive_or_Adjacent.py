# to find the max subsequence without any 3 consecutive elements from the array .
# As there are 3 elements not  to be consecutive , so their can be 3 case .
# For 3 elements , Excluding any one of them will make the sum as sum of non-consecutive numbers
# exclude 1  -> sum[i] = sum[i-1]
# exclude 2  -> sum[i] = sum[i-2] + a[i]
# exclude 3  -> sum[i] = sum[i-3] + a[i-1] + a[i]
# But here , include 1 is covered in exclude 3 include 3
# include 2 is covered in exclude


def find_max_recursive(a, l):
    sum = [-1] * (l)

    if l >=1 :
        sum[0] = a[0]
    if l >=2:
        sum[1] = a[0]+a[1]

    for i in range(2,l):
        sum_excl_i = sum[i-1]
        sum_excl_i_minus_1 = sum[i-2] + a[i]
        if i ==2:
            sum_excl_i_minus_2 =  a[i-1] + a[i] #sum[i-3] wont exist for i =2
        else:
            sum_excl_i_minus_2 = sum[i-3] + a[i-1] + a[i] #sum[i-3] wont exist for i =2
        sum[i] = max(max(sum_excl_i,sum_excl_i_minus_1),sum_excl_i_minus_2)

    print (sum)
    return  sum[l-1]


# sum of l+1 size for memoized version.
def find_max_memoized(a, l):
    if sum_memo[l] !=-1:
        return sum_memo[l]
    if l ==0:
        sum_memo[0] =0
        return 0
    if l ==1:
        sum_memo[1] = a[0]
        return a[0]
    if l ==2:
        sum_memo[2] = a[0]+ a[1]
        return a[0]+ a[1]
    for i in range(3,l+1):
        sum_excl_i = find_max_memoized(a,i-1)
        sum_excl_i_minus_1 = find_max_memoized(a,i-2) + a[i-1]
        sum_excl_i_minus_2 = find_max_memoized(a,i-3)+ a[i-2] + a[i-1]
        sum_memo[i] =max(max(sum_excl_i,sum_excl_i_minus_1),sum_excl_i_minus_2)
    return sum_memo[l]

if __name__ == "__main__":
    a = [3000, 2000, 1000, 3, 10]
    l = len(a)
    print(find_max_recursive(a,l))

    global sum_memo
    sum_memo = [-1 for i in range(l + 1)]
    print(find_max_memoized(a,l))