# 61	Check whether an array contains a
#       pair with target sum
arr = [2, 4, 1, 2, 3, 2, 4, 5, 4, 2, 7]
target = 12 #5,7

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])