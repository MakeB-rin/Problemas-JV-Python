def ultimoElemento(n):
    s = 0
    while n != 0:
        aux = n % 10
        n //= 10
        s += aux
    return s

n = int(input())
l1 = [0] * 10
l2 = [0] * 10
valor = list(map(int, input().split()))
c = 0
for i in range(0, n):
    v = ultimoElemento(valor[i]) % 10
    if l1[v] == 0:
        l1[v] = valor[i]
    else:
        l2[c] = valor[i]
        c = c + 1
cnt = 0
for j in range(0, 10):
    if l2[cnt] != 0:
        if l1[j] == 0:
            l1[j] = l2[cnt]
            cnt = cnt + 1
    else:
        break

for i in range(0, 10):
    print(l1[i], end=" ")
    #AutoIndexación
