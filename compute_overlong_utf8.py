banner = """   _____   _____ ___ _    ___  _  _  ___    _   _ _____ ___    ___ 
  / _ \ \ / / __| _ \ |  / _ \| \| |/ __|  | | | |_   _| __|__( _ )
 | (_) \ V /| _||   / |_| (_) | .` | (_ |  | |_| | | | | _|___/ _ \\
  \___/ \_/ |___|_|_\____\___/|_|\_|\___|   \___/  |_| |_|    \___/                                                                   
             ___ ___ ___  _   _ ___ _  _  ___ ___ ___              
            / __| __/ _ \| | | | __| \| |/ __| __/ __|             
            \__ \ _| (_) | |_| | _|| .` | (__| _|\__ \             
            |___/___\__\_\\\___/|___|_|\_|\___|___|___/                                                                                
                                                                   """
line1 = "======================================================================"
line2 = "----------------------------------------------------------------------"

def compute_overlong_sequences(char):
    ascii_code = ord(char)
    
    # 2-byte sequence
    sequence = [0xc0 + (ascii_code >> 6), 0x80 + (ascii_code & 0x3f)]
    print_overlong_sequence(char, 2, sequence)
    
    # 3-byte sequence
    sequence = [0xe0 + (ascii_code >> 12), 0x80 + ((ascii_code >> 6) & 0x3f), 0x80 + (ascii_code & 0x3f)]
    print_overlong_sequence(char, 3, sequence)

    # 4-byte sequence
    sequence = [0xf0 + (ascii_code >> 18), 0x80 + ((ascii_code >> 12) & 0x3f), 
                0x80 + ((ascii_code >> 6) & 0x3f), 0x80 + (ascii_code & 0x3f)]
    print_overlong_sequence(char, 4, sequence)


def print_overlong_sequence(char, length, sequence):
    print(f"Overlong {length}-byte sequence:", end=" ")
    
    # Print character representation
    for byte in sequence:
        print(chr(byte), end="")
    print()
    
    # Print hexadecimal representation
    print("                          Hex: ", end="")
    for byte in sequence:
        print(hex(byte)[2:].zfill(2), end=" ")
    print()
    
    # Print binary representation
    print("                          Binary: ", end="")
    for byte in sequence:
        print(bin(byte)[2:].zfill(8), end=" ")
    print()
    print()
    
if __name__ == '__main__':
    # Print banner
    print(line1)
    print(banner)
    print(line1)
    print()
    
    while True:
        try:
            char = input("Enter an ASCII character: ")
            if len(char) != 1 or not char.isascii():
                raise ValueError("Invalid input. Please enter a single ASCII character.")
            print(f"ASCII character {char}: Decimal {ord(char)}, Hex {hex(ord(char))}, Binary {bin(ord(char))[2:].zfill(8)}")
            print(line2)
            compute_overlong_sequences(char)
            print(line1)
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            exit(0)
        print()
