# we can access the string through slicing or indexcing
# slicing process is variable[1:3]
# indexcing process is variable[3]

matrix = [
    [3,5,6],
    [6,7,9],
    [56,78,23]
]

print(matrix[0][0]) # accesssing through indexing
print(matrix[0][2]) # accessing through indexing

# let's access through slicing

print(matrix[2])
print(matrix[2][:2:])