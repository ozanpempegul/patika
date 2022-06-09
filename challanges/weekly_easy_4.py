# 10/10

def Palindrome(strParam):
    if strParam.replace(" ", "") == strParam[::-1].replace(" ", ""):
        return True
    return False
