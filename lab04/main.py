import hashlib
def crack(md5_hash):
    for i in range(100000):
        password = str(i).zfill(5)
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == md5_hash:
            return password
    return None