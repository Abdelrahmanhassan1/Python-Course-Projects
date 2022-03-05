from traceback import print_tb
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(logo)
print()

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(plain_text, shift_amount):
#     encrypted_text = ""
#     for char in plain_text:
#         current_position = alphabet.index(char)
#         new_position = current_position + shift_amount
#         if new_position > len(alphabet) - 1:
#             new_position -= len(alphabet)
#         encrypted_text += alphabet[new_position]
#     print(encrypted_text)


# def decrypt(encrypted_text, shift_amount):
#     plain_text = ""
#     for char in encrypted_text:
#         current_position = alphabet.index(char)
#         new_position = current_position - shift_amount
#         plain_text += alphabet[new_position]
#     print(plain_text)


def caeser(input_text, shift_amount, caeser_direction):
    output_text = ""
    for char in input_text:
        if char in alphabet:

            current_position = alphabet.index(char)

            if caeser_direction == "encode":
                new_position = current_position + shift_amount
                if new_position > len(alphabet) - 1:
                    new_position -= len(alphabet)

            elif caeser_direction == "decode":
                new_position = current_position - shift_amount

            else:
                print("Invalid coding direction")
                break

            output_text += alphabet[new_position]
        else:
            output_text += char

    print(output_text)


is_ended = True

while is_ended:
    caeser(input_text=text, shift_amount=shift, caeser_direction=direction)
    user_input = input("Want to continue.. type (yes) otherwise type (no): ")
    print()
    if user_input.lower() == "no":
        is_ended = False

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
