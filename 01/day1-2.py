with open("input.txt", "r") as f:
    a = f.read().splitlines()

f = set()
s = 0
while True:
    for i in a:
        if s in f:
            print(s)
            exit()
        f.add(s)
        if i[0] == '+':
            s += int(i[1:])
        else:
            s -= int(i[1:])

print(s)