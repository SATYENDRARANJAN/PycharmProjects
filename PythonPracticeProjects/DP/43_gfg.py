# Python3 Program to find number of ways to
# which numbers that are greater than
# given number can be added to get sum.
MAX = 100


# Return number of ways to which numbers
# that are greater than given number can
# be added to get sum.

def numberofways(n, m):
    dp = [[0 for i in range(n+2)]for j in range(n+2)]

    dp[0][n + 1] = 1

    # Filling the table. k is for numbers
    # greater than or equal that are allowed.
    for k in range(n, m - 1, -1):

        # i is for sum
        for i in range(n + 1):

            # initializing dp[i][k] to number
            # ways to get sum using numbers
            # greater than or equal k+1
            dp[i][k] = dp[i][k + 1]

            # if i > k
            if (i - k >= 0):
                dp[i][k] = (dp[i][k] + dp[i - k][k])
            print(dp)

    print(dp)
    print("%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%")

    return dp[n][m]


# Driver Code
if __name__ == "__main__":
    n, m = 3, 1
    print(numberofways(n, m))

# This code is contributed by Ryuga
