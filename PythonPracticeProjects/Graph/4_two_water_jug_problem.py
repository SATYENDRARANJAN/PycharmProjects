# Given 2 water jugs of m and n , need to calculate the min  turns in which we can find the d litres of water .
# starting form 0,0
# At each step we see whether the next vertices is present in the dict or not .
# Mark the vertex (x,Y) as visited .
# add it to queue and move to next .
# By default bfs finds the min shortest path in an array

# ALGO
# Visit a node and mark it visited
# check if m or n = d
# IF TRUE

def is_visited(visited,x,y):
    for node in visited:
        if node.x == x and node.y == y:
            return True
    return False

class St:
    def __init__(self,x, y):
        self.x = x
        self.y = y

class BFS:
    def __init__(self, m , n):
        self.m = m
        self.n = n
        visited = False

    def findTurns1(self,d):
        m = self.m
        n =self.n
        visited =[]
        # check if jug is of d size
        if m ==d or n ==d:
            return True

        q =[]
        path =[]
        q.append(St(0,0))
        path.append({0,0})
        while len(q)!=0 :
            k = q.pop(0)
            print("Runing for ",k.x,k.y)
            # if visited[{k.x,k.y}] is not None:
            #     continue
            # visited.append({k.x,k.y})
            flag = False
            a=b=0
            for node in visited:
                if node.x==k.x and node.y==k.y:
                    a=k.x
                    b=k.y
                    flag = True
            if flag:
                print("Returning for ", a, b)
                continue

            # Add to visited and path
            visited.append(St(k.x,k.y))
            path.append((k.x,k.y))
            print(path)
            # If target reached
            if k.x==d and not k.y<0:
                # path.append({k.x,0})
                print("got1  it ")
                return path

            if k.y==d and not k.x<0:
                # path.append({0,k.y})
                print("got 2  it ")
                return path

            # Fill the empty one
            if k.x == 0:
                print("Fill and Appending x: " ,m,0)
                if not is_visited(visited,m,k.y):
                    q.append(St(m,k.y))
            if k.y ==0:
                print("Fill and Appending y:" ,k.x,n)
                if not is_visited(visited,k.x,n):
                    q.append(St(k.x,n))

            # Empty the filled one
            if k.x == m:
                print("Empty and append" ,0,k.y)
                if not is_visited(visited,0,k.y):
                    q.append(St(0,k.y))

            if k.y ==n:
                print("Empty and append" ,k.x,0)
                if not is_visited(visited,k.x,0):
                    q.append(St(k.x,0))

            # If one of the jugs is not empty or not  full
            # One of the jugs will always be either empty or full
            if (k.x<m and k.y==n) or (k.y<n and k.x==m):
                if k.x<m :
                    diffx = m-k.x
                    if (k.x + diffx <= m and k.y - diffx >= 0):
                        if not is_visited(visited,k.x+diffx,k.y-diffx):
                            print("Pouring {0} to {1} from {2}".format(diffx, k.x, k.y))
                            q.append(St(k.x+diffx,k.y-diffx))
                if k.y<n :
                    diffy = n-k.y
                    if (k.x-diffy>=0 and k.y+diffy <=n) :
                        if not is_visited(visited,k.x-diffy,k.y+diffy):
                            print("Pouring {0} from {1} to {2}".format(diffy, k.x, k.y))
                            q.append(St(k.x-diffy,k.y+diffy))

            # print ([{i.x,i.y} for i in q])


    def findTurns(self, d):
        m = self.m
        n = self.n
        visited = []
        # check if jug is of d size
        if m == d or n == d:
            return True

        q = []
        path = []
        q.append(St(0, 0))
        path.append({0, 0})
        while len(q) != 0:

            print("")
            print("queue is ==>", end=" ")
            for item in q:
                print("(" + str(item.x) + "," + str(item.y) + ")", end=" ")


            k = q.pop(0)
            print("Running for ", k.x, k.y)

            flag = False
            a = b = 0
            for node in visited:
                if node.x == k.x and node.y == k.y:
                    a = k.x
                    b = k.y
                    flag = True
            if flag:
                print("Returning for ", a, b)
                continue

            # Add to visited and path
            visited.append(St(k.x, k.y))
            path.append((k.x, k.y))
            print(path)
            # If target reached
            if k.x == d and not k.y < 0:
                # path.append({k.x,0})
                print("got 1  it ")
                return path

            if k.y == d and not k.x < 0:
                # path.append({0,k.y})
                print("got 2  it ")
                return path

            # Fill the empty one
            if k.x == 0:
                print("     Fill and Appending x: ", m, 0)
                # if not is_visited(visited, m, k.y):
                q.append(St(m, k.y))

            if k.y == 0:
                print("     Fill and Appending y:", k.x, n)
                # if not is_visited(visited,k.x,n):
                q.append(St(k.x, n))

            # Empty the filled one
            if k.x == m:
                print("     Empty and append", 0, k.y)
                # if not is_visited(visited, 0, k.y):
                q.append(St(0, k.y))

            if k.y == n:
                print("     Empty and append", k.x, 0)
                # if not is_visited(visited, k.x, 0):
                q.append(St(k.x, 0))

            # If one of the jugs is not empty or not  full
            # One of the jugs will always be either empty or full
            # Find the min size of both the jugs
            # if y is filled and x is not filled -> pour empty(x) to x from y
            # if x is filled and y is not filled -> pour empty(y) to y from x
            if (k.x < m and k.y == n) or (k.y < n and k.x == m):
                print("** -> " ,k.x,k.y)
                if k.x < m:
                    # find the min here as it might happen that the bigger tank may be empty and diff will be 4 i.e. size of bigger tank, but 4 removed from smaller tank
                    diffx = min(m-k.x,k.y)
                    print("diff : ",diffx)
                    if (k.x + diffx <= m and k.y - diffx >= 0):
                        # if not is_visited(visited, k.x + diffx, k.y - diffx):
                        print("     Pouring {0} to {1} from {2}".format(diffx, k.x, k.y))
                        q.append(St(k.x + diffx, k.y - diffx))
                if k.y < n:
                    # find the min here as it might happen that the bigger tank may be empty and diff will be 4 i.e. size of bigger tank, but 4 removed from smaller tank
                    diffy = min(n-k.y,k.x)
                    if (k.x - diffy >= 0 and k.y + diffy <= n):
                        # if not is_visited(visited, k.x - diffy, k.y + diffy):
                        print("     Pouring {0} from {1} to {2}".format(diffy, k.x, k.y))
                        q.append(St(k.x - diffy, k.y + diffy))

            # print ([{i.x,i.y} for i in q])





if __name__ == "__main__":
    jugs = BFS(4,3 )
    path= jugs.findTurns(2)
    print(path)


