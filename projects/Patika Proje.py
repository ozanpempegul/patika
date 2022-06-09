"""1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi)
oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]"""


def flattener(liste):
    str_list = str(liste)
    str_list = str_list.replace("[", "")
    str_list = str_list.replace("]", "")
    str_list = str_list.replace("'", "")
    new_list = str_list.split(", ")
    print(new_list)


"""2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon 
yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların 
elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]"""


def reverse_list(liste):
    new_list = []
    for i in reversed(liste):
        print(type(i))
        if type(i) == list:
            i.reverse()
            new_list.append(i)
        else:
            new_list.append(i)
    return new_list