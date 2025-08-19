text = input("Enter a word: ").lower()

vowel_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
vowels = "aeiou"

total_vowels = 0
total_consonants = 0

for char in text:
    if char in vowels:
        vowel_count[char] += 1
        total_vowels += 1
    elif char.isalpha():
        total_consonants += 1

print(f"Total vowels: {total_vowels}")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")
print(f"Total consonants: {total_consonants}")
