import re

pattern = re.compile(r'(^[a-zA-Z0-9$%#@]{8,}\d$)')

string = 'someasdfas123dfasdf3fasdfasd3f3'

a = pattern.fullmatch(string)

if not a:
    print('Invalid Password')

else:
    print('success')