def binary_search():

  list = [x for x in range(50)]
  target = int(input('What do you want from 1-50: '))
  first = 0
  last = len(list)-1

  while (first <= last):
    middle = round((first + last) / 2)

    if target > list[middle]:
      first = middle + 1
    
    elif target < list[middle]:
      last = middle - 1

    else:
      return middle
  
  return None

print(binary_search())
  
