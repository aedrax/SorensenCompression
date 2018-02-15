import hashlib
from itertools import combinations

data = "abc"
length = len(data)

hexdigest = hashlib.sha256(data).hexdigest()
print(hexdigest)

lookupTable = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3,
        4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2, 2, 3, 2,
        3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4,
        5, 4, 5, 5, 6, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2,
        3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3, 4, 4,
        5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5,
        6, 6, 7, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3,
        4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3, 4, 4, 5, 3,
        4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6,
        7, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4,
        5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5,
        6, 5, 6, 6, 7, 4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8]

sum1 = 0
for i in xrange(length):
    sum1 += lookupTable[bytearray(data)[i]]

print("The length is: {0}").format(length)
print("The ones count is: {0}").format(sum1)

combinations = list(combinations(range(length * 8),sum1))
numCombs = len(combinations)

count = 1
for comb in combinations:
    print("Trying {0}/{1}").format(count, numCombs)
    count += 1
    a = [0] * length
    for bit in comb:
        a[bit/8] |= 1 << (bit % 8)
    if hashlib.sha256(bytearray(a)).hexdigest() == hexdigest:
        print("Found! {0}").format(a)
        break
else:
    print("failed to find")
