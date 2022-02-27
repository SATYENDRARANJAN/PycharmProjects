# to find the max length chain of pairs , an array of pairs is sorted according to the first element .
# We need SORTING by first element as we array of pairs where in the "second element of the first pair" needs to be smaller than the
# ... "first element of the second pair". This means if all elements are sorted by the first element , the length of the pair would be maximum .
# and then the max length of chain of pairs subsequence is found in a similar fashion to max_pair_subsequence.

class Pair:
    def __init__(self, a , b):
        self.a = a
        self.b = b

    def __lt__(self,other):
        return  self.a < other.a

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




def find_max_pair_chain_length_recursive(a,n):
    print(a,n)
    if n ==0:
        return 0
    maxx = 0
    for i in range(1,n):
        for j in range(i):
            print (i , j)
            if a[i].a > a[j].b:
                print ("hi")
                res = find_max_pair_chain_length_recursive(a,j+1)
                if res>maxx:
                    maxx =res
    return 1+maxx


def get_list_max_pair_chain_length_recursive(a,n):
    if n == 0 :
        return []
    maxx = []
    for i in range(1,n):
        for j in range(i):
            if a[i].a > a[j].b:
                res = get_list_max_pair_chain_length_recursive(a,j+1)
                if len(res) > len(maxx):
                    maxx = res
    return [a[n-1]] + maxx


if __name__== "__main__":
    a1 = [Pair(5, 29), Pair(39, 40),Pair(15, 28), Pair(27, 40), Pair(50, 90)]
    a = [10, 22, 9, 33, 21, 50, 41, 60]

    n = len(a)
    print(find_max_chain_length_recursive(a,n))

    n1 = len(a1)
    for i in (get_list_max_pair_chain_length_recursive(a1,n1)):
        print (i.a ,i.b)
        print()

    print("len is :{0} ".format(len((get_list_max_pair_chain_length_recursive(a1,n1)))))

