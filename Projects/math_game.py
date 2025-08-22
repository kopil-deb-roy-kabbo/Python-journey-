import random

z=random.randint(5,10)
h=random.randint(10,20)
print("\t    Welcome to the math game\n")
print("\t1.easy\n\t2.Medium\n\t3.Hard")
level=input("\n#Select your difficulty : ")
def level1():
    print("You have selected the easy Level.")
    ans=float(input(f"\nFirst of all do the sum of {x} and {y}.Then divided the answer by two and enter the result: "))
    res=float(((x+y)/2))
    if(ans==res):
        print("\nYou are genius.")
    else:
        print("\nTry again.")    
def level2():
    print("You have selected the Medium Level.")
    ans=int(input(f"\nEnter the factorial of {z}: "))
    product=1
    for i in range(1,z+1):
     product=product*i 
    if(product==ans):
        print("You are genius👑.")
    else:
        print("You lose!\nTry next time.")    

def level3():
    print("You have selected the Hard Level")
    ans=int(input(f"\nEnter the factorial of {h}: "))
    product=1
    for i in range(1,h+1):
     product=product*i 
    if(ans==product):
        print("You are a genius.")
    else:
        print("You are a looser!")    

if(level=="1"):
        x=random.randint(1,1000)
        y=random.randint(1,1000)
        level1()
        if(==1)


elif(level=="2"):
       level2()
    
elif(level=="3"):
      level3()

else:
        print("Invalid input.Try again!")    
  

    
