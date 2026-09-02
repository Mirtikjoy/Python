names = ['Mirtik joy Molsom', 'Wilson', '', 'inraju', 'achyut']
new_names = []

for name in names:
    if name == '':
        print("Empty value is detected")
        continue
    new_names.append(name)

print("Names are:-",", ".join(new_names))