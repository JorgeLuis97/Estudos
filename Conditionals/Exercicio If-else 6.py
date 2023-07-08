# Exercise 6: Palindrome Check
# Write a program that takes a string as input from the user and determines if it is a palindrome or not.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

Word = input("Word: ")
Word_list = list(Word)
Word_list.reverse()
Reversed_Word = ''.join(Word_list)

if Word.upper() == Reversed_Word.upper():
    print(f"{Word} Its a Palindrome")
else:
    print(f"{Word} Isn't a Palindrome")
