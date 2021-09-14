# decorator used to wrap functions to give it an enhanced feature
def decorated_function(func):
  def wrap(*args, **kwargs):
    if args[0] < 0:
      print("Give a number 0 or higher")
      return 
    print("This is the start of new function")
    return func(*args, **kwargs)
  return wrap


@decorated_function
def fib1(number):
  num1 = 0
  num2 = 1
  for i in range(number):
    if i % 2 == 0:
      print(num1)
      num1 += num2
    else:
      print(num2)
      num2 += num1

# fibonacci sequence with generators
@decorated_function
def fib2(number):
  a = 0
  b = 1
  for i in range(number):
    yield a # yield a, so a is 0. Give me what a is and pause the function until the next part
    temp = a # temperary variable that hold on to whatever a was
    a = b # modify a to equal to b
    b = temp + b # add it to b 

# fibonacci sequence with recursion
def recurfib(number):
  if number == 0:
    return 0

  if number == 1:
    return 1
  else:
    return recurfib(number-1) + recurfib(number-2)

for x in fib2(5):
  print(x)