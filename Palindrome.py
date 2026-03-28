text = "Civic".lower()
start = 0
end = len(text) - 1
isPalindrome = False
while(start < end):
    if (text[start] == text[end]):
        start = start + 1
        end = end - 1
        isPalindrome = True
    else:
        isPalindrome = False
        break
        
print(f"{text} is Palindrome: {isPalindrome}")