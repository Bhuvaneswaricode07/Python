#ifelse Example 7...
#Get input for score out of 100
#if score is<35="Poor Student"
#if score is greater than 35 but <than 70="Average Student"
#if score is greater than 70="Good Student"

score=int(input("Score"))
if(score<35):
 print("Poor Student")
if(score>35 and score<70): #True and True
 print("Average Student")
if(score>70):
 print("Good Student") #else not Compulsory without else if condition give output
 
#NEXT METHOD USING ELIF....

score=int(input("Score:"))
if(score<35):
   print("Poor Student")
elif(score>35 and score<70): 
   print("Average Student")
else:
   print("Good Student")

#NEXT METHOD USING ELIF....
score=int(input(Score:))
if(score<35):
      print("Poor Student")
elif(score>35 and score<70):
      print("Average Student")
elif(score>70 and score<100):
      print("Good Student")
else:
      print("Invalid Score")
      


















      
