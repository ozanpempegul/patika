def VowelCount(strParam):
    vowel_count = 0
    vowels = "aeiou"
    for i in strParam:
        if i in vowels or i in vowels.upper():
            vowel_count += 1
    return vowel_count

# 10 / 10
