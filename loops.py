def check_prime(y):
    x = y // 2

    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            print('Hence, %s is NOT prime' %(y))
            break
        x -= 1
    else:
        print(y, 'is a prime')

check_prime(2)

# for i in range(-3, 2, 2):
#     print(i, 'Pythons')
