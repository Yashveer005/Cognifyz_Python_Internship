def is_palindrome(s):       #PALINDROME CHECKER
    #Remove spaces and convert the string to lowercase
    s = s.replace(" ", " ").lower()

    #compare the string with its reverse
    return s == s[::-1]

#Test the function with some examples
test_strings = [
    "google",
    "apple",
    "oppo",
    "level",
    "cognifyz",
    "deed",
    "malayalam"
]

for string in test_strings:
    if is_palindrome(string):
        print(f"{string} is a palindrome.")
    else:
        print(f"{string} is NOT a palindrtome.")