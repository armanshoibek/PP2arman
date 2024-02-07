def is_palindrome(word):
    word = word.replace(" ", "").lower()
    
    return word == word[::-1]

word = "madam"
print("Is '{}' a palindrome?".format(word), is_palindrome(word))

phrase = "A man a plan a canal Panama"
print("Is '{}' a palindrome?".format(phrase), is_palindrome(phrase))
