import random

print("Welcome to the number game🫂")
print("You have 5 chances only")
print("Here you can select your difficulty.")
print("For 1-20 words select  :1\nFor 1-50 words select  :2\nFor 1-100 words select :3")
level=int(input("\nSelect your difficulty :"))
if(level==1):
    print("\nYou have selected easy level.")
    x=random.randint(1,21)
    for i in range(1,5):
        k=int(input("\nGuess a number :"))
        if(x==k):
            print(f"You are great.You choosed the correct number.It is {x}")
            break
        elif((abs(x-k))<6):
            print("You are very close!")
        else:
            print("You are too far bro!")
    else:
        print(f"Nice try bro.The number was {x}")    
elif(level==2):
    print("\nYou have selected medium level.")
    x=random.randint(1,51)
    for i in range(1,5):
        
        k=int(input("\nGuess a number :"))
        if(x==k):
            print(f"You are great.You choosed the correct number.It is {x}")
            break
        elif((abs(x-k))<11):
            print("You are very close!")
        else:
            print("You are too far bro!")   
    else:
        print(f"Nice try bro.The number was {x}")              
elif(level==3):
    print("\nYou have selected difficult level.")
    x=random.randint(1,101)
    for i in range(1,5):
       k=int(input("\nGuess a number :"))
       if(x==k):
            print(f"You are great.You choosed the correct number.It is {x}")
            break
       elif((abs(x-k))<11):
            print("You are very close!")
       else:
            print("You are too far bro!") 
    else:
        print(f"Nice try bro.The number was {x}")
else:
    print("\nInvalid choice")            
