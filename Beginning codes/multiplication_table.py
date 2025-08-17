n=int(input("Enter a number:")) #Take number from user.
#starts for loop
print("Table of",n,"using for loop")
for i in range(1,11): #takes 1 to 10 numbers into the variable i
    print(f"{n} X {i} = {n*i}") #runs the program 
    
    
#same task completed by while loop

#n=int(input("Enter a number:"))
print("\nMultiplication table of",n,"using while loop")
print()
i=1
while(i<11):
    print(f"{i} times {n}: {n} X {i} = {n*i}")
    i+=1
    
print("\nreverse table\n")  
for i in range(1,11) :
    print(f"{n}X{11-i}={n*(11-i)}")
print("\n reverse table using while loop\n") 
i=1
while(i<11)   :
    print(f"{n}X{11-i}={n*(11-i)}")
    i+=1 # i=i+1
print("\nsame task using recursion\n")  
def multiplication(n)  :
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")
multiplication(n)        