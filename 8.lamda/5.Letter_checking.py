matr = [
    ['Mirtik joy', 87],
    ['Inraju', 67],
    ['margaret', 98],
    ['achyut', 60],
    ['rojoni', 55]
]

st_m = list(filter(lambda row : (row[0].lower().startswith('m')),matr))
print(st_m)