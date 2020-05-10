a = [2, 2, 1, 2, 2, 1, 2, 1, 5]
k = 0
for i in range(0, len(a)):
    count = 0
    for j in range(0, len(a)):
        if a[i] == a[j]:
            count += 1

    if count > k:
        k = count
        l = a[i]
print("The count is:",k)
print("The element is:",l)

