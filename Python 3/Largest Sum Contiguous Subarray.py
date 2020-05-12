a = [-2, -3, 4, -1, -2, 1, 5, -3]
sum = 0
sum1 = 0
for i in range(0, len(a) - 1):
    sum=0
    for j in range(i, len(a)):
        sum = sum + a[j]
        if sum > sum1:
            sum1 = sum
            temp1 = a[i]
            temp2 = a[j]
print(sum1)
print(temp1)
print(temp2)
