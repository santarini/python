#display all prime numbers below 2000
#a prime number is int greater that cannot be formed by multiplying two smaller ints

#define two ints equal to the current number undergoing the check
i=2

#create int to be modulo holder
m =0

print(i)
i+=1
print(i)
i+=1
j = i -1
while i < 2000:
    j = i -1
    while j > 1:
        m = i%j
        if m == 0:
            #stop counting down
            j = 1
            #go to next i
            i += 1
        if j == 2:
            print(i)
            i += 1
        else:
            #if nothing else decrement j
            j = j -1
