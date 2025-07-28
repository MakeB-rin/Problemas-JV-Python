def letra_faltante_menor(s):
    for c in range(ord('a'), ord('z') + 1):
        if chr(c) not in s:
            return chr(c)
    return -1

s = input().strip()
print(letra_faltante_menor(s))

# Menor Letra
