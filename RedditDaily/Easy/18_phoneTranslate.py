#unfinihsed

num_dict = {"a":2, "b":2, "c":2, "d":3, "e":3, "f":3, "g":4, "h":4, "i":4, "j":5, "k":5, "l":5, "m":6, "n":6, "o":6, "p":7,"q":7, "r":7, "s":7, "t":8, "u":8, "v":8, "w":9, "x":9, "y":9, "z":9}
phone = input("String?")
translation = ""
for i in phone:
    if i in ("1","2","3","4","5","6","7","8","9","0"):
        translation += i
    elif i in num_dict:
        translation +=str(num_dict[i])
print(translation)
