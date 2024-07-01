#forloop Example 1.....
for i in "Apple": #i is a variable
    print(i)
    
#forloop Example 2.....
for i in range(5): #it store la no(0to4)
    print(i)

#forloop Example 3.....
for i in range(1,5): 
    print(i)
#forloop Example 4.....( 2 table)
for i in range(1,11):
    print(i,"*2=",i*2)
    
#forloop Example 5.....( 3 table)
for i in range(1,11):
    print(i,"*3=",i*3)

#forloop Example 6.....
a=int(input())
b=int(input())
for i in range(a+1,b):
    print(i)
    
#forloop Example 7.....
for i in range(1,11):#for loop 10 times run
    if(i%2==0):
        print(i) #if 5 times running

#forloop Example 8.....
#Count the number of even numbers between 1 to 10 
count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count)

#forloop Example 9.....
#Count the number of odd and even number between 1 to 10 and print it
e_count=0
o_count=0
for i in range(1,11):
    if(i%2==0):
        e_count=e_count+1
    else:
        o_count=o_count+1
print(e_count)
print(o_count)
#forloop Example 10.....
#count the number divisible by 3 and 5 Range 1-100
count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)
        












        
