# max diff of zeroes and ones in binary string in O(n) times .
# convert all 0's to 1s AND all 1's to -1's

# let length be 0 in the beginning , when we encounter 0 we need to increase lenght by 1 and when we encounter 1 , we need to decrease lenght by 1
# so it basically becomes a max sum subarry problem with 1's in place of 0; and -1's in place of 1;s

def findLength(s, n):
    max_sum =0
    curr_sum =0
    for i in range(n):
        next_ele = 1 if s[i] == '0' else -1
        curr_sum += next_ele
        if curr_sum <0:
            curr_sum = 0
        if curr_sum > max_sum :
            max_sum = curr_sum
    return max_sum




def findLength1(string, n):
    current_sum = 0
    max_sum = 0

    # traverse a binary string from left
    # to right
    for i in range(n):

        # add current value to the current_sum
        # according to the Character
        # if it's '0' add 1 else -1
        current_sum += (1 if string[i] == '0' else -1)

        if current_sum < 0:
            current_sum = 0

        # update maximum sum
        max_sum = max(current_sum, max_sum)

        # return -1 if string does not contain
    # any zero that means all ones
    # otherwise max_sum
    return max_sum if max_sum else 0


# DP approach
# Python Program to find the length of
# substring with maximum difference of
# zeroes and ones in binary string.
MAX = 100


# Return true if there all 1s
def allones(s, n):
    # Checking each index
    # is 0 or not.
    co = 0

    for i in s:
        co += 1 if i == '1' else 0

    return co == n


# Find the length of substring with
# maximum difference of zeroes and
# ones in binary string
def findlength(arr, s, n, ind, st, dp):
    # If string is over
    if ind >= n:
        return 0

    # If the state is already calculated.
    if dp[ind][st] != -1:
        return dp[ind][st]

    if not st:
        dp[ind][st] = max(arr[ind] +
                          findlength(arr, s, n, ind + 1, 1, dp),
                          (findlength(arr, s, n, ind + 1, 0, dp)))
    else:
        dp[ind][st] = max(arr[ind] +
                          findlength(arr, s, n, ind + 1, 1, dp), 0)

    return dp[ind][st]


# Returns length of substring which is
# having maximum difference of number
# of 0s and number of 1s
def maxLen(s, n):
    # If all 1s return -1.
    if allones(s, n):
        return -1

    # Else find the length.
    arr = [0] * MAX
    for i in range(n):
        arr[i] = 1 if s[i] != '0' else -1

    dp = [[-1] * 3 for _ in range(MAX)]
    return findlength(arr, s, n, 0, 0, dp)



if __name__ == "__main__":
    # Driven Program
    # s = "11000010001"
    # s = "00111101110"
    s = "00111101110"
    n = 11
    print(findLength(s, n))
    print((maxLen(s,n)))