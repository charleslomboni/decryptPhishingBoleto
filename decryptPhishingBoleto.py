# coding: utf-8

#-------------------------------------------------------------------------------
# Name:        decryptPhishingBoleto
# Purpose:     Decryptar a dll que vem junto com o phising do boleto
#              Carvalo Motos Ltda - Bol. 81139
#
# Author:      Charles Lomboni
#
# Created:     28/09/2018
# Copyright:   (c) Charles Lomboni 2018
# Licence:     <MIT licence>
#-------------------------------------------------------------------------------


import argparse
import sys

def getargs():
    # Nome do script
    parser = argparse.ArgumentParser("decryptPhishingBoleto")

    # Argumento necessário
    parser.add_argument("path", help="Path to encrypted file.")

    return parser.parse_args()


def decryptExe(fileName):
    # Executável criptografado convertido em bytes
    byteToModify = bytearray(open(fileName, 'rb').read())

    # Contador
    count = 0

    bytesLen = len(byteToModify) - 2

    # Loop que varre todo o exe para decryptar
    for i in range(bytesLen):

        decryptedByte = byteToModify[i+1] - (0x1A + count)

        if(decryptedByte < 0):
            if(decryptedByte == -1):
                byteToModify[i] = 0xFF
            else:
                byteToModify[i] = decryptedByte * (- 1)
        else:
            byteToModify[i] = decryptedByte

        count += 1
        if(count > 9):
            count = 0
            i += 1

    open(fileName + '_decrypted.dll', 'wb').write(byteToModify)

def main():

    args = getargs()

    print "Iniciando decrypt do executável..."
    decryptExe(args.path)
    print "Finalizado! \o/"

    pass

if __name__ == '__main__':
    main()
