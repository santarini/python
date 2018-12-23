#max(x,y) = (x+y+|x-y|)/2
#max(x,y,z) = max(x,max(y,z))

def AlgebraicallyFindMaxTwo(x,y):
    return(x+y+abs(x-y))/2

AlgebraicallyFindMaxTwo(3,4)

def AlgebraicallyFindMaxThree(x,y,z):
    print (AlgebraicallyFindMaxTwo(AlgebraicallyFindMaxTwo(x,y), z))

AlgebraicallyFindMaxThree(3,4,5)
