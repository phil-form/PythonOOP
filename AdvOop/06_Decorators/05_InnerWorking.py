def concatStrings(str1, str2):
    return f"{str1}, {str2}"

print(concatStrings("Hello", "World!"))
print(concatStrings("Hello", "World!").upper())

def capitalizeString(func):
    def funcWrapper(str1, str2):
        return func(str1, str2).upper()
    return funcWrapper

# j'écrase concatStrings avec la fonction capitalizeString(concatStrings)
# capitalize string appellera la fonction ligne 1 à l'intérieur.
print(concatStrings)
concatStrings = capitalizeString(concatStrings)
print(concatStrings)
print(concatStrings("Hello", "World!"))

@capitalizeString
def concatStrings2(str1, str2):
    return f"{str1}, {str2}"

print(concatStrings2)
print(concatStrings2("Hello", "World!"))