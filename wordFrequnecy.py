import sys

fileSource = open("test.txt")
data = fileSource.read()
sourceWords = data.split()
fileSource.close()

wordFrequnecy = {}

unwantedChars = ".,-_\""

for rawWord in sourceWords:
    cleanWord = rawWord.strip(unwantedChars)
    if cleanWord not in wordFrequnecy:
        wordFrequnecy[cleanWord] = 0 
    wordFrequnecy[cleanWord] += 1

items = [(v, k) for k, v in wordFrequnecy.items()]
items.sort()
items.reverse()
items = [(k, v) for v, k in items]
print(items)
