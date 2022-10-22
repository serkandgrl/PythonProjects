#Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.

def flatten(l):

    for i in l:

        if isinstance(i, list):

            flatten(i)

        else:

            bosListe.append(i)

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

bosListe = []

flatten(l)

print(bosListe)