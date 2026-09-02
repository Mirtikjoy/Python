numbers = ['55','78','234','45','87']

n_nub =list(map(lambda num : float(num),numbers))
greater = list(filter(lambda g : g > 70,n_nub))
print(n_nub)
print('greater number: ', greater)
# print(list(filter(str.isalpha,numbers)))