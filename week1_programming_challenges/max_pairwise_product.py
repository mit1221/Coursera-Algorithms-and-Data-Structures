# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

max1_index = -1
for i in range(0, n):
    if (max1_index == -1) or (a[i] > a[max1_index]):
        max1_index = i

max2_index = -1
for i in range(0, n):
    if (i != max1_index) and ((max2_index == -1) or (a[i] > a[max2_index])):
        max2_index = i

result = a[max1_index] * a[max2_index]

print(result)
