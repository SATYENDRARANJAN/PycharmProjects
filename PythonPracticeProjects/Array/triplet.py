
class Array():
    def __init__(self, arr):
        self.arr = arr

    def findTripletwithSumK(self):
        l = len(self.arr)
        for i in range(0,l):
            for j in range(i+1 , l):
                for k in range(j+1,l):
                    if i!= j and j !=k:
                        print ("nos are : {0} . {1} . {2}".format(self.arr[i],self.arr[j],self.arr[k]))


    def findTripletwithSumK_o_n_square(self,sum):
        l = len(self.arr)
        # first element of triplet is chosen .
        # the sum of next two elements must be (K - arr[i])
        a= self.arr
        print (a)
        # for i in range(0,l):
        i=0
        for j in range(0 , l-1):
            for k in range(j+1 , l):
                print("equation is  {0} + {1} = {2} - {3} i.e. {4} = {5}  :".format(a[j], a[k] , sum ,a[i], a[j]+ a[k] , sum- a[i] ))
                if a[j] + a[k] == sum - a[i] :
                        print("nos are :".format(a[i],a[j]))
            i = i+1


if __name__ == "__main__":
    a = [3,2,5,7,3,4,5,3] [2,3,3,4,4,4,5,5,6,7,7,7,7]
    arrayObj = Array(a)
    arrayObj.findTripletwithSumK_o_n_square(12)