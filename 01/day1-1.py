with open("input.txt", "r") as f:
    a = f.read().splitlines()

f = set()
s = 0
for i in a:
    if i[0] == '+':
        s += int(i[1:])
    else:
        s -= int(i[1:])

print(s)