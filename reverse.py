#Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

from unittest import result


def reverse(l):

    for i in range(len(l)):

        l[i] = l[i][::-1]

    return l

l = [[1, 2], [3, 4], [5, 6, 7]]

l = l[::-1]

result = reverse(l)

print(l)