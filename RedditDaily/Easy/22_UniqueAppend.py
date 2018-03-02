a = ["a","b","c",1,4,]
b = ["a", "x", 34, "4"]
c = a
def AppendUnique(a, b):
    for x in b:
        if x not in a:
            c.append(x)
    print(c)

AppendUnique(a,b)
