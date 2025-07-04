from random import randint

numsRandom = [randint(1,10000) for i in range(10)]

a = sorted(numsRandom)
b = [k for k in numsRandom if k>30]

print(a)
print(b)