def SimpleMode(arr):
  set_of_arr = set(arr)
  mode_and_count = [arr[0], arr.count(arr[0])]
  for i in set_of_arr:
    if arr.count(i) > mode_and_count[1]:
      mode_and_count[0] = i
      mode_and_count[1] = arr.count(i)
  if mode_and_count[1] == 1:
    return -1
  return mode_and_count[0]