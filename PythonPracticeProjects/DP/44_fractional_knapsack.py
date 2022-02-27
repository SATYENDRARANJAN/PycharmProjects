# Given weight and value of items , we need to add these items in a
# capacity of knapsack W to find the max total value in the knapsack
from builtins import staticmethod, range, len, str


class Item:
    def __init__(self,wt,val,cost,ind):
        self.wt =wt
        self.val =val
        self.cost =cost
        self.ind =ind

    def __lt__(self,other):
        return self.cost < other.cost

    def __str__(self):
        return str(self.cost)


class FractionalKnapsack:

    @staticmethod
    def init_items( wt_arr,val_arr):
        global items
        items=[]
        for i in range(len(wt_arr)):
            item = Item(wt_arr[i],val_arr[i],val_arr[i]/wt_arr[i],i)
            items.append(item)
        return items


    @staticmethod
    def find_max_value(items , Cap):
        knapsack=[]
        knapsack_value =0
        # find item with max cost
        items.sort(reverse=True)
        for i in items:
            print(i)
        for i in range(len(items)):
            print("Using item ",items[i].wt)
            if Cap>0:
                knapsack.append(items[i])
                if Cap >= items[i].wt:
                    knapsack_value += items[i].val
                    Cap = Cap - items[i].wt
                else:
                    knapsack_value += items[i].val * ( Cap/items[i].wt)
                    Cap= 0

        if Cap!=0:
            print("Items are lesser")
        else:
            for i in range(len(knapsack)):
                print(knapsack[i].wt)
            print(knapsack_value)


if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    Cap = 50
    items = FractionalKnapsack.init_items(wt,val)
    FractionalKnapsack.find_max_value(items,Cap)