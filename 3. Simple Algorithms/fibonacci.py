def rabbit_pairs(n):
    if n == 0 or n == 1:
        return 1
    else:
        return rabbit_pairs(n-1) + rabbit_pairs(n-2)

months = int(input("Find no. of rabbits after how many months? -- "))
rbpairs = rabbit_pairs(months)
print('Number of rabbits after', str(months), 'months:', str(rbpairs))