from hashlib import sha256

def split_hex_input(hex_input):
    byte_groups = [4, 32, 32, 4, 4, 4]
    result = []
    start = 0
    for group in byte_groups:
        end = start + group * 2  # Each byte is represented by 2 hex characters
        result.append(hex_input[start:end]) 
        start = end
    return result

def little_endian_convert(hex_string):
    byte_pairs = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
    return ''.join(byte_pairs[::-1])

raw_input = input("Enter your 80-byte hexadecimal input: ")
if len(raw_input) == 160: 
    split_result = split_hex_input(raw_input)
    print("Split result:")
    labels = ["Version", "prevBlockHash", "MerkleRoot", "Timestamp", "nBits", "Nonce"]
    for i, (group, label) in enumerate(zip(split_result, labels)):
        little_endian = little_endian_convert(group)
        print(f"{label} ({len(group)//2} bytes): {little_endian}")

    print (f"SHA256 Hash (32 bytes): {little_endian_convert(sha256(sha256(bytes.fromhex(raw_input)).digest()).hexdigest())}")
else:
    print("Invalid input length. Please enter exactly 80 bytes (160 hexadecimal characters).")
