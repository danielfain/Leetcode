def productNotI(arr):
    ans = []
    prod = 1
    for i in range(len(arr)):
        prod *= arr[i]
    for i in range(len(arr)):
        ans.append(prod // arr[i])
    return ans


arr = [1, 2, 3, 4, 5]
print(productNotI(arr))