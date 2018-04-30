#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
from digger import FileDigger


def init(args):
    """
        :param args:
        :return: None

        Initial main start method.

        Here the initial folder scanning will start based on the first parameter, it should be a folder or file.

        args[1] - Initial folder.
    """

    t_app_startup = time.time()

    # Initial folder
    initial_folder = args[1]

    print("\nStarting identification duplicated files process by MD5 hash!")
    print("Initial folder: " + initial_folder)

    # Start digging files...
    duplicated_hashes = FileDigger.dig(initial_folder)

    # Write the result in a csv file
    file_txt = open("duplicates-found.txt", "w")

    file_txt.write("Duplicated files founded in folder %s\n\n" % initial_folder)

    for key, val in duplicated_hashes.items():
        print("Hash Key: %s" % key)
        file_txt.write("Hash Key: %s\n" % key)
        for item in val:
            print("\tPath - %s" % item)
            file_txt.write("\tPath - %s\n" % item)

    t_app_ended = time.time() - t_app_startup

    file_txt.write(("\nFinished in %.3f." % t_app_ended))

    file_txt.close()


# Main
if __name__ == '__main__':
    init(sys.argv)
