"""
File: a7.py
Group: Seth Michel and Dillon Mathew
"""

from stack import Stack


def isPalindrome(sentence):
    """Returns True if sentence is a palindrome
    or False otherwise."""
    stk = Stack()  # Creates a stack called stk.
    sentence = sentence.replace(" ", "")  # removes spaces from sentence
    sentence = sentence.lower()  # turns sentence into lower case
    reversed_sentence = []  # will list of characters in sentence but reversed

    for character in sentence:  # pushes each character from sentence in the stk stack
        stk.push(character)
    for i in range(len(sentence)):  # pops each character from stk into the reverse_sentence list (reversing the order of the OG sentence)
        reversed_sentence.append(stk.pop())

    reversed_sentence = "".join(reversed_sentence)  # converts list into a string

    return sentence == reversed_sentence  # returns true if sentence is a palindrome, false if not


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
