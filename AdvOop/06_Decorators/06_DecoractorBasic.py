def capitalizeString(func):
    def funcWrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return funcWrapper

@capitalizeString
def concatStrings(str1, str2):
    return f"{str1}, {str2}"

print(concatStrings("Hello", "World"))

class HelloWorld:
    def __init__(self) -> None:
        self.hello = "Hello"
        self.world = "world"

    @capitalizeString
    def sayHelloWorld(self):
        return f"{self.hello}, {self.world}!"

# capitalizeString -> funcWrapper -> sayHelloWorld().upper()
print(HelloWorld().sayHelloWorld())


def nameToEmail(domain):
    def toLowerCase(func):
        def funcWrapper(*args, **kwargs):
            return func(*args, **kwargs).lower().replace(', ', '') + '@' + domain
        return funcWrapper
    return toLowerCase

class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    @nameToEmail(domain="google.com")
    def getFullName(self):
        return f"{self.firstname}, {self.lastname}"

print(Person("Riri", "Duck").getFullName())