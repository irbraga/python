#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
import Md5File


def digg_files(path):

    all_hashes = {}
    hashes_duplicados = {}

    if os.path.isfile(path):
        return Md5File.md5(path)
    elif os.path.isdir(path):
        for caminho, diretorios, arquivos in os.walk(path):
            for arquivo in arquivos:
                hash_retornado = digg_files(caminho + "/" + arquivo)

                if hash_retornado == 0:
                    print("Arquivo ignorado: %s" % arquivo)
                # Se o hash não estiver na lista do que possui todos, adicionar.
                elif not all_hashes.__contains__(hash_retornado):
                    all_hashes.__setitem__(hash_retornado, caminho + "/" + arquivo)

                # Se o hash já existir na lista, adicionar na lista de duplicados.
                else:
                    if hashes_duplicados.__contains__(hash_retornado):
                        hashes_duplicados.__getitem__(hash_retornado).append(caminho + "/" + arquivo)
                    else:
                        caminhos_com_mesmo_hash = [all_hashes.__getitem__(hash_retornado),caminho + "/" + arquivo]
                        hashes_duplicados.__setitem__(hash_retornado,caminhos_com_mesmo_hash)

    else:
        print("Não é nem arquivo nem diretório \_(ツ)_/ -> %s" % os.path.abspath(path))

    return hashes_duplicados
