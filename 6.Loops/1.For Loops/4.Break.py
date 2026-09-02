names = ['Mirtik joy Molsom', 'Wilson', '', 'inraju', 'achyut']
new_name = []

for name in names:
    if name == '':
        print('Empty value is detected')
        break

    new_name.append(name)
print("Names:- ", ", ".join(new_name))