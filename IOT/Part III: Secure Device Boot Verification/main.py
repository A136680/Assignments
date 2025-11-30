# boot.py  (or main.py on MicroPython)
import uhashlib as hashlib
import ubinascii

EXPECTED_FW_HASH = "a3d1ab7fceb305cbd9160cb2381f11e5bf60f78b9a4cda0b2597b32cd73da07a"  # <-- paste from step 2


def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(256)
            if not chunk:
                break
            h.update(chunk)
    return ubinascii.hexlify(h.digest()).decode()


def verify_firmware():
    current_hash = hash_file("firmware.py")
    print("Current firmware hash:", current_hash)
    if current_hash != EXPECTED_FW_HASH:
        print("ERROR: Firmware integrity check FAILED! Refusing to boot.")
        # refuse to boot: stop here
        while True:
            pass
    else:
        print("Firmware integrity OK. Booting...")


# ----- "Boot" sequence -----
verify_firmware()

import firmware
firmware.main_loop()
