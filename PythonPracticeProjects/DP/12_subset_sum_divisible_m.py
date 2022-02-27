# To find subset sum divisible by n exists in an array or not we need to use the subset sum problem approach .
# The subset sum problem tells us in a cell whether dp[m,n] whether the sum n is possible by using a subset in m .
# Now , we use modulo here and use a property , subset_sum % m == 0 , if subset_sum is divisble by m .
# So , now we update dp[arr[i]%m]==






if __name__ == "__main__":
    arr =[4,5,6,7,8,5]
    print(find_subset_sum_divisible_m(arr, m ,n))