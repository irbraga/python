#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
from md5 import Md5File


def dig(path):

    """
        :param path: Path to dig files.
        :return: A List of hashes files with it's related paths.
    """

    all_hashes = {}
    duplicated_hashes = {}

    if os.path.isfile(path):
        return Md5File.md5(path)
    elif os.path.isdir(path):
        for path, directories, files in os.walk(path):
            for file in files:

                returned_hash = dig(path + "/" + file)

                # If the MD5 hash returns 0 the file will be ignored
                if returned_hash == 0:
                    print("File ignored: %s" % path)
                # If the hash is not already on the List, add to the List
                elif not all_hashes.__contains__(returned_hash):
                    all_hashes.__setitem__(returned_hash, path + "/" + file)

                # If the hash is in the List, add the hash and the paths to the duplicated_hashes
                else:
                    if duplicated_hashes.__contains__(returned_hash):
                        duplicated_hashes.__getitem__(returned_hash).append(path + "/" + file)
                    else:
                        same_hash_paths = [all_hashes.__getitem__(returned_hash), path + "/" + file]
                        duplicated_hashes.__setitem__(returned_hash, same_hash_paths)

    else:
        print("It's neither a File or a Folder \_(ツ)_/ -> %s" % os.path.abspath(path))

    return duplicated_hashes
