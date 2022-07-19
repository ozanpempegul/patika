def fibonacci_generator():
    a,b = 0,1
    while True:
        yield a
        b = a+b
        yield b
        a = a+b

def FibonacciChecker(num):
    for i in fibonacci_generator():
        if i > num:
            return "no"
        elif i == num:
            return "yes"

print(FibonacciChecker(12586269025))

"""def FibonacciChecker(num):
  FIBONACCI_NUMBERS = [0, 1]
  i = 0
  while i < 100:
    k = FIBONACCI_NUMBERS[i] + FIBONACCI_NUMBERS[i + 1]
    FIBONACCI_NUMBERS.append(k)
    i += 1
  if num in FIBONACCI_NUMBERS:
    return "yes"
  # code goes here
  return "no"""