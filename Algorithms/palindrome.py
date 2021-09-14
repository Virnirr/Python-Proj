phrase = input('Give me a phrase: ')

phrase = phrase.lower().replace(' ', '').replace(',', '').replace('?', '').replace('\"', '').replace('.', '').replace('—', '').replace('!', '').replace("\'", '')

print(phrase)
phrase2 = phrase[::-1]

print(phrase2)
print(bool(phrase == phrase2))