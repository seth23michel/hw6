"""
File: a7.py

"""

from stack import Stack

def isPalindrome(sentence):          
    """Returns True if sentence is a palindrome
    or False otherwise."""
    stk = Stack() # Creates a stack called stk.

    # *** Write your code here ***
    
    return True

# *** Do not modify main() ***
def main():
    while True:
        sentence = input("Enter some text or just hit Enter to quit: ")
        if sentence == "":
            break
        elif isPalindrome(sentence):
            print("It's a palindrome.")
        else:
            print("It's not a palindrome.")

main()
