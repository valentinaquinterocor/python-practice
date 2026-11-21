M = int(input())

for i in range(1, M + 1):
    print(' ' * (M - i), end='')
    print(*(i * '1'), sep='0')