import hashlib
from Tkinter import Tk
from tkFileDialog import askopenfilename
import Errors


available_hashes = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]


def generate_checksum(hash_method, object_being_hashed):

    if hash_method == available_hashes[0]:
        hasher = hashlib.md5()

    elif hash_method == available_hashes[1]:
        hasher = hashlib.sha1()

    elif hash_method == available_hashes[2]:
        hasher = hashlib.sha224()

    elif hash_method == available_hashes[3]:
        hasher = hashlib.sha256()

    elif hash_method == available_hashes[4]:
        hasher = hashlib.sha384()

    elif hash_method == available_hashes[5]:
        hasher = hashlib.sha512()

    else:
        raise Errors.HashError(hash_method)

    block_size = 65536

    try:

        with open(object_being_hashed, "rb") as a_file:
            buf = a_file.read(block_size)

            while len(buf) > 0:
                hasher.update(buf)
                buf = a_file.read(block_size)

            return hasher.hexdigest()

    except IOError:
        return "File non-existent"


def get_file():
    Tk().withdraw()
    filename = askopenfilename(initialdir="C:/Users/deanw/Downloads/")
    return filename


def check_equal(objects_hash, actual_hash):
    if objects_hash == actual_hash:
        return True
    else:
        return False
