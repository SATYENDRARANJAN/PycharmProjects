from builtins import len


def findsum(a,b):

    l1 = len(a)
    l2 = len(b)
    if l1<l2:
        temp=l2
        l2=l1
        l1=temp
        temp=a
        a=b
        b=temp

        # adding 0's in beginning of shorter string
        i=l1
        j=l2
        while  j!=i:
            b="0"+b
            j+=1
        print(a)
        print(b)
        print(len(a),len(b))
        carry =0
        final_ans=''
        for i in range(len(a)-1,-1,-1):
            sum = (int(a[i])) + (int(b[i])) + carry
            d = sum%10
            carry=sum//10

            final_ans = str(d)+ final_ans
            # print("{0}+{1}={2} , carry={3}".format(int(a[i]),int(b[i]),d,carry))

        final_ans= str(carry) +final_ans if carry!=0 else final_ans
        print(final_ans)






if __name__ == "__main__":
    a = '42342423423'
    b= "34234242324424234"
    findsum(a,b)