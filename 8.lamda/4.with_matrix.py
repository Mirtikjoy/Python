matr = [
    ['Mirtik joy', 87],
    ['Inraju', 67],
    ['margaret', 98],
    ['achyut', 60],
    ['rojoni', 55]
]

great = list(filter(lambda row : row[1] >= 70, matr))
print(great)