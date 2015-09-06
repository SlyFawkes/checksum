
import hashlib
import Errors


def generate_checksum(hash_method, object_being_hashed):

    if hash_method == "md5":
        hasher = hashlib.md5()
    elif hash_method == "sha1":
        hasher = hashlib.sha1()
    elif hash_method == "sha224":
        hasher = hashlib.sha224()
    elif hash_method == "sha256":
        hasher = hashlib.sha256()
    elif hash_method == "sha384":
        hasher = hashlib.sha384()
    elif hash_method == "sha512":
        hasher = hashlib.sha512()
    else:
        raise Errors.HashError(hash_method)

    blocksize = 65536

    try:

        with open(object_being_hashed, "rb") as a_file:
            buf = a_file.read(blocksize)

            while len(buf) > 0:
                hasher.update(buf)
                buf = a_file.read(blocksize)

            return hasher.hexdigest()

    except IOError:
        return "File non-existent"



