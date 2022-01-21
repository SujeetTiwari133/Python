with open("word.txt") as f:
    content = f.read()
    # print(content)

words = []
# number_replace = int(input("Enter the number of words you want to replace "))

for i in range(1):
    replaceword = input("Enter the word to be replaced ")
    wordreplace = input("Enter the replacing Word ")
    words.append(replaceword)
for word in words:
    content = content.replace(word, wordreplace)
# print(words)
with open("word.txt", 'w') as f:
    f.write(content)
