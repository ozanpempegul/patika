def BitwiseOne(strArr):
  result = ""
  i = 0
  while i < len(strArr[0]):
    if (strArr[0][i] == "0" and strArr[1][i] == "0"):
      result += "0"
    else:
      result += "1"
    i += 1

  return result