import difflib
listOfLines = list()
char2Times = 0
char3Times = 0
for line in open("tests/Day2Input.txt", "r"):
# for line in open("test.txt", "r"):
    listOfLines.append(line)

for line in listOfLines:
    uniques = list(set(line.strip()))
    tmpChar2Times = 0
    tmpChar3Times = 0
    for char in uniques:
        if line.count(char) == 2:
            tmpChar2Times += 1
        elif line.count(char) == 3:
            tmpChar3Times += 1
    if tmpChar2Times > 0:
        char2Times += 1
    if tmpChar3Times > 0:
        char3Times += 1

    for line2 in listOfLines:
        listOfDiff = list(enumerate(difflib.ndiff(line,line2)))
        tmpChars = ""
        if len(list(filter(lambda item: "+" in item[1] or "-" in item[1], listOfDiff))) == 2:
            for a,b in listOfDiff:
                if "+" not in b and "-" not in b:
                    tmpChars = tmpChars + str(b.strip())
            print (tmpChars)


print(char2Times*char3Times)