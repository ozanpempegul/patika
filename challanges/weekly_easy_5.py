# 10/10

def FindIntersection(strArr):
  a = strArr[0].split(", ")
  b = strArr[1].split(", ")
  result = ""
  for i in a:
    if i in b:
      result += i + ","
  if result == "":
    return False
  else:
    return result[:-1]