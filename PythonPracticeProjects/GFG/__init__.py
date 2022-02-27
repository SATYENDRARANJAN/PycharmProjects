#Recursion
#Hashing
#Practice Questions

"""
sum of nos from 1 to n = n+ f(n-1)   ----  n== 5 to 1
                    = i + f(i+1,n)   ----   n= 1 to 5


find no. of digits in a no. : = 1+ f(n/10) if n !=0 else 0
no of digits in a no. N is = logn base 10
Thus TC = O(logn base 10)



count char 'a' in a given string .

check(s,n)
if n==0 : return 0
if s[n-1] =='a': return 1+ check(s,n-1)
return check (s,n-1)



Print all the binary strings of length n :
n =2
00
01
11
10


printall(str ,n)
 if len(str)==n:
    print(str)
    return

printall(str+'0',n)
printall(str+'1',n)




Stair case problem :
In how many ways we can reach to the nth step ?
Steps allowed 1 or 2

Solution : wither start from 0 and reach 4
or start from 4 and reach 0


reached_0(n):

if n ==0: return 1
if n <0: return 0


if n ==1 : return 1
if n ==2 : return 2
else:
return reached(n-1)+ reached(n-2)


reach_4(





"""