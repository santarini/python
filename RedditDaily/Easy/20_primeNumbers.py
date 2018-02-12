#display all prime numbers below 2000
#a prime number is int greater that cannot be formed by multiplying two smaller ints

#define two ints equal to the current number undergoing the check
i=2

#creat int to be modulo holder
m =0

print(i)
i+=1
print(i)
i+=1
j = i -1
while i < 100:
    j = i -1
    
    while j > 1:
        m = i%j
        if m == 0:
            #number is composite
            #stop counting down, break loop
            j = 1
            #go to next i
            i += 1
        if j == 2:
            #you've reached the bottom without encountering a perfect divisor
            print(i)
            i += 1
        else:
            #if nothing else decrement j
            j = j -1
