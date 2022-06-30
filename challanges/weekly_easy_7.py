# 10/10

def DashInsert(strParam):
  i = 0
  result = ""
  while i < len(strParam) - 1:
    if int(strParam[i]) % 2 == 1 and int(strParam[i+1]) % 2 == 1:
      result += strParam[i] + "-"
    else:
      result += strParam[i]
    i += 1
  result += strParam[-1]
  return result

print(DashInsert("77993"))
print(DashInsert("567"))
print(DashInsert("2129"))
print(DashInsert("399047"))
print(DashInsert("60497"))
print(DashInsert("667488958374553"))

