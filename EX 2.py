#....Question 1...
a=int (input())
b=int (input())
c=int (input())
d=(a*b*c)
print(d)
e=(a+b+c)
print(e)
f=d/e
print(f)

#....Question 2...
name=input()
score=int(input())
department=input()
print("My Name is:",name)
print("My score is:",score/10,"/10")
print("My Department is:",department)

#Indexing...
name , age="Mango" , 34
print(name[4])

#OPERATORS
#Arthimetic Opertor
a=5
b=6
print(a+b)

a=2
b=3
c=10
print(a**b**(a%c))

#Relational Operator
a="Siva"
b="siva"
print(a==b)
print(a<b)

#ASCI VALUE
print('S:', ord('S'))
print('s:', ord('s'))

#Swapping
a=5
b=7
print(a,b)
#temp=a
#a=b
#b=temp
#print(a,b)
a,b=b,a
print(a,b)

#Membership Operator
list=[1,2,3,4,5]
print(9 in list)

#Membership Operator Example 2...
name="Bhuvi anes"
age=21
print('B' in name)
print('B' not in name)
print('G' not in name)

#Membership Operator Example 3...
numbers=[1,4,'2',8,5]
print(2  in numbers) #2 assigned as a String
print(10 not in numbers)

#Logical Operator
a=5
b=10
statement1=(a==10)
statement2=(b==10)
print(statement1 or statement2)

#Bitwise Operator(& | )
a=2
b=3
print(a & b)







