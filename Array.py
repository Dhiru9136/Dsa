# 31	Find the largest element in an array
nums = [10, 25, 7, 40, 15]
largest=0
for i in nums:
    if i>largest:
        largest=i
print(largest)

# method 2
nums = [10, 25, 7, 40, 15]
nums.sort()
index=-1
print(nums[index])



# 32	Find the smallest element in an arrays
nums = [10, 25, 7, 40, 15]
nums.sort()
index=0
print(nums[index])

# 33	Find the sum of all elements
nums = [10, 25, 7, 40, 15]
sum = 0
for i in nums:
    sum = i + sum
print(sum)

# 34	Find the average of array elements
nums = [10, 25, 7, 40, 15]
sum=0
for i in nums:
    sum = i+sum

avg = sum/len(nums)
print(avg)


# 35	Count even and odd numbers
nums = [10, 25, 7, 40, 15] 
even=0
odd=0
for i in nums:
    if i%2==0:
        # print(f"This is even number = {i}")
        even+=1
    else:
        # print(f"This is odd number = {i}")
        odd+=1
print(f"Total Even Number is = {even}\nTotal Odd Number is = {odd}")


# 36	Reverse an array

nums = [10, 25, 7, 40, 15]
nums.reverse()
print(nums)

# method 02
nums = [10, 25, 7, 40, 15]
rev=[]
for i in nums:
    rev.insert(0,i)

print(rev)



# 37	Find the second largest element
nums = [10, 25, 7, 40, 15]
nums.sort()
index= -2
print(nums[index])


# 38	Find the second smallest element
nums = [10, 25, 7, 40, 15]
nums.sort()
index= 1
print(nums[index])

# 39	Remove duplicates from an array
nums = [10, 25, 7, 40, 15, 10, 15]
dup = set(nums)
dupli=list(dup)
print(dupli)

# 40	Find the frequency of each element
nums = [10, 25, 7, 40, 15, 10, 15]

freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] =1
print(freq)


# 41	Check whether an array is sorted
nums = [10, 20, 30, 40,5]
sr= sorted(nums)
if nums == sr :
    print(f"Array is sorted = {nums}")
else:
    print( f"not sorted = {nums}")

# 42	Find the missing number from 1 to N

nums = [2,3,4,5]
N = 5
exp_sum = 0
act_sum = 0
for i in nums:
    act_sum += i
for j in range(N+1):
    exp_sum+=j

missing = exp_sum-act_sum 
print(missing)



# 43	Find the duplicate number

nums = [10, 25, 7, 40, 15, 10, 15]
sr =set([])
for i in nums:
    if i not in sr:
        sr.add(i)
    else:
        print(f"duplicate= {i}")




# 44	Move all zeroes to the end

nums = [0, 1, 0, 3, 12]
count = 0
for i in nums:
    if i == 0:
        count +=1
        nums.remove(i)
nums.extend([0]*count)

print(nums)


# 45	Move all negative numbers to one side

nums = [1, -2, 3, -4, 5, -6]

negative = []
postive = []
for i in nums:
    if i >= 0:
        postive.append(i)
    else:
        negative.append(i)
postive.extend(negative)
print(f"{postive}")


# 46	Find the intersection of two arrays

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6]

result = []

for i in arr1:
    if i in arr2:
        result.append(i)
print(result)

# 47	Find the union of two arrays
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 4, 5, 6]

# union = [1,2,3,4,5,6]
union = []
for i in arr1:
    if not i in union:
        union.append(i)
for i in arr2:
    if not i in union:
        union.append(i)
print(f"Union = {union}")

# 48	Find all pairs whose sum equals a target

arr = [2, 4, 3, 5, 7, 8, 1]
target = 6

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+ arr[j] == target:
            print(arr[i],arr[j])



# 49	Find the maximum difference between two elements

arr = [2, 4, 3, 5, 7, 8, 1]

arr.sort()
# 12345678
maximum = 0 

for i in range(len(arr)):
    for j in range(len(arr)):
        sub = arr[j] -arr[i]
        if sub > maximum:
            maximum = sub 
print(maximum)


# 50	Find the maximum subarray sum
arr = [2, 4, 3, 5, 7, 8, 1]
# output = 30 
result =0 
for i in arr:
    result += i
print(result)