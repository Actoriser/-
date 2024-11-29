from collections import Counter

def encode(text):
    encoded = ""
    for char in text:
        
        binary = f"{ord(char):08b}"
        tripled = "".join(bit * 3 for bit in binary)
        encoded += tripled
    return encoded

def decode(bits):
    
    triples = [bits[i:i+3] for i in range(0, len(bits), 3)]
    

    corrected_bits = "".join(Counter(triple).most_common(1)[0][0] for triple in triples)
    
    
    bytes_ = [corrected_bits[i:i+8] for i in range(0, len(corrected_bits), 8)]
    
    
    decoded_text = "".join(chr(int(byte, 2)) for byte in bytes_)
    return decoded_text


if __name__ == "__main__":
    text = "hey"
    encoded_text = encode(text)
    print(f"Encoded: {encoded_text}")
    
    
    noisy_encoded_text = encoded_text[:5] + "0" + encoded_text[6:10] + "1" + encoded_text[11:]
    print(f"Noisy Encoded: {noisy_encoded_text}")
    
    decoded_text = decode(noisy_encoded_text)
    print(f"Decoded: {decoded_text}")