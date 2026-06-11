

candies=10
for i in range (candies):
    if candies-1==5:
        print("only 5 condies left")
        continue
print("giving a candy to a frnd")g

n=int(input())
i=1
while i<=n:
    print(i)
    i+=1


n=int(input())
sum=0
for i in range(1,n+1):
    sum+=1
    print(sum)
 # leap year
year = int(input())
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
else:
    print("not a lea year")

#profit , loss
cp = int(input())
sp = int(input())
if sp > cp:
    print("profit", sp - cp)
elif sp < cp:
    print("loss", sp - cp)
else:
    print("no profit no loss")

#largest of 3 numbers
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else :
    print(c)

# grade calculation 
marks = int(input())
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("E")

#sum of total
n = int(input("Enter number"))
sum = 0
for i in range (1, n+1):
  sum + = 1
print(sum)

#multiplication table
n = int(input("Enter number"))
for i in range(1,11):
  print(f"{n} x {i} = {n * i}")


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due :{due_date}")
display_invoice("suresh", 50, "10/02")
