__author__ = 'Dean'

import hashlib


def generate_checksum(hash_method, object_being_hashed):

    blocksize = 65536
    hasher = hashlib.sha1()

    try:

        with open(object_being_hashed, "rb") as a_file:
            buf = a_file.read(blocksize)

            while len(buf) > 0:
                hasher.update(buf)
                buf = a_file.read(blocksize)

            return hasher.hexdigest()

    except IOError:
        return "File non-existant"



