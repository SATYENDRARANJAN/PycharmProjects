#
#
# def swap(a,start,end,limit):
#     for i in range(limit):
#         a[start+i],a[end+i]=a[end+i],a[start+i]
#
#
# def rotateLeft(a,r,n):
#     r=r%n
#     if (r==0 or  r%n==0):
#         return a
#     A=r
#     B=n-r
#     while(A!=B):
#         if A<B:
#             swap(a,r-A,r-A+B,A)
#             B=B-A
#         elif B<A:
#             swap(a,r-A,r,B)
#             A=A-B
#     print("before swap :",a)
#     swap(a,r-A,r,A)
#     return a
#
#
#
# if __name__=="__main__":
#     a =[1,2,3,4,5]
#     r =2
#     n =len(a)
#     rotateLeft(a,2,5)
#     print(a)

# RECURSIVE
def leftrotate(arr,i,n,d):
    if d==0 or n==d:
        return

    if d==n-d:
        swap(arr,i, n-d+i,d)
    if d <n-d:
        swap(arr,i,n-d+i,d)
        leftrotate(arr,i,n-d,d)
    elif d>n-d:
        swap(arr,i,n-d,d)

def blockswap(arr,d,n):
    leftrotate(arr,0,d,n)




def blockswap2(arr,n,d):
    pass









if __name__ == "main":
    arr=[1,2,3,4,5,6,7]
    blockswap(arr,2,7)
    blockswap2(arr,2,7)

















