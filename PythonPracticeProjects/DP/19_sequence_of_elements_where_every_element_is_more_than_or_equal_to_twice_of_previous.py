
# Python3 program to count total number of
# special sequences of length n where
# Recursive function to find the number of
# special sequences

# Program to find total no. of special sequences of length n .
def add_next(a,i):
    if i==n-1 :
        print("a:", a)
        return
    # print(i, 2*a[i])
    if 2*a[i]>m:
        return
    else:
        k=0
        while( 2*a[i]+k <= m):
            # print("2*a[i]+k: " ,2*a[i]+k)
            a[i+1] = 2*a[i]+k
            k+=1
            add_next(a, i+1)

        return


def get_total_no_of_special_sequences(m,n):
    # There can be two possibilities :
    # (1) Reduce last element value
    # (2) Consider last element as m and reduce number of terms
    if m < n: # if total sum is less than no. of elements
        return 0
    if n==0:
        return 1
    res = get_total_no_of_special_sequences(m-1,n) + get_total_no_of_special_sequences(m//2,n-1)
    return res




if __name__ == "__main__":
    global n,m,a
    n = 4
    m = 10
    a = [0] * n
    print (m//2)
    # Recursive normal to print
    for i in range(1,m//2+1):
        print("i:",i)
        a[0] =i
        count =0
        add_next(a,count)

    # Recursive to derive dynamic
    print(get_total_no_of_special_sequences(m,n))