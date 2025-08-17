n=int(input("Enter your number:"))
print("HOLLOW SQUARE using for loop")
for i in range (1,n+1):
    if(i==1 or i==n):
        print("S"*n)
    else:
        print("S",end="")   
        print(" "*(n-2),end="") 
        print("S")
print("HOLLOW SQUARE using while loop")
i=1
while(i<=n):
    if(i==1 or i==n) :
        print("K"*n)
    else:
        print("K",end="")
        print(" "*(n-2),end="")
        print("K")    
    i+=1    