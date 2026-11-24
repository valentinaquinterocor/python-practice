S = input()
num_spaces = 0
str_length = len(S)
space_count = 0

for char in S:
    if char == ' ':
        num_spaces += 1

for index in range(str_length):
    char_at_index = S[index]
    if char_at_index == ' ':
        space_count += 1
        
        if space_count == num_spaces:
            print(index)
        else:
            print(f'{index}, ', end="")

if num_spaces == 0:
    print('no spaces found')
    