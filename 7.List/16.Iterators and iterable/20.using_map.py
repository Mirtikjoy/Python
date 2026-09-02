letters = ['a','b','c','d']

print(list(map(str.upper, letters)))

numbers = ['1', '2', '3', '4']
print(list(map(int, numbers)))

names = ['mirtik joy molsom', ' rojoni sing molsom', '  achyut ', 'inraju  ']

# print(list(map(str.strip,names)))

for name in map(str.strip,names):
    print(name.capitalize())