

def find_max_sum(a):
    n = len(a)
    dp = [0] * (n)
    dp[0] = a[0]
    dp[1] = a[1]
    for i in range(2,n):
        print (i)
        dp[i] = max(dp[i-2]+a[i],dp[i-1])
    return dp[n-1]


# in O(1) space
def find_max_sum_less_space(a):
    n = len(a)
    # for 0th element
    sum_after_incl_prev_element = a[0]
    sum_after_excl_prev_element = 0
    sum_after_excl_curr_element = 0
    sum_after_incl_curr_element = 0
    for i in range(1,n):
        sum_after_excl_curr_element = sum_after_incl_prev_element
        sum_after_incl_curr_element = sum_after_excl_prev_element + a[i]
        # for next iteration
        sum_after_incl_prev_element = sum_after_incl_curr_element
        sum_after_excl_prev_element = sum_after_excl_curr_element
    return max(sum_after_excl_curr_element,sum_after_incl_curr_element)






if __name__ == "__main__":
    a = [5,  5, 10, 40, 50, 35]
    print(find_max_sum(a))
    print(find_max_sum_less_space(a))