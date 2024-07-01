##ifelse Example 8...
#Make a mini calculator
#Get input for 2 numbers a and b
#Get input from user whether to add/sub/mul/div
#if user selects add then add the two number and Print the result.
a=int(input("A:"))
b=int(input("B:"))
operator=input("add/sub/mul/div:")
if(operator=="add"): #it check add==add
 print(a+b)
elif(operator=="sub"):
 print(a-b)
elif(operator=="mul"):
 print(a*b)
elif(operator=="div"):
 print(a/b)
else:
 print("Invalid Input")

#ifelse Example 9...
#Get a input for score percentage.Only if the percentage is greater than 70,
#get input for his name,department and location.Then print you are eligible.
#If not print you are not eligible.
score=int(input("score percentage:"))
if(score>=70):
 name=input("Enter your name:")
 department=input("Enter your department:")
 location=input("Enter your location:")
 print("you are eligible")
else:
 print("you are not eligible")

#ifelse Example 10...
#Get input for salary and age.
#If salary greater than or equal 20000 or age less than or equal to 25,
#get input for required loan amount.If not print your are not eligible for loan.
#If required loan amount is less than or equal to 50,000 print you are eligible
#for loan.If it is greater than 50,000print maximum loan amount is 50000
Salary=int(input("Salary:"))
Age=int(input("Age:"))
if(Salary>=20000 or Age<=25):
    loan=int(input("Loan:"))
    if(loan>50000): #Using Nested if here
        print("Maximum loan amount is 50000")
    else:
        print("you are eligible for loan")
else:
    print("you are not eligible")
