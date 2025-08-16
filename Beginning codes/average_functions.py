def average_function():   #starts a Function.

    n=int(input("Enter how many numbers you have: "))    #takes input of how many numbers, from users.
    total=0 #initial value of sum is 0
    for i in range(n): #starts a for loop
        num=int(input(f"Enter number{i+1}: ")) #takes input of numbers from users
        total += num  #on every loop sum the value of total and num and save it into total.       
    average=total/n   #divides total by n
    print (f"average is {average}") #prints the average value
 
average_function()  #call the Function 
 
