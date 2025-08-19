name="Kopil Deb Roy Kabbo"
kabbo="Kabbo"
digits="69"
numeric="12Kabbo"

#Case Conversion
lower=name.lower()            #lowercase all characters 
print(f"1.{lower}")            
upper=name.upper()            #uppercase all characters
print("2.",upper)
title=name.title()            #Capitalize all the first character from every word
print("3.",title)
capitalize=name.capitalize()  #capitalize the first word of line
print("4.",capitalize)
swapcase=name.swapcase()      #swaps between capital and small word
print("5.",swapcase)

#Searching/Finding

#Whitespace/Strip
strip=name.strip()           
print("6.",strip)
lstrip=name.lstrip()          
print("7.",lstrip)
rstrip=name.rstrip()         
print("8.",rstrip)
#Check/Test Methods
isalpha=kabbo.isalpha()       #True if there is only alphabets
print("9.",isalpha)
isdigit=digits.isdigit()      #True if there is only numbers 
print("10.",isdigit)
isnumeric=digits.isnumeric()  #True if there is anuly number in the string
print("11.",isnumeric)
isalnum=numeric.isalnum()     #True if there is number and alphabets  
print("12.",isalnum)
islower=lower.islower()       #True if there is only lowercase
print("13.",islower)
isupper=upper.isupper()       #True if there is only uppercase
print("14.",isupper)
istitle=title.istitle()       #True if there is title case
print("15.",istitle)
isspace=name.isspace()        #True for whitespace 
print("16.",isspace)
isdecimal=digits.isdecimal()  #True for decimals only
print("17.",isdecimal)

#Replacements/Modification



    
