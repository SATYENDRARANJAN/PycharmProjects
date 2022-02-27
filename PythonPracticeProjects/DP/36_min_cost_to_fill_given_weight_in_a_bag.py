# In this problem , provided
# cost of item and
# weight of packets and
# infinite supply
# Its an Unbounded Knapsack problem .
# dp[] = dp[]


#using recursion
def min_cost( n , W):
    if n == 0 or W == 0:
        return 0
    if







if __name__ == "__main__":
    global cost
    cost  = [1, 2, 3, 4, 5]
    W =5
    n = len(cost)

    print(min_cost(n,W))