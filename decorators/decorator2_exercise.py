# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # code here
  def wrapper(*args, **kwargs):
    if (args[0]['valid']):
      print(*args)
      return fn(*args, **kwargs)
  return wrapper
  

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

def super_func(*args, **kwargs):
    total = 0
    print(args)
    print(kwargs) # gives you a dictionary of all the keyword arguments.
                  # {"num":5, "num2":10}
    for items in kwargs.values(): # goes through all the keyword arugments
        total += items # sum of all the values in keyword arguments
    return sum(args) + total # add all of arguments and keyword argument values
 
print(super_func(1,2,3,4,5, num=5, num2=10))