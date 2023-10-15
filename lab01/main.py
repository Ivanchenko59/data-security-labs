import sys
import math
import string

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

operation = input()
shift = int(input())

rotors = []
for i in range(3):
    rotor_line = input()
    rotors.append(rotor_line)
    
message = input()


import sys
import math

def doCaesar(message, shift, operation):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 4
    result = []
    if operation == 'ENCODE':
        for i, letter in enumerate(message):
            result.append(alphabet[alphabet.index(letter) + shift + i])
    else:
        for i, letter in enumerate(message):
            result.append(alphabet[alphabet.index(letter) - shift - i])
    return result


def doRotor(message, rotor, operation):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	if operation == 'ENCODE':
		result = [rotor[alphabet.index(letter)] for letter in message]
	else:
		result = [alphabet[rotor.index(letter)] for letter in message]

	return result

def encode(message, shift, rotors):
	coded = message
	coded = doCaesar(coded, shift, 'ENCODE')
	for i, rotor in enumerate(rotors):
		coded = doRotor(coded, rotor, 'ENCODE')
	return coded

def decode(message, shift, rotors):
	decoded = message
	for i in range(len(rotors)-1, -1, -1):
		decoded = doRotor(decoded, rotors[i], 'DECODE')
	decoded = doCaesar(decoded, shift, 'DECODE')

	return decoded

result = encode(message, shift, rotors) if operation == 'ENCODE' else decode(message, shift, rotors)

print(''.join(result))