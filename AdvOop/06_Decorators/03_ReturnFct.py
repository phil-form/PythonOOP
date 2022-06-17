def listSum(arr):
    def sumInteger():
        return sum([data for data in arr if isinstance(data, int)])
    return sumInteger

arr = [2252, "TOTO", 3253.0, 225, 642, 6986]
fctVar = listSum

print(type(fctVar))
print(fctVar(arr))
internalFct = fctVar(arr)
print(internalFct())