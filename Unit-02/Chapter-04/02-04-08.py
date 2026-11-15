S_1 = int(input())
S_2 = int(input())
S_3 = int(input())



if (S_1 > 0) and (S_2 > 0) and (S_3 > 0):
    if (S_1 + S_2) > S_3:
        if (S_1 == S_2 == S_3):
            print('equilateral')
        elif (S_1 == S_2 != S_3) or (S_2 == S_3 != S_1) or (S_1 == S_3 != S_2):
            print ('isosceles')
        elif S_1 != S_2 != S_3:
            print ('scalene')
    else:
        print ('not a triangle')
else:
    print ('not a triangle')

       