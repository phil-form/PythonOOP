class StaticClass:
    staticVar = 55

    def __init__(self) -> None:
        pass

    @staticmethod
    def setStaticVar(value):
        StaticClass.staticVar = value

    def setStaticVarInInstance(self, value):
        StaticClass.staticVar = value

    def setLocalVar(self, value):
        self.staticVar = value


test = StaticClass()

print(test.staticVar)
print(StaticClass.staticVar)

# test.setStaticVar(35)
StaticClass.setStaticVar(35)
print(test.staticVar)
print(StaticClass.staticVar)

test.setStaticVarInInstance(75)
print(test.staticVar)
print(StaticClass.staticVar)

test.setLocalVar(163)
print(test.staticVar)
print(StaticClass.staticVar)

test.staticVar = 321
print(test.staticVar)
print(StaticClass.staticVar)