n=int(input("Enter the number: "))
print("Using while loop")
i=1          #start muliplication from 1
product=1    #the value of product is 1 in the beginning
while(i<=n): #the programm will run from 1 ,and runs till the value of i is less than or equal n
    product=product*i  #product = product + i
    i+=1     #i = i + 1
     
     
print(product)
print("same task using for loop")
product=1
for i in range(1,n+1):
     product=product*i # sum =sum+i
print (product)
print("Factorial using recursion")
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1) 
print(f"The factorial of the number {n} is {factorial(n)}")       