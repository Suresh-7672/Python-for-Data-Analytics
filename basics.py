

#candies=10
#for i in range (candies):
#    if candies-1==5:
 #       print("only 5 condies left")
 #       continue
#print("giving a candy to a frnd")g

#n=int(input())
#i=1
#while i<=n:
 #   print(i)
 #   i+=1


n=int(input())
sum=0
for i in range(1,n+1):
    sum+=1
    print(sum)

# grade calculation 
marks = int(input("Enter marks : "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("E")

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

#profit , loss
cp = int(input())
sp = int(input())
if sp > cp:
    print("profit", sp - cp)
elif sp < cp:
    print("loss", sp - cp)
else:
    print("no profit no loss")

# leap year
year = int(input())
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
else:
    print("not a lea year")
