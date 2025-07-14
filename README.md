# XOR Cipher Challenge TryHackMe by Skynnet

## Problem Description

This challenge involves decrypting an intercepted message that was encrypted using a repeating-key XOR cipher. The attackers made a critical error by always starting their messages with a known header, which provides us with the leverage needed to break the encryption.

**Given:**
- Encrypted message (in hexadecimal): `1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60`
- Known header: `ORDER:`

## Algorithm Analysis

### XOR Cipher Properties
XOR (exclusive OR) encryption has a crucial property: **XOR is its own inverse**
- If `A XOR B = C`, then `C XOR B = A`
- This means if we know the plaintext and ciphertext, we can recover the key
- Once we have the key, we can decrypt the entire message

### Repeating-Key XOR
- A short key is repeated to match the length of the message
- Each byte of plaintext is XORed with the corresponding byte of the repeating key
- Example: Key "ABC" encrypting "HELLO" → A⊕H, B⊕E, C⊕L, A⊕L, B⊕O

## Solution Approach

### Step 1: Key Recovery
Since we know the message starts with "ORDER:", we can recover the first 6 bytes of the key:
1. Convert the known header to ASCII values
2. Convert the first 6 bytes of the hex message to decimal
3. XOR them together: `key_byte = known_plaintext_byte XOR ciphertext_byte`

### Step 2: Message Decryption
With the recovered key, decrypt the entire message:
1. Convert the full hex message to decimal bytes
2. Apply the key cyclically (repeat the key as needed)
3. XOR each message byte with the corresponding key byte
4. Convert the result back to ASCII characters

## Code Structure

The solution contains two main functions:

- `find_key()`: Recovers the encryption key using the known header
- `decode()`: Decrypts the entire message using the recovered key

## Key Recovery Process

```
Known header: "ORDER:" → [79, 82, 68, 69, 82, 58] (ASCII)
First 6 hex bytes: 1c1c010419637 → [28, 28, 1, 4, 25, 99] (decimal)
XOR operation:
79 ⊕ 28 = 83 (S)
82 ⊕ 28 = 78 (N)  
68 ⊕ 1 = 69 (E)
69 ⊕ 4 = 65 (A)
82 ⊕ 25 = 75 (K)
58 ⊕ 99 = 89 (Y)
```

**Recovered Key**: `SNEAKY` (ASCII values: [83, 78, 69, 65, 75, 89])

## Usage

```python
python3 xor_decoder.py
```

## Output

```
We want to decode : 1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f63731a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60
This is the key: [83, 78, 69, 65, 75, 89]
And here is the result after the decoding: **solution_here**.
```