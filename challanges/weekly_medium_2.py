def FormattedDivision(num1,num2):
  temp = "%.4f" % (float(num1)/num2)
  return "{:,}".format(float(temp))

print(FormattedDivision(9112, 2))

# 9 / 10
#Failed test Cases
# 9112, 2