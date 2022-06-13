def argsFunction(*args):
    print(args)
    for a in args:
        print(a)

argsFunction("coucou", "tu", "vas", "bien?")

def kwargsFunction(**kwargs):
    print(kwargs)

kwargsFunction(test="coucou", tu="tu", vas="vas", bienm="bien?")

def findBy(**kwargs):
    query = f"SELECT * FROM table WHERE "
    for k,v in kwargs.items():
        query += f"{k} = {v}"
    print(query)

findBy(test="1234")