imput = input("Enter Word: ")
im = [*imput]
wordback = []
word = ""
for c in range(1,len(im)+1):
    wordback.append(im[len(im)-c])
for v in range(1,len(wordback)+1):
    word += wordback[v-1]
print(f"Backwards Word: {word}")
