# 10/10

def even(s):
    even_count = 0
    for i in s:
        if i.isnumeric():
            if even_count == 1 and int(i) % 2 == 0:
                return True
            elif int(i) % 2 == 0:
                even_count += 1
        else:
            even_count = 0

    return False


print(even("7r5gg812"))
