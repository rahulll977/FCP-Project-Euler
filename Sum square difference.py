#6 Sum square difference.

N = 100
count_1 = 0
count_2 = 0
l1 = [i for i in range(1, N + 1)]
l2 = [i**2 for i in range(1, N + 1)]
for i in l1:
    count_1 += i
for i in l2:
    count_2 += i
print(count_1**2-count_2)