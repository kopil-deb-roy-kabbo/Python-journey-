import random
computer = random.choice([-1,0,1])
youstr=input("Enter your choice:")
youDict= {"r":1,"p":-1,"s":0}
reverseDict={1:"Rock",-1:"Paper",0:"Scissor"}
you=youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if(computer == you):
    print("Its a draw")
else:
    if(computer==-1 and you ==1)    :
        print("You Lose!")
    elif(computer==-1 and you ==0): 
        print("You Win!") 
    elif(computer==1 and you==-1)   :
        print("You Lose!")   
    elif(computer ==1 and you ==0)  :
        print("You Lose!") 
    elif(computer==0 and you == -1) :
        print("You Lose!") 
    elif(computer==0 and you ==1)   :
        print("You Win!")  
    else:
        print("Something went wrong")     
        
'''
print("same task using unreadable program")  


'''       