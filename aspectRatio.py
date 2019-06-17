from fractions import Fraction

width = 1920
height = 1080


print("Your aspect ratio:\n" + str(Fraction(width/height)).replace("/",":"))

print("\nExamples of your aspect ratio:")
for i in range(0, 3 * width , 100)[1:]:
    print(str(i) + " x " + str(int(i/(width/height))))
