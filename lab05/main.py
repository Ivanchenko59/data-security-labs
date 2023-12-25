def encode(string):
    bits = []
    for c in string:
        byte = (bin(ord(c))[2:]).zfill(8)
        bits.extend(b * 3 for b in byte)
    return ''.join(bits)


def decode(bits):
    
    result = []
    c = ''
    
    for i in range(0, len(bits)-2, 3):
        t = bits[i:i+3]
        b = sorted(t)[1]
        c += b
        if len(c) == 8:
            result.append(chr(int(c, 2)))
            c = ''

    return ''.join(result)
        