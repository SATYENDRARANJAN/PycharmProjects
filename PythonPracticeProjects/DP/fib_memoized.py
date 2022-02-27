


def fib(n,lookup):
    if n <=1 :
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib(n-1,lookup) + fib(n-2,lookup)
    return lookup[n]



def main():
    n =9
    lookup = [None] * (n+1)
    print(fib(9,lookup))



if __name__ == "__main__":
    main()