import operator
import sys

file = open(sys.argv[1], "r")

text = file.read()
file.close()

splitText = text.split()
print("")
print("splitText = {}".format(splitText))
print("")

words = {}

"""Count the words: """
for i in splitText:
    if i.lower() in words:
        words[i.lower()] += 1
    else:
        words[i.lower()] = 1

sortedWords = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
print(sortedWords)

file = open(sys.argv[1][:-4] + "-count" + sys.argv[1][-4:], "w")

file.write("Total words - {}\nUnique Words - {}\n\n".format(len(splitText), len(sortedWords)))

for i in sortedWords:
    file.write("{} - {}\n".format(i[0],i[1]))

file.close()

print("All counted!")
