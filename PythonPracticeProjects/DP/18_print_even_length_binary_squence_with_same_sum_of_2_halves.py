# to print even sequences with diff of left and right halves as 1


def print_seq_util(a, n , diff , first , last):
    # if last<0 or first>n:
    #     return
    if abs(diff)> (last-first+1)//2:
        return

    if first>=last and diff ==0:
        print (a)
        return

    print(first,last)

    a[first] = '0';
    a[last] = '0';
    print_seq_util(a,n-1 , diff ,first+1,last-1 )
    a[first] = '1';
    a[last] = '1';
    print_seq_util(a,n-1 , diff ,first+1,last-1 )

    a[first] = '0';
    a[last] = '1';
    print_seq_util(a,n-1 , diff+1 ,first+1,last-1 )

    a[first] = '1';
    a[last] = '0';
    print_seq_util(a,n-1 , diff-1 ,first+1,last-1 )



def print_seq(n):
    arr = ['']*2*n
    first = 0
    last = (2 * n)-1
    print(print_seq_util(arr, n, 0, first, last))



if __name__ == "__main__":
    n=2
    print(print_seq(n))