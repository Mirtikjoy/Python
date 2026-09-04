a = {10,20,30}
b = {10,20,30,40,50}

a.issubset(b)  # Using issubset() method that returns True if all items in the first set are present in the second set
print(a.issubset(b))  

b.issuperset(a)  # Using issuperset() method that returns True if all items in the second set are present in the first set
print(b.issuperset(a))  

a.isdisjoint(b)  # Using isdisjoint() method that returns True if both sets have no items in common
print(a.isdisjoint(b))  
