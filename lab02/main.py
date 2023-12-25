import sys

def encode_decalage(text, decalage):
    """Encodes a string by shifting letters by a specified decalage."""
    result = []
    for char in text:
        if char.isalpha():
            base_char = 'a' if char.islower() else 'A'
            encoded_char = chr(((ord(char) - ord(base_char) + decalage) % 26) + ord(base_char))
            result.append(encoded_char)
        else:
            result.append(char)
    return ''.join(result)

def proba_text_anglais(text):
    """Calculates the probability of a string being English based on letter frequencies."""
    a = ord('a')
    proba = [8.08, 1.67, 3.18, 3.99, 12.56, 2.17, 1.8, 5.27, 7.24, 0.14, 0.63, 4.04, 2.6, 7.38, 7.47, 1.91, 0.09, 6.42, 6.59, 9.15, 2.79, 1, 1.89, 0.21, 1.65, 0.07]
    frequence = [0] * 26

    text = text.lower()

    for char in text:
        index = ord(char) - a
        if 0 <= index <= 25:
            frequence[index] += 1

    len_str = len(text)
    score = 0

    for i in range(26):
        p = (frequence[i] / len_str) * 100
        score += (proba[i] - p) ** 2

    return score ** 0.5

def main():
    """Finds the most likely decoded string from a Caesar cipher."""
    message = input()
    score_min = float('inf')
    best_text = ''

    for i in range(26):
        text = encode_decalage(message, i)
        score = proba_text_anglais(text)

        if score < score_min:
            score_min = score
            best_text = text

    print(best_text)

if __name__ == '__main__':
    main()
