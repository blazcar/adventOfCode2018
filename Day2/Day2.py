import difflib
listOfLines = list()
char2Times = 0
char3Times = 0
for line in open("tests/Day2Input.txt", "r"):
# for line in open("test.txt", "r"):
    listOfLines.append(line)

for line in listOfLines:
    uniques = list(set(line.strip()))
    update2 = True
    update3 = True
    for char in uniques:
        if update2 and line.count(char) == 2:
            char2Times += 1
            update2 = False
        elif update3 and line.count(char) == 3:
            char3Times += 1
            update3 = False

    for line2 in listOfLines:
        listOfDiff = list(enumerate(difflib.ndiff(line,line2)))
        tmpChars = ""
        if len(list(filter(lambda item: "+" in item[1] or "-" in item[1], listOfDiff))) == 2:
            for a,b in listOfDiff:
                if "+" not in b and "-" not in b:
                    tmpChars = tmpChars + str(b.strip())
            print (tmpChars)


print(char2Times*char3Times)