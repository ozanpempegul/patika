#10/10
def PalindromeTwo(strParam):
    letters = []
    for i in strParam:
        if i.isalpha():
            letters.append(i.lower())
    if letters == letters[::-1]:
        return True
    return False


print(PalindromeTwo("Anne, I vote more cars race Rome-to-Vienna"))
