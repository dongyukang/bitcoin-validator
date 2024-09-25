def calculate_target(compact):
    exponent = compact >> 24
    coefficient = compact & 0x00ffffff
    target = coefficient * (2 ** (8 * (exponent - 3)))
    target_hex = f"{target:064x}"

    return {
        "compact": f"0x{compact:08x}",
        "exponent": f"0x{exponent:02x} ({exponent})",
        "coefficient": f"0x{coefficient:06x} ({coefficient})",
        "targetDecimal": f"{target:,}",
        "targetHex": f"0x{target_hex}",
        "targetBytes": ' '.join([target_hex[i:i+8] for i in range(0, 64, 8)]),
        "difficulty": calculate_difficulty(target)
    }

def calculate_difficulty(target):
    MAX_TARGET=0x00000000FFFF0000000000000000000000000000000000000000000000000000
    return MAX_TARGET / target

def main():
    while True:
        user_input = input("Enter bits (e.g., 0x17038a6d) or 'q' to quit: ").strip()
        
        if user_input.lower() == 'q':
            break

        try:
            compact = int(user_input, 16)
            result = calculate_target(compact)
            
            print("\nResults:")
            print(f"Compact: {result['compact']}")
            print(f"Exponent: {result['exponent']}")
            print(f"Coefficient: {result['coefficient']}")
            print(f"Target (Decimal): {result['targetDecimal']}")
            print(f"Target (Hex): {result['targetHex']}")
            print(f"Target (32 bytes hex): {result['targetBytes']}")
            print(f"Difficulty: {result['difficulty']}")
            print()
        except ValueError:
            print("Invalid input. Please enter a valid hexadecimal number.\n")

if __name__ == "__main__":
    main()
