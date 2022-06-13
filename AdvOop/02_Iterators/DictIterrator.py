from typing import Iterator

class ExampleIterator:
    def __init__(self) -> None:
        self.datas = {}

    def __iter__(self) -> Iterator:
        # return self.datas.__iter__()
        self.current = 0
        self.currentKeys = tuple(self.datas.keys())
        return self

    def __len__(self):
        return len(tuple(self.datas.keys()))

    def __next__(self):
        itr = self.current

        if itr >= len(self.currentKeys):
            raise StopIteration

        self.current = itr + 1

        return self.datas[self.currentKeys[itr]]

    # if value in Object
    def __contains__(self, value):
        return True if value in self.datas.keys() else False

    def __getitem__(self, key):
        return self.datas[key]

    def __setitem__(self, key, value):
        self.datas[key] = value
        
testList = ExampleIterator()

testList[55] = 55
testList[54] = 54
testList[53] = 53

for i in testList:
    print(i)

testList[0] = 60

for i in testList:
    print(i)

testList[55] = 75

for i in testList:
    print(i)