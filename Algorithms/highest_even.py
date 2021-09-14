# What I did
def heighest_even(li):
  high = 0
  for items in li:
    if items % 2 == 0:
      if items > high:
        high = items
  return high

# Alternative Solution (using list)
def highest_even2(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

random = [10,1,2,3,4,5,6,7,8,11]
print(heighest_even(random))

print(highest_even2(random))