

def count_set_of_bits(n):
    count=0
    while n:
        count+=1
        n &=(n-1)
    return count



def count_flips(a,b):
    flips =0
    while(a>0 and b>0):
        t1=a&1
        t2=b&1
        if t1!=t2:
            flips+=1
        a>>1
        b>>1
    return flips



if __name__ =="__main__":
    a=10
    b=20
    count_set_of_bits(a^b)