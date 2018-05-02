#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from md5 import Md5File
from database import DupFilesDabase


def dig(path):

    """
        :param path: Path to dig for files.
        :return: A List of file hashes with it's related paths.
    """

    all_hashes = DupFilesDabase.create()
    duplicated_hashes = DupFilesDabase.create()

    if os.path.isfile(path):
        return Md5File.md5(path)
    elif os.path.isdir(path):
        for root, directories, files in os.walk(path):

            for file in files:

                full_path = os.path.join(root, file)

                returned_hash = dig(full_path)
                record_on_all_hashes = all_hashes(hash=returned_hash)

                # If the MD5 hash returns 0 the file will be ignored
                if returned_hash == 0:
                    print("File ignored: %s" % full_path)
                # If the hash is not already in the List, add it
                elif len(record_on_all_hashes) == 0:
                    all_hashes.insert(hash=returned_hash, path=full_path)

                # If the hash is in the List, add the hash and the paths to the duplicated_hashes
                else:
                    # As the record was found on the all_hashes, it means it was already added.
                    # Verify now if it's already added to the duplicated_hashes
                    record_on_duplicated = duplicated_hashes(hash=returned_hash)

                    if len(record_on_duplicated) > 0:
                        # If i'ts already added to the duplicated_hashes then append the path do the existing hash.
                        record_on_duplicated[0]['path'].append(full_path)
                        duplicated_hashes.update(record_on_duplicated, path=record_on_duplicated[0]['path'])
                    else:
                        # Else, insert the hash and path to the duplicated_hashes
                        same_hash_paths = [record_on_all_hashes[0]['path'], full_path]
                        duplicated_hashes.insert(hash=returned_hash, path=same_hash_paths)

    else:
        print("It's neither a File or a Folder \_(ツ)_/ -> %s" % os.path.abspath(path))

    return duplicated_hashes
