# Palindrome Checker
# Write a function that checks whether a string reads the same backward
# as forward, ignoring spaces, punctuation, and capitalization.
# Keep letters and digits. An empty string (including one containing only
# spaces or punctuation) counts as a palindrome.


def is_palindrome(text):
    normalized = "".join(character.lower() for character in text if character.isalnum())
    return normalized == normalized[::-1]
