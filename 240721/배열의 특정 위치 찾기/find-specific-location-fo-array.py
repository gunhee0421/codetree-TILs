arr = list(map(int, input().split()))

n = len(arr)

sumVal = 0
for i in range(1, n, 2):
    sumVal += arr[i]

print(sumVal, sumVal/(len(arr)/2))