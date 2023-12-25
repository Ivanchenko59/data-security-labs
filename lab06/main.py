import numpy as np

def scanner(qrcode):
    def toggle_bit(val):
        return 1 - val
    
    def extract_letters(encoded_data):
        letter_count = int(encoded_data[:8], 2)
        encoded_data = encoded_data[8:]
        word = ''
        for i in range(0, (letter_count * 8) + 11, 8):
            word += chr(int(encoded_data[i:i+8], 2))
            if len(word) == letter_count:
                return word

    def transform_qrcode(qr_code):
        qr_code = np.array([[toggle_bit(val) if (i + j) % 2 == 0 else val for j, val in enumerate(row)] for i, row in enumerate(qr_code)])
        qr_code = qr_code[9:]
        odd, output = 0, []
        for i in [19, 17, 15, 13]:
            columns = qr_code[:, [i, i + 1]]
            direction = 1 if odd == 1 else -1
            for row in columns[::direction]:
                output += row.tolist()[::-1]
            odd = 1 - odd
        return ''.join(map(str, output[4:]))

    processed_qrcode = transform_qrcode(qrcode)
    result = extract_letters(processed_qrcode)
    
    print(result)
    return result