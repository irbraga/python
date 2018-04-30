# -*- coding: utf-8 -*-
import hashlib


def md5(file_name):
    """
    :param file_name: File used to calculate a MD5 hash value.
    :return: MD5 hash value.
     
    """

    hash_md5 = hashlib.md5()

    try:
        file = open(file_name, "rb")
        with file as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        file.close()
        return hash_md5.hexdigest()
    except PermissionError:
        print("Error on open file: %s" % file_name)
        return 0
