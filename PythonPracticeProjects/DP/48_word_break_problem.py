# For a word break problem , ilikethiscity
# Given words:"i,like,love,ok,street,city,this,liket"
# We need to find whether these words are enough to form this sentence or not
#
"""
we start from first letter of the word.
i - it might be or might not be in the sen
i -
il
ili
ilik
ilike
....
ilikethiscity

if ith position is counted ==

sentence ="i" "like"
if ith is a word -- find_words(i+1,i+1) --  not a word (counted)   ---  find_words(i+1,i+2) .... (i+1,n)
                                        --  a word (not counted)   ---  find_words(i+2,i+2) .... (i+1,n)
                    find_words(i+1,i+2)
                    find_words(i+1,i+3)
                    find_words(i+1,i+4) "like" -  find_words(i+5,i+5)
                                               -  find_words(i+5,i+6)
                                               -  find_words(i+5,i+7)
                                               -  find_words(i+5,i+8) ="this" --  find_words(i+1,i+2) .... (i+1,n)
                    find_words(i+1,i+5)
                    find_words(i+1,i+6)
                    .... (i+1,n)
if ith isnt a word -- find_words(i,i+1) .... (i,n)



0,0   -- 0,1
         0,2
         0,3
         0,4
         0,5
         ...
         0,n

0,1   --


0,2


0,3


 ....



0,n


"""
from builtins import range, len



def wordbreak(st,end,list):
    print(st,end,sentence[st:end+1])
    # base case
    if st>=end:
        return True

    for i in range(st,end+1):
        print(st,i+1)
        w= sentence[st:i+1]
        if w in words:
            if wordbreak(i+1,end,list): # recursively finds till end
                list.append(w)
                # return True
    if list is not None:
        return True
    return False


def word_break_print(s, d, ans):
    '''recursive approach'''
    if s == '':
        return []
    list2=[]

    for i in range(1, len(s) + 1):
        pre = s[:i]
        if pre in d:
            c_ans_list = word_break_print(s[i:], d, ans)
            if len(c_ans_list)!=0 :
                for c_ans in c_ans_list:
                    ans = f"{pre} {c_ans}"
                    # print (ans)
                    if len(ans.replace(" ", "")) == len(sentence):
                        list.append(ans)
                    list2.append(ans)
            else:
                ans = f"{pre}"
                # print (ans)
                list2.append(ans)
                        
                # print ("lit",list2)
    return list2


def word_break_print1(s, d, ans):
    '''recursive approach'''

    for i in range(1, len(s) + 1):
        pre = s[:i]
        if pre in d:
            if not s[i:]:
                # base case
                return ans.append(pre)

            c_ans = word_break_print(s[i:], d, ans)
            if c_ans:
                ans.extend([f"{pre} {x}" for x in c_ans])

    return ans



def word_break_dp(s,d,ans):
    dp = [False for i in range(len(s)+1)]

    for i in range(1,len(s)+1):
        if i>len(s):
            break;

        w = s[0:i]
        if dp[i]==False and w in words:
            dp[i]=True

        if dp[i]==True:
        # Traverse the suffix
            if i==len(s):
                return True

            for j in range(i+1,len(s)+1):
                w = s[i:j]
                if dp[j] ==False and w in words  :
                    dp[j]=True

                if j==len(s) and dp[j]==True:
                    return True
    return False

list2=[]
list =[]
# words=["mobile","samsung","sam","sung","man","mango","icecream","and","go","i","like","ice","cream"]
# sentence = "ilikesungsamsammobilei"

sentence = 'indiaisagreatcountryi'
words =['india',"i",'japan','is','was','a','great','country',"count","ry" ,'state','city']

if __name__ == "__main__":
    ans=[]
    # print(wordbreak(0,len(sentence),list))
    # print(word_break_print(sentence,words,ans))
    # print(word_break_print1(sentence,words,ans))
    # print(list)
    print(word_break_dp(sentence,words,ans))