from icecream import ic

def genSubsets(L):
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])

    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller + new

ic(genSubsets([0,1,2,3]))
ic(genSubsets([14,139,64,2,23420]))

def recurPowerNew(a, b):
   print(a, b)
   if b == 0:
      return 1
   elif b%2 == 0:
      return ic(recurPowerNew(a*a, b/2))
   else:
      return ic(a * recurPowerNew(a, b-1))

ic(recurPowerNew(3,7))
