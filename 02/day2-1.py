with open("input.txt", "r") as f:
    a = f.read().splitlines()

c1, c2 = 0, 0
for i in a:
    two = False
    three = False
    l = [0] * 26
    for j in i:
        l[ord(j) - 97] += 1
    if 2 in l:
        c1 += 1
    if 3 in l:
        c2 += 1
print (c1 * c2)