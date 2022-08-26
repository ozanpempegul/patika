def ThreeFiveMultiples(num):
  numbers_list = []
  i = 0
  while i < num:
    if i % 3 == 0 or i % 5 == 0:
      numbers_list.append(i)
    i += 1
  # code goes here
  return sum(numbers_list)

print(ThreeFiveMultiples(10))
