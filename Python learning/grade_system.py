import sys

print()
print("Grade System")
print("************")
print()

#Enter the Mark
print("Enter the mark between 0 to 100") 
print()

mark = float(input("Enter the student mark: "))

 #checking for decimal values
try:
       	if not mark.is_integer():
            raise ValueError("Mark should be an integer value")
except ValueError as e:
	print(e) 
	sys.exit()

try:
#checking for negative values 
   if mark < 0:
    raise ValueError("Error:Mark cannot be negative") 
except ValueError as e:
   print(e)
   sys.exit()
if(mark>=90 and mark<=100):
    print("Your grade is A")
else:
 if(mark>=80 and mark<=89):
    print("Your grade is B")   
 else:
     if(mark>=70 and mark<=79):
        print("Your grade is C") 
     else:
          if(mark>=60 and mark<=69):
             print("Your grade is D") 
          else:
   
            if(mark<60):
               print("Your grade is E")
            else: 
                 if(mark>100):
                    print("Mark cannot be more than 100")
                    
 