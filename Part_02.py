# 16	Reverse a string
char= "hello"
print(char[::-1])

# 17	Check whether a string is palindrome


char ="heheh"
rev= char[::-1]
if char==rev:
    print("palindrome")
else:
    print("not palindrome")

# 18	Count vowels and consonants in a string

vowels= ['a','e','i','o','u']
char= "HELLO"
chars=char.lower()
vowel=0
cons= 0

for i in chars:
    
    if i in vowels:
        vowel +=1
    else:
        cons +=1
print(f"vowels = {vowel}")
print(f"consonants = {cons}")

# 19	Count the frequency of each character

char = "Hello"
freq = {}
chars= char.lower()
for i in chars:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] =1

print(freq)

# 20	Find the first non-repeating character


char = "Hello"
freq = {}
chars= char.lower()
for i in chars:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] =1
print(freq)
for key , value in freq.items():
    if value != 1:
        print(key,"=",value)


# 21	Find the first repeating character
char = "abcaade"
seen = set()
for i in char:
    if i in seen:
        print(i)
        break
    else:
        seen.add(i)
# 22	Remove all spaces from a string

char= "         first repeating character guarantee      "

print(char.replace(" ",""))


# 23	Remove duplicate characters from a string

# method 01
char= "programming"
rem = set()
for i in char:
    rem.add(i)

print(rem)

# mehtod 02


result = ""
for i in char:
    if i not in  result:
        result += i

print(result)



# 24	Check whether two strings are anagrams


char1= "listen"
char2 = "silent"
char01=list(char1)
char02 =list(char2)
char01.sort()
char02.sort()
if char01 == char02:
    print("Anagrams")
else:
    print("not anagrams")


# 25	Count the number of words in a string

char  = "I love Python programming"
word=char.split()
print(len(word))

# 26	Find the longest word in a sentence

char  = "I love Python programming"
word=char.split()
longest=""
for i in word:
    if len(i)>len(longest):
        longest= i

print(longest)


# 27	Find the shortest word in a sentence

char  = "I love Python programming"
word=char.split()
short=word[0]
for i in word:
    if len(i)<len(short):
        short= i

print(short)


# 28	Convert lowercase characters to uppercase without using .upper()

char  = "I Love Python programming"
low_char= ""
for i in char:
    
    num1=ord(i)
    if num1> 96 and num1<122:
        if num1 ==32:
            print(" ",end="")
        num2 = num1 - 32
        upper=chr(num2)
        print(upper,end="")
    else:
        print(chr(num1),end="")


# 29	Find the character with maximum frequency

char = "programming"
freq = {}
chars= char.lower()
for i in chars:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] =1

for key , value in freq.items():
    mx=max(freq.values())
    if value == mx:
        print(key,"=",mx)
        break



# 30	Check whether a string contains only digits
a= "1231"
for i in a:
    # print(i)
    num1=ord(i)
if num1>47 and num1<57:
    print("Digits")
else:
    print("Not Digits")