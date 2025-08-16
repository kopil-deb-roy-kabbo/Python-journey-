def average_function():

    n=int(input("Enter how many numbers you have: "))
    total=0
    for i in range(n):
        num=int(input(f"Enter number{i+1}: "))
        total += num        
    average=total/n
    print (f"average is {average}")
 
average_function()  
 
