import random
number=random.randint(1,100)
while True:
    print('number from 1 to 100')
    first_try=input()
    i=int(first_try)
    if i==number:
        print('right number')
        break
    elif i<number:
        print('take higher')
    elif i>number:
        print('take low')