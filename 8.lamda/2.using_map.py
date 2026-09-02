# prices = ['$123.98', '$76.90', '87.75', '$100.20']
prices = input("Enter prices: ").split(',')

price =list(map(lambda p : float(p.replace('$', '')), prices))

total_price = sum(price)


print(price)
print(total_price)