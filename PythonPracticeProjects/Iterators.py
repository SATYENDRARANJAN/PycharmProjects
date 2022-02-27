

class Dummy():
    global myGlobalVariable2
    myGlobalVariable2=600

    def changeGlobalVarValue(self,gl):
        # TO CHANGE GLOBAL VARIABLE USE BELWOW 2 LINES .
        global myGlobalVariable2
        myGlobalVariable2 = gl




myGlobalVariable = 500

if __name__=="__main__":
    myTuple = ("India","China","Japan",1,2,4.4)
    it = iter(myTuple)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(len(myTuple))


    myStr ="banana"
    for  x in myTuple:
        print(x)


    myStr ="banana"
    for  x in myStr:
        print(x)


    print(myGlobalVariable2)

    obj = Dummy()
    obj.changeGlobalVarValue(800)
    print((myGlobalVariable2))