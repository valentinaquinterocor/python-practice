L = int(input())

if L % 4 == 0:
    if L % 100 == 0:
        if L % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")
                  
        
    