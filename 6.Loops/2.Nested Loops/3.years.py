years = ["2026", "2027"]
dates = range(1,30)
months = ["jan", "Feb", "March"]

for year in years:
    for month in months:
        for date in dates:
            print(f"{date}-{month}-{year}")
