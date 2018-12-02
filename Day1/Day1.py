def processLine(recursively):
    global diff
    global inputValues
    global reachedTwice
    reachedTwice = False
    if reachedTwice:
        return
    for value in inputValues:
        diff = diff + value
        if diff in reachedValues:
            print("First reached twice was ", diff)
            reachedTwice = True
            break
        else:
            reachedValues[diff] = diff
    if recursively is False:
        print("Overall reached value is ", diff)
    if recursively and reachedTwice is False:
        processLine(True)
    return


f = open("tests/Day1Input.txt", 'r')
diff = 0
reachedValues = dict()
inputValues = list()
ix = 0
reachedTwice = False

for line in f:
    inputValues.append(int(line))
    ix += 1
processLine(False)
processLine(True)
