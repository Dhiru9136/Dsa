# 51	Find the frequency of elements using a dictionary
arr = [2, 4, 2, 5, 4, 2, 7]
# Output = {2: 3, 4: 2, 5: 1, 7: 1}

freq ={}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

# 52	Find the first element that appears only once
arr = [2, 4, 2, 5, 4, 2, 7]

freq ={}
for i in arr:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1

for key, value in freq.items():
    if value ==1:
        print(key)
        break