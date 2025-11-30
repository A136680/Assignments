# gen_hash.py
import uhashlib as hashlib
import ubinascii

def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(256)
            if not chunk:
                break
            h.update(chunk)
    return ubinascii.hexlify(h.digest()).decode()

print(hash_file("firmware.py"))
