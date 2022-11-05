"""
File: a7.py

"""

from stack import Stack


def isPalindrome(sentence):
    """Returns True if sentence is a palindrome
    or False otherwise."""
    stk = Stack()  # Creates a stack called stk.
    sentence = sentence.replace(" ", "")  # removes spaces from sentence
    sentence = sentence.lower()
    comparative_sentence = []

    for character in sentence:
        stk.push(character)
    for i in range(len(sentence)):
        comparative_sentence.append(stk.pop())

    comparative_sentence = "".join(comparative_sentence)

    if sentence == comparative_sentence:
        return True

    return False


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


if __name__ == '__main__':
    main()
