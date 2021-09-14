some_list = ['a', 'b','c','b','d','m','n','n']

# a way with dictionary
check = {}

for items in some_list:
  if items in check:
    check[items] += 1
  else:
    check[items] = 1

for items in check:
  if check[items] > 1:
    print(items)


# another way with lists
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
 
print(duplicates)

# With set comprehension and list function
my_list = list({char for char in some_list if some_list.count(char) > 1})
print(my_list)