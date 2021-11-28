with open("input.txt", "r") as f:
    a = f.read().splitlines()

for i in a:
    for j in a:
        if i == j: continue
        wrong = 0
        letter = ''
        for k in range(len(i)):
            if i[k] != j[k]: 
                wrong += 1
                letter = i[k]
            if wrong > 1: break
        if wrong == 1:
            print(i.replace(letter, ''))
            exit()