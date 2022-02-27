
def summation(num):

    num = num
    sum=5
    def totsum():
        print(sum)
        for i in range(1,num+1):
            add(i)

    def add(i):
        sum=0
        sum+=i
        print(sum)


    l=totsum()
    return l



print(summation(3))