import difflib
a = "abcde"
b = "abcdj"

list2 = list(filter(lambda item: "+" in item[1] or "-" in item[1], list(enumerate(difflib.ndiff(a,b)))))
print (list2)

# list = [("a", "+"), ("a", "a"), ("a", "-1")]
# [item for item in list if "+" in item[1] or "-" in item[1]]
# for item in list:
#     print ("+" in item[1])
#
# list2 = [item for item in list if "x" in item[1]]
#
#
# [item for item in list ]
