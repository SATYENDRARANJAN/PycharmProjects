from builtins import input, list, range, map, int
from collections import defaultdict


class AssignCap():
    def __init__(self):
        self.allmask =0
        self.total_caps =3
        self.caps = defaultdict(list)

    def countways(self,N):
        for person in range(int(N)):
            caps_possessed_by_a_person =map(int, input().strip().split())
            print(caps_possessed_by_a_person)

            for i in caps_possessed_by_a_person:
                print("i=" ,i)
                print("self.caps[{0}]={1}".format(i,self.caps[i]))
                self.caps[i].append(person)
                print(self.caps[i])
                print("")

        # allmask is used to check if all persons are included or not .
        self.allmask = (1<<int(N)) -1
        print(self.allmask)

        # Initialise all entries in dp as -1
        dp = [[-1 for j in range(self.total_caps + 1)] for i in range(2 ** int(N))]
        print (dp)
        # Call recursive function countWaysUtil
        # result will be in dp[0][1]
        print (self.countWaysUtil(dp, 0, 1, ))



def countWaysUtil(self,dp, mask, cap_no):
    if mask == self.allmask:
        return 1

    if cap_no > self.total_caps:
        return 0





def main():
    no_of_people = input()
    AssignCap().countways(no_of_people)

if __name__ == "__main__":
    main()