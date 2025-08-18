b=str(input("Enter your word: "))
word=b.lower()
a  = word[::-1]
reverse_word=a.lower()
if (word==reverse_word ):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not palindrome.")    
