# 1. Print numbers from 1 to N
n= int(input("Enter a number = "))
for i in range(1, n+1):
    print(i)

# 2.Print numbers from N to 1

for i in range(n,0,-1):
    print(i)


# 3.Find the sum of first N natural numbers
sum =0 
for i in range(1,n+1):
    sum = i + sum
print(sum)


# 4.Find the factorial of N
fac = 1
for i in range(1,n+1):
    fac = i * fac
print(fac)


# 5.Check whether a number is even or odd


if n % 2 ==0:
    print("This is Even Number")
else:
    print("This is Odd Number")


# 6.Find the largest of two numbers
num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
if num1 > num2 :
    print("Largest number =",num1)
else:
    print("Largest number = ", num2)

#7. Find the largest of three numbers

num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))
num3 = int(input("Enter third number = "))
if num1 > num2 :
    print("first is Largest number =",num1)
elif num2 >num3:
    print("second is Largest number = ", num2)
else:
    print("third isLargest number = ", num3)


# 8.Count the number of digits in a number


n = 15332
count= 0
while n>0:
    last = n%10
    # print(last)
    n= n//10
    count += 1
print(count)


# 9.Find the sum of digits of a number
n = 15332
sum = 0
while n>0:
    last = n%10
    n= n//10
    sum = last + sum
print(sum)


# 10.Reverse a number
n = 15332

rev = 0 
while n >0 :
    last = n%10
    n= n//10
    rev = rev *10 + last
print(rev)


# 11.Check whether a number is palindrome
n = 101
p =n

rev = 0 
while n >0 :
    last = n%10
    n= n//10
    rev = rev *10 + last
if rev== p :
    print("Palindrome")
else:
    print("Not Palindrome")

#12. Check whether a number is prime

n= int (input("Enter a Number="))
for n in range(2, n+1):
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False

            
            break

if is_prime:
    print("This is prime Number = ", n)
else:
    print("This is Not prime Number = ",n)

# 13.Print all prime numbers from 1 to N

n= int (input("Enter a Number="))
for n in range(2, n+1):
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False

            
            break

    if is_prime:
        print("This is prime Number = ", n)



# 14.Find the GCD/HCF of two numbers


a= 15
b= 24
la=[]
lb=[]
for i in range(1,a):
    if a% i==0:
        la.append(i)
for i in range(1,b):
    if b% i==0:
        lb.append(i)
same= []
for i in la:
    if i in lb:
        same.append(i)
    

for i in same:
    if a%i==0 and b% i==0:
        gcd=i
print(f"The GCD is {gcd}")
       

#15. Find the LCM of two numbers
a= 120
b=18

la =[]
lb=[]
same=[]
for i in range(1,2000):
    var1= a*i
    la.append(var1)
    var2 = b*i
    lb.append(var2)
    for j in la:
        if j in lb:
            same.append(j)
print(min(same))





    


        