# use even length binary sequences with same sum of first and second half .
# for a binary sequence --- generate .. get sum of first half and second half  => compare .
# recursive way  : find the sum1 and sum2 till nth count from beginnning and the last
# stop when n == n

# to generate -->if nth bit is same  as (l-n-1)th, diff =0
# base case => if  n >= l-n-1 : return 0
# if a[n] == a[l-n-1] =>
# if a[n] - a[l-n-1] == 1 ==> diff +=1
# if a[n] - a[l-n-1] == -1 ==>  diff-=1

# Also ,for n =1:  if the num is 00 or 11 => then there are 2 choices :
# for different ones like 01 or 10 - the difference is not 0 and has to adjusted internally .
# when similar -> 2 * countseq(n-1, diff)
# when different :  when 0...1 -> 1* countseq(n-1,diff+1)
# when similar : when 1...0  -> 1 * countseq(n-1,diff-1)


def countseq_util(n, diff):

    if n == 1 and diff ==0 :
        return 2
    elif n ==1 and abs(diff) ==1:
        return 1

    count_same = 2 * countseq_util(n - 1, diff)
    # if first and last are different 01 10
    # 01
    count_01 = countseq_util(n-1, diff-1)
    # 10
    count_10 = countseq_util(n-1, diff+1)
    return count_same + count_01 + count_10



def countseq(n) :
    diff =0
    first = 0
    last = n-1
    # if first and last are same 00 or 11 2 cases
    return countseq_util(n,0)



if __name__ == "__main__":
    n =2
    print(countseq(n))