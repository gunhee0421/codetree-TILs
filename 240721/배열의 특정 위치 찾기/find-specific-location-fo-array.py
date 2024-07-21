arr = list(map(int, input().split()))

n = len(arr)

sumVal = 0
threeVal = []
for i in range(1, n, 2):
    sumVal += arr[i]
for i in range(2, n, 3):
    threeVal.append(arr[i])

three = sum(threeVal)/len(threeVal)


print(sumVal, round(three, 1))