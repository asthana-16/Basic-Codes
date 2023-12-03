ch= (input("ch: "))
vowels = ["A","E","I","O","U","a","e","i","o","u"]
if ch.isalpha():
    if (ch in vowels):
        print("vowels")
    else:
        print("consonant")
else:
    print("Not an alphabet")

b = "Hello, World!"
print(b[2:8:2])


# pascals triangle of n rows
rows = int(input("rows: "))
for index in range(0, rows):
    for spaces in range(rows, index, -1):
        print(' ', end='')
    number = 1
    for col in range(0, index + 1):
        print("%d " % number, end ='')
        number = number * (index - col)/(col + 1)
    print()

# to find greater number among the following
a, b, c = (input("a,b,c: ").split(','))
a, b, c = [int(a), int(b), int(c)]
if (a > b and a > c):
    print(a)
elif (b > c and b > c):
    print(b)
else:
    print(c)    

count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")

# for prime number
num = int(input("num: "))
if num > 1:
    
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break 
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

sumfact = 0
num = int(input("num:"))
temp = num
while(num):
    i = 1
    fact = 1
    digit = num % 10
    while(i <=digit):
       fact = fact * i
       i = 1 + 1
    sumfact = sumfact + fact
    num = num // 10
if(sumfact == temp):
   print("strong number")
else:
   print("not a strong number")



num = int(input("enter the number:"))
s=0
li=[]
for i in range(1,num):
    if num%i==0:
        s+=i
        li+=[i]
print("factors:",li)
print("sum",s)
if s==num:
    print("perfect")
elif s>num:
    print("abundant")
else:
    print("deficient")


