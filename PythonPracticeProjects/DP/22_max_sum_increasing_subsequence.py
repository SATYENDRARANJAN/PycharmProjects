

def msims(a ,n):
    # if n==0 :
    #     return 0
    # print("FOR N: ",n)
    if n ==0:
        # print("n=0: returned    ", a[0],[a[0]])
        return a[0],[a[0],]
    max_sum = 0
    chain_till_i=[]
    max_chain =[]
    for i in range(n):
        if a[i] < a[n]:

            res = msims(a ,i)
            sum_till_i = a[n] + res[0]
            chain_till_i = [a[n]]+res[1]

            # print(i,a[n],a[i],sum_till_i,chain_till_i)
            # print("chain:",chain_till_i)
            if sum_till_i > max_sum:
                max_sum = sum_till_i
                max_chain = chain_till_i
    # print("     n={0}: returned {1} ,{2}   ".format(n,max_sum,max_chain))

    return max_sum,max_chain



if __name__ == "__main__":
    a=[1, 101, 2, 3, 100, 4, 5]
    l = len(a)
    for i in range(l):
        print(msims(a,i-1))