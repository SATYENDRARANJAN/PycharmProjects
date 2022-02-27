import json

if __name__ == "__main__":
    x ='{"name":"John", "age":"30" ,"city" : "New York"}'  #JSON
    y = json.loads(x)
    # y is a python dict
    print(y['name']) # prints John


    print(json.dumps(y))# prints json back .


    myTuples =(2,3,4,"sf")
    print (json.dumps(myTuples)) # output --> [2, 3, 4, "sf"]

    print(json.dumps(["apple", "bananas"]))# output is list
    print(json.dumps("hello"))# output is "hello"

    print(json.dumps(42))# output is 42
    print(json.dumps(31.76))# output is 31.76
    print(json.dumps(False)) # output is false
    print(json.dumps(None)) # output is null

