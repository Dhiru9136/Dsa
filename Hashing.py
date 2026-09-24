# # 51	Find the frequency of elements using a dictionary
# arr = [2, 4, 2, 5, 4, 2, 7]
# # Output = {2: 3, 4: 2, 5: 1, 7: 1}

# freq ={}
# for i in arr:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)

# # 52	Find the first element that appears only once
# arr = [2, 4, 2, 5, 4, 2, 7]

# freq ={}
# for i in arr:
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i] = 1

# for key, value in freq.items():
#     if value ==1:
#         print(key)
#         break

# # 53 Find duplicate elements in an array
# arr = [2, 4, 2, 5, 4, 2, 7]
# freq= {}
# for i in arr:
#     if i in freq:
#         freq[i] = freq[i] +1
#     else:
#         freq[i] = 1


# for i in freq:
#     if freq[i] > 1:
#         print(i)


# 54 Find elements that appear more than once
# arr = [2, 4, 2, 5, 4, 2, 7]
# freq= {}
# for i in arr:
#     if i in freq:
#         freq[i] = freq[i] +1
#     else:
#         freq[i] = 1


# for i in freq:
#     if freq[i] > 1:
#         print(i)

# Find two numbers whose sum equals a target
arr = [2, 4, 2, 5, 4, 2, 7]
target= 12
freq= {}
for i in arr:
    if i in freq:
        freq[i] = freq[i] +1
    else:
        freq[i] = 1
for i in range(len(freq)): #2
    for j in range(i+1, len(freq)): #4
        if list(freq.keys())[i] + list(freq.keys())[j] == target:
            print(list(freq.keys())[i], list(freq.keys())[j])