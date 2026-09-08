# # n= 7789
# # while n>0:
# #     last= n% 10 
# #     print(last)
# #     n =n//10
# # print(n)


# # Sum of digit

# n= 123
# count= 0 
# while n>0:
#     n= n//10
#     count+=1
# print(count)
n=1012

#Write Your Code Here
def reverse(n):
    revnmuber=0
    prev=n
    while n>0:
      

        last = n%10
        n=n//10
        revnmuber=(revnmuber*10)+last

    if prev == revnmuber:
        print("Palindrome")
    else:
        print("Not Palindrome")
    return revnmuber


print(reverse(n))