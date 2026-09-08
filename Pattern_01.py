# for i in range(4):
#     for j in range(4):
#         print("*",end=" ")
#     print()

n=5

# for i in range(n+1):
#     for j in range(n-i):
#          print(" ",end="")
#     for j in range(i) :
#         print("*", end= "")
#     print()

# for i in range(n+1):
#     for j in range(n-i):
#          print(" ",end="")
#     for j in range(i) :
#         print("*", end= " ")
#     print()
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print(j, end=" ")
#     print()



# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
    
           
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(2*n-(2*i+1)):
#         print("*",end="")
#     for j in range(i):
#         print(" ",end="")
           
#     print()


n= 5
# for i in range(1,2*n):
#     stars = i
#     if i > n :
#         stars =2*n-i
#     for j in range(stars):
#         print("*",end="")
#     print()



# for i in range (1,n+1):
#     if i %2 == 0:
#         start = 1
#     else:
#         start = 0
#     for j in range(i):
#         start = 1- start
#         print(start,end="")
#     print()

# space=2*(n-1)
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range(space):
#         print(" ",end="")

#     for j in range(i,0,-1):
#         print(j,end="")
#     print()
#     space-=2

# count = 1
# for i in range(n+1):
#     for j in range(i):
#         print(count, end= " ")
#         count +=1
        
#     print()



# for i in range(n):
#     for j in range(i) :
#         print(chr(65+j), end=" ")
#     print()


# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print(chr(64+j), end=" ")
#     print()

# for i in range(1,n):
#     for j in range(i):
#         print(chr(64+i),end="")
    
#     print()

# for i in range(n):
#     ch= chr(65+i)
    
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print(ch,end="")
#     print()



# for i in range(n):
#     for j in range(69,69-i-1,-1):
#         print(chr(j),end="")
    
#     print()


# for i in range (n):
#     for j in range(n-i):
#         print("*",end="")
#     for j in range(2,i+2):
#             print(" ",end="")
#     for j in range(i):
#          print(" ",end="")
#     for j in range(n-i):
#         print("*",end="")
#     print()
# for i in range (n):
#     for j in range(i+1):
#         print("*",end="")
#     for j in range(2 * (n - i - 1) ):
#         print(" ",end="")
    
#     for j in range(i+1):
#         print("*",end="")
#     print()

n = 5

space = 2 * n - 2

for i in range(1, 2 * n):

    # Stars
    star = i

    # Lower half
    if i > n:
        star = 2 * n - i

    # Left stars
    for j in range(star):
        print("*", end="")

    # Middle spaces
    for j in range(space):
        print(" ", end="")

    # Right stars
    for j in range(star):
        print("*", end="")

    # Space update
    if i < n:
        space -= 2
    else:
        space += 2

    print()