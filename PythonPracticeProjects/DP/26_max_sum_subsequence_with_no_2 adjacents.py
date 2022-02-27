# In this problem , we have an array and we need to find the max sum with no 2 adj in the subsequence .
# We calculate the sum by including and excluding the last element .


def find_max(a):
    l = len(a)
    incl_prev = 0
    excl_prev = 0
    for i in range(l):
        excl_curr = max(incl_prev,excl_prev)
        incl_curr = excl_prev  + a[i]
        incl_prev = incl_curr
        excl_prev = excl_curr
    return max(incl_curr,excl_curr)



if __name__ == "__main__":
    a = [3,4,5,6,7,9,4]
    print(find_max(a))