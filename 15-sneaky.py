# This pseudo-encryption method works by shifting each letter in a message a fixed amount, so for example:

# shift_cipher("b", 1)     # --> "c"
# shift_cipher("b", 2)     # --> "d"
# shift_cipher("b", -1)    # --> "a"
# shift_cipher("bbc", 1)   # --> "ccd"
# shift_cipher("bbc", -1)  # --> "aab"
# shift_cipher("bbc", 3)   # --> "eef"
# Can you implement this 2000 year old cipher?

# You can use the ord built-in method to turn a character into its corresponding number.

# You can use the chr built-in method to turn a number into its corresponding character.

# Think through this problem. It may seem complex, but you can do this.

# What gets returned for an empty string?
# Can you do this with a single if statement?
# Can you do this with a for loop?
# ord("a") # Returns 97, the integer value for the letter "a"
# chr(97)  # Returns "a"
# chr(98)  # Returns "b"

# def shift_cipher(message, shift):

#     sneaky = []

#     for i in message:
#         sneaky.append(chr(ord(i) + shift))

#     return "".join(sneaky)


# def shift_cipher(message, shift):
#     return "".join(chr(ord(i) + shift) for i in message)


def shift_cipher(message, shift):
    secret_message = ""
    for index in range(len(message)):
        char = message[index]
        ascii = ord(char)
        secret_message += chr(ascii + shift)
        return secret_message



print(shift_cipher("abcdef", 1))




# def shift_cipher(message, shift):
#     return ''.join(chr(ord(c) + shift) for c in message)
