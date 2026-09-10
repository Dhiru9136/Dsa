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