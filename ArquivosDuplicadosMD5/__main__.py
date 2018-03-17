#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import FileDigger


def init(args):

    t_inicial = time.time()

    # Arquivo inicial para a busca
    arquivo_inicial = args[1]

    print("\nIniciando o processo de identificação de arquivos duplicados pelo MD5!")
    print("Arquivo inicial: " + arquivo_inicial)

    # Iniciar a busca por arquivos e sub-diretórios
    hashes_duplicados = FileDigger.digg_files(arquivo_inicial)

    # Escreve o resultado em um arquivo csv
    fileTxt = open("arquivos-duplicados.txt", "w")

    fileTxt.write("Arquivos duplicados da pasta %s\n\n" % arquivo_inicial)

    for key,val in hashes_duplicados.items():
        print("Hash: %s" % key)
        fileTxt.write("Hash: %s\n" % key)
        for item in val:
            print("\tCaminho - %s" % item)
            fileTxt.write("\tCaminho - %s\n" % item)

    t_decorrido = time.time() - t_inicial

    print("\nFinalizado em %.3f." % t_decorrido)
    fileTxt.write(("\nFinalizado em %.3f." % t_decorrido))

    fileTxt.close()


# Main
if __name__ == '__main__':
    init(sys.argv)
