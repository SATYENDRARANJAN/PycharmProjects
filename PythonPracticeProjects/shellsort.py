# its a variation of insertion sort
# start with a big gap . gap = length/2
# reduce the gap by n/2 each time
# starting with gap , compare all elements to the right of the gap with (ele_index - gap)th element .
# and swap them if condition is true
# Just like insertion sort but everytime starting from gap/2 and reducing it by a factor of 2

class ShellSort():
    def __init__(self , arr1, arr2 = None):
        self.arr1 = arr1
        self.arr2 = arr2

    def sort(self):
        n = len(self.arr1)
        gap = n//2
        print (gap)
        a = self.arr1
        while( gap>0 ):
            for i in range(gap, n):
                while i > 0 and a[i] > a[i-gap]:
                    print("{0}.. {1}".format(i,i-gap))
                    a[i],a[i-gap] = a[i-gap],a[i]
                    i = i-gap

            gap = gap//2
            print("gap changed to {0}".format(gap))

        print (a)




    def print(self):
        print (self.arr1)
        print (self.arr2)







if __name__ == "__main__":
    arr1 = [5,3,41,5,  9]
    ss = ShellSort(arr1)
    ss.sort()
    ss.print()