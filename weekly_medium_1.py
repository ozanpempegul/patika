def CaesarCipher(strParam,num):
  result = ""
  letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in strParam:
    if i in letters:
      result += letters[letters.find(i) + num]
    else:
      result += i
  return result

print(CaesarCipher("ozan", 2))

