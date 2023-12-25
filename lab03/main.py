import sys
import math

def main():
    """Decodes three encrypted messages using bitwise XOR."""
    message1 = input()
    message2 = input()
    message3 = input()

    m1 = bytes.fromhex(message1)
    m2 = bytes.fromhex(message2)
    m3 = bytes.fromhex(message3)

    m0 = bytearray(len(m1))

    for i in range(len(m0)):
        m0[i] = m1[i] ^ m2[i] ^ m3[i]

    hex_string = m0.hex()
    print("Combined message (hex):", hex_string, file=sys.stderr)

    message = m0.decode("ascii")
    print(message)

if __name__ == "__main__":
    main()
