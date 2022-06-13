from typing import Iterator

class ExampleIterator:
    def __init__(self) -> None:
        self.datas = []
        self.length = 0

    def __len__(self) -> int:
        # return self.length
        return len(self.datas)

    def __iter__(self) -> Iterator:
        # return self.datas.__iter__()
        self.current = 0
        return self

    def __next__(self):
        itr = self.current

        if itr >= self.length:
            raise StopIteration

        self.current = itr + 1

        return self.datas[itr]

    # if value in Object
    def __contains__(self, value):
        return True if value in self.datas else False

    def __getitem__(self, key):
        return self.datas[key]

    def __setitem__(self, key, value):
        self.datas[key] = value

    def append(self, value):
        self.datas.append(value)
        self.length += 1
        
testList = ExampleIterator()

testList.append(55)
testList.append(54)
testList.append(53)

for i in testList:
    print(i)

testList[0] = 60

for i in testList:
    print(i)

testList[55] = 75
