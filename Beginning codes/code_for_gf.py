n=int(input("Enter how many lines you need: "))
with open("Love.txt","w") as f:
     for i in range(1,n+1):
          f.write("I love You\n")
