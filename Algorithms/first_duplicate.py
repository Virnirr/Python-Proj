some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

check = {}

for items in some_list:
  if items not in check:
    check[items] = 0
  check[items] += 1

  if check[items] > 1:
    print(items)
    break
