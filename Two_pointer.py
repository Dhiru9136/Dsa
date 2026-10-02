# 61	Check whether an array contains a
#       pair with target sum
arr = [2, 4, 1, 2, 3, 2, 4, 5, 4, 2, 7]
target = 12 #5,7

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])

# 62 Reverse an array using two pointers
arr = [1, 2, 3, 4, 5]
left =0
right = len(arr)-1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)


# 64	Remove duplicates from a sorted array
arr = [1, 1, 2, 2, 3, 3, 4, 5, 5]
arr1 = []
for i in arr:
    if i not in arr1:
        arr1.append(i)
print(arr1)




# 69	Find intersection of two sorted arrays

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5]
arr2 = [1, 2, 3, 4, 5, 6, 7]
a1=sorted(arr)
a2=sorted(arr2)
intersection = []
for i in a1:
    if i in a2 and i not in intersection:
        intersection.append(i)
print(intersection)
