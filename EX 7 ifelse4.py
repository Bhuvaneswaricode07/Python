#ifelse Example 11...
#Get input for five subjects marks.Add all of it, And find average.If average
#mark is less than 35.Print "Additional class is required" else Print "you are
#good to go".
a=int(input("Enter Tamil Mark:"))
b=int(input("Enter English Mark:"))
c=int(input("Enter Maths Mark:"))
d=int(input("Enter Science Mark:"))
e=int(input("Enter Social Mark:"))
f=a+b+c+d+e/5
avg=f/5
if(avg<35):
    print("Additional class is required")
else:
    print("You good to go")
