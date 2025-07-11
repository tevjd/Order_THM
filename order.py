#!/usr/bin/env python3
"""This program try to decode the Order challenge by TryHackMe"""

def find_key(hint, encoded):
    """Try to find the key based on a hint and an encoded message"""

    hint_ascii = [ord(i) for i in hint]
    encoded_dec = [int(encoded[i:i+2], 16) for i in range(0, len(encoded), 2)]

    key_list = []
    for i, _ in enumerate(hint_ascii):
        key_byte = hint_ascii[i] ^ encoded_dec[i]
        key_list.append(key_byte)

    return key_list

def decode(key_list, encoded):
    """This function decode the message based on the key"""

    decoded_message = []
    for i, char in enumerate(encoded):
        key_byte = key_list[i%len(key_list)]
        decoded_message.append(key_byte ^ char)

    answer = ""
    for elem in decoded_message:
        answer += chr(elem)

    return answer

if __name__ == "__main__":
    print("We want to decode : 1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60")

    ENCODED_MESSAGE = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"
    ENCODED_MESSAGE_DEC = [int(ENCODED_MESSAGE[i:i+2], 16) for i in \
                           range(0, len(ENCODED_MESSAGE), 2)]
    HINT = "ORDER:"
    key = find_key(HINT, ENCODED_MESSAGE)

    print(f"This is the key: {key}")

    DECODED_MESSAGE = decode(key, ENCODED_MESSAGE_DEC)
    print(f"And here is the result after the decoding: {DECODED_MESSAGE}")
