#Ask the user for a string and print out whether this string is a palindrome or not.
#  (A palindrome is a string that reads the same forwards and backwards.)


word = (input(str("Enter your word  ")))
word = str(word)
reverse = word[::-1]
print(reverse)

if word == reverse:
    print("Your word is a palindrome")
else:
    print("No it isn't")
