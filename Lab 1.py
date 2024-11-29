import sys


operation = input().strip()
pseudo_random_number = int(input())
rotors = [input().strip() for _ in range(3)]
message = input().strip()


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_shift(message, start_shift, decode=False):
    shifted_message = []
    shift = start_shift
    for char in message:
        if decode:
            new_index = (alphabet.index(char) - shift) % 26
        else:
            new_index = (alphabet.index(char) + shift) % 26
        shifted_message.append(alphabet[new_index])
        shift += 1
    return "".join(shifted_message)


def apply_rotor(message, rotor, decode=False):
    mapped_message = []
    for char in message:
        if decode:
            
            mapped_char = alphabet[rotor.index(char)]
        else:
            
            mapped_char = rotor[alphabet.index(char)]
        mapped_message.append(mapped_char)
    return "".join(mapped_message)


if operation == "ENCODE":
    
    intermediate_message = caesar_shift(message, pseudo_random_number)
    
    
    for rotor in rotors:
        intermediate_message = apply_rotor(intermediate_message, rotor)
    
    print(intermediate_message)

elif operation == "DECODE":
    
    intermediate_message = message
    for rotor in reversed(rotors):
        intermediate_message = apply_rotor(intermediate_message, rotor, decode=True)
    
    
    decoded_message = caesar_shift(intermediate_message, pseudo_random_number, decode=True)
    
    print(decoded_message)