coin_collection = 50 * ['H']

for i in range(1, len(coin_collection)):
    j = i
    while j < len(coin_collection):
        if coin_collection[j] == 'H':
            coin_collection[j] = 'T'
            j = i + j + 1
        else:
            if coin_collection[j] == 'T':
                coin_collection[j] = 'H'
                j = i + j + 1
for count, item in enumerate(coin_collection, start=1):
    print(count, item)
print("Numbers of H in coin collection are:", coin_collection.count('H'))
