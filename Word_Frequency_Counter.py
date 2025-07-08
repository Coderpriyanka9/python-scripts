sentence = "The pen is on The table inside The pen box"
words = sentence.split()
wordCount = {}
for word in words:
    if word in wordCount:
        wordCount[word] = wordCount[word] + 1
    else:
        wordCount[word] = 1
print(wordCount)