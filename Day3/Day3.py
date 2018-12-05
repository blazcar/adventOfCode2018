f = open("tests/Day3Input.txt")

panelx = []

area = 0
id = 0

untouched = [(0, 0) for i in range(1, 2001)]

for i in range(1, 2001):
    panely = []
    for j in range(1, 2001):
        panely.append((0, "=CLEAN=", 0))
    panelx.append(panely)

for line in f:
    array = line.split(" ")
    id += 1
    array = array[2:]
    (xOffset, yOffset) = array[0].split(",")
    (xLen, yLen) = array[1].split("x")
    xOffset = xOffset.strip()
    yOffset = yOffset.strip()[0:-1]
    # print(int(xOffset), int(xOffset) + int(xLen) - 1)
    for i in range(int(xOffset), int(xOffset) + int(xLen)):
        # print(int(yOffset), int(yOffset) + int(yLen) - 1)
        panely = panelx[i]
        for j in range(int(yOffset), int(yOffset) + int(yLen)):
            tup = panely[j]

            if tup[0] == 1:
                area += 1
            if tup[0] >= 1:
                untup = (tup[0] + 1, tup[2])
                untouched[tup[2] - 1] = untup
                tup = (tup[0] + 1, "COVERED", id)
                untouched[id - 1] = (tup[0], id)
                panely[j] = tup
                continue

            tup = (tup[0] + 1, tup[1], id)
            if untouched[tup[2] - 1][0] == 0:
                untouched[tup[2] - 1] = (9, id)
            panely[j] = tup
        panelx[i] = panely
# for i in range(0, len(panelx)):
#     s = ""
#     panely = panelx[i]
#     for j in range(0, len(panely)):
#         s = s + str(panely[j]) + "|"
#     print(s)
print("Area=", area)
print("Not covered=", list(filter(lambda x: x[0] == 9, untouched))[0][1])