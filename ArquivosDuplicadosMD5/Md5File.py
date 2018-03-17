# -*- coding: utf-8 -*-
import hashlib


def md5(fname):

        hash_md5 = hashlib.md5()

        try:
            file = open(fname, "rb")
            with file as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            file.close()
            return hash_md5.hexdigest()
        except PermissionError:
            print("Erro ao abrir o arquivo: %s" % fname)
            return 0
