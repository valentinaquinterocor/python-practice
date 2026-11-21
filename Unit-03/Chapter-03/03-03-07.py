M = int(input())

for i in range(M, 0, -1):
    print(' ' * (M - i), end='')
    print(*(i * '1'), sep='0')

