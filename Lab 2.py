import sys
import string
from collections import Counter

# Frequency of letters in English language
english_frequencies = {
    'A': 8.08, 'B': 1.67, 'C': 3.18, 'D': 3.99, 'E': 12.56,
    'F': 2.17, 'G': 1.80, 'H': 5.27, 'I': 7.24, 'J': 0.14,
    'K': 0.63, 'L': 4.04, 'M': 2.60, 'N': 7.38, 'O': 7.47,
    'P': 1.91, 'Q': 0.09, 'R': 6.42, 'S': 6.59, 'T': 9.15,
    'U': 2.79, 'V': 1.00, 'W': 1.89, 'X': 0.21, 'Y': 1.65,
    'Z': 0.07
}

# Convert frequencies to percentages
english_frequencies = {k: v / 100 for k, v in english_frequencies.items()}

# Input message
message = input()

def decode_shift_cipher(message):
    # Count frequencies of letters in the message (case-insensitive)
    letter_counts = Counter(c.upper() for c in message if c.isalpha())
    total_letters = sum(letter_counts.values())

    # Calculate frequency in the message
    message_frequencies = {
        letter: count / total_letters for letter, count in letter_counts.items()
    }

    # Find the most likely shift by comparing frequencies
    best_shift = 0
    smallest_difference = float('inf')

    for shift in range(26):  # Try all possible shifts
        difference = 0
        for letter, freq in english_frequencies.items():
            shifted_letter = chr(((ord(letter) - 65 + shift) % 26) + 65)  # Apply shift
            observed_freq = message_frequencies.get(shifted_letter, 0)
            difference += abs(freq - observed_freq)
        if difference < smallest_difference:
            smallest_difference = difference
            best_shift = shift

    # Decode the message using the best shift
    decoded_message = []
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decoded_char = chr(((ord(char) - base - best_shift) % 26) + base)
            decoded_message.append(decoded_char)
        else:
            decoded_message.append(char)  # Keep non-alphabetic characters as-is

    return ''.join(decoded_message)

# Get the decoded message
decoded_message = decode_shift_cipher(message)

# Print the result
print(decoded_message)