text = open("data/maerchen.txt", "r")

lineCount = 0
lineList = wordList = []
passWord = ""

for line in text:

  if len(line) > 3:
    lineCount += 1
    wordList.append(line.split(" "))

print(f"There´re: '{lineCount}' useful lines.")
print(wordList)

for row in wordList:
  for word in row:
    if "cyber" in word.lower():
      print(word)

      if "-" in word:
        passWord += "1"
      else:
        passWord += "0"

print(passWord)