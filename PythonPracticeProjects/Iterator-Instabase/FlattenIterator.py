class Iterator:
    def __init__(self, l):
        self._l = l

    def next(self):
        try:
            return self._l.pop(0)
        except:
            return None

    def hasNext(self):
        return bool(len(self._l))


# iterator = Iterator([1,2,3])
# print(iterator.hasNext()) -> True
# print(iterator.next()) -> 1
# print(iterator.hasNext()) -> True
# print(iterator.next()) -> 2
# print(iterator.hasNext()) -> True
# print(iterator.next()) -> 3
# print(iterator.hasNext()) -> False
# print(iterator.next()) -> None

class FlattenIterator:
    def __init__(self, it_list):
        self.it_list = it_list
        self.last = it_list[len(it_list) - 1]

    def next(self):
        try:
            # return ..
            # iterate iterators
            # if not last move to nxt list
            it = self.it_list[0]
            while not it.hasNext():
                if it != self.last:
                    self.it_list.pop(0)
                    it = self.it_list[0]

                else:
                    return None
            return it.next()

        except:
            return None

    def hasNext(self):
        it = self.it_list[0]
        if not it.hasNext() and it == self.last:
            return False
        return True


flatten_iterator = FlattenIterator([Iterator([1]), Iterator([]), Iterator([2, 3, 4]), Iterator([5, 6])])
print(flatten_iterator.hasNext())
print(flatten_iterator.next())
print(flatten_iterator.next())
print(flatten_iterator.hasNext())
print(flatten_iterator.hasNext())
print(flatten_iterator.next())
print(flatten_iterator.next())
print(flatten_iterator.hasNext())
print(flatten_iterator.next())
print(flatten_iterator.next())
print(flatten_iterator.next())

# flatten_iterator.next())
# flatten_iterator.next() -> 4
print(flatten_iterator.hasNext())
# flatten_iterator.next() -> 5
# flatten_iterator.next() -> 6
# flatten_iterator.hasNext() -> False