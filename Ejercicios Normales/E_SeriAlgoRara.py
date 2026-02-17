num = int(input())

a, b = 0, 1
cnt = 1
sw = 3

for i in range(num):
    c = a + b
    a = c
    if cnt < sw:
        b += 1
        cnt += 1
    else:
        b -= 1

    if b == 0:
        sw += 1
        cnt = 1
        b = 1

    print(c, end=" ")

#Una Serie Algo rara
