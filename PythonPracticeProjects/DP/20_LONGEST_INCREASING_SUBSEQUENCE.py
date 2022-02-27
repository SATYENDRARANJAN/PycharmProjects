# this program is about longest increasing subsequence
# where f(i)>f(i) where i>j
# For an array of 5 , to find length of LS
# f(5) = 1 + max(f4,f3,f2)
#
# base case : if i==0 : return 0
#                i==1 : return 1
#                i==2 : if a1 < a2 ? 1+a[1] : 1
#                i==3 : if a


# for the  LIS  ,

def find_lcs(a,n):
    if n<0: return 0
    if n == 0 : return 1
    mxm = 0
    ind =0
    for i in range(n-1,-1,-1):
        if a[n] >a[i]:
            if mxm < find_lcs(a, i):
                mxm = find_lcs(a,i)
                ind = i # PREvious max length code.
    if a[n] > a[ind]:
        return 1+mxm
    return 1



#RIGHT CODE 1
def find_lcs_tab(a,n):
    dp =[0]*(n+1) # n is max subscript here
    dp[0] = 1

    for i in range(1,n+1):
        mxm=0
        for j in range(i-1,-1,-1):
            if a[i]>a[j]:
                mxm = max(mxm,dp[j])
        dp[i] =1+ mxm
    return(dp)




#RIGHT CODE 2
def find_lcs_tab_rt(a, n):
    dp =[1] *(n+1)
    dp[0] =1
    for i in range(1, n+1):
        for j in  range(i-1,-1,-1):
            if a[i] >a[j]  and dp[i]<dp[j]+1:
                dp[i] = dp[j]+1
    print(dp)



# THIS ONE IS WHERE WE GO FROM 0 TO N rather than N-1 TO 0.
def find_max_chain_length_recursive(a,n):
    if n ==0 :
        return 0

    maxx =0

    for i in range(1,n):
        for j in range(i):
            if a[j]<a[i] :
                _res = find_max_chain_length_recursive(a , j+1)
                if _res > maxx:
                    maxx =_res
    return  1+ maxx





if __name__ == "__main__":
    n = 8
    a = [70, 36, 9, 33, 21, 50, 41, 60]
    print("ans:",find_lcs(a,n-1))
    print("by dp tabulation 1 : ", find_lcs_tab(a,n-1))
    print("by dp tabulation 2 : ", find_lcs_tab_rt(a,n-1))


